#!/usr/bin/env python
"""Convert Obsidian vault markdown files to Jekyll posts.

Usage:
    python convert_obsidian.py ~/Documents/Research
    python convert_obsidian.py ~/Documents/Research --only fleeting
    python convert_obsidian.py ~/Documents/Research --only til consumed
    python convert_obsidian.py ~/Documents/Research --dry-run
"""
import argparse
import re
import shutil
from pathlib import Path

import yaml
from dateutil.parser import parse

# Mapping of vault folder name -> (jekyll output subdir, category)
SYNC_FOLDERS = {
    "TIL": ("til", "til"),
    "Consumed": ("consumed", "consumed"),
    "Microposts": ("notes", "notes"),
    "Posts": ("articles", "articles"),
}


def get_jekyll_filename(yaml_data: dict) -> str:
    """Generate a Jekyll-compatible filename like YYYY-MM-DD-title-slug.md."""
    title = yaml_data["title"]
    safe_title = re.sub(r"[^a-z0-9]+", "-", title.lower())
    safe_title = re.sub(r"^-+|-+$", "", safe_title)
    safe_title = re.sub(r"-{2,}", "-", safe_title)

    created_dt = yaml_data["created"]
    if isinstance(created_dt, str):
        created_dt = parse(created_dt)
    return f"{created_dt.strftime('%Y-%m-%d')}-{safe_title}.md"


def build_post_title_index() -> dict[str, str]:
    """Build a mapping of post title (lowercase) -> URL from existing Jekyll posts."""
    index = {}
    for f in Path("_posts").rglob("*.md"):
        text = f.read_text()
        match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not match:
            continue
        yaml_data = yaml.safe_load(match.group(1))
        title = yaml_data.get("title", "")
        # Use explicit permalink if set, otherwise derive from filename
        if "permalink" in yaml_data:
            url = yaml_data["permalink"]
        else:
            slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.stem)
            url = f"/{slug}/"
        index[title.lower()] = (title, url)
    return index


def resolve_wikilinks(content: str, post_index: dict[str, str]) -> str:
    """Convert [[wikilinks]] to markdown links when a matching post exists."""

    def _replace_wikilink(match: re.Match[str]) -> str:
        target = match.group(1)
        display = match.group(2) or target
        display = display.lstrip("|")

        lookup = target.lower()
        if lookup in post_index:
            title, url = post_index[lookup]
            return f"[{display}]({url})"
        return display

    # [[link|display text]] and [[link]]
    content = re.sub(r"\[\[([^\]\|]+)(\|[^\]]*)?\]\]", _replace_wikilink, content)
    return content


def replace_obsidian_images(content: str, vault_dir: Path) -> str:
    """Convert ![[image.png|alt]] to Jekyll image includes, copy image files."""
    obsidian_img_regex = r"!\[\[(.*?)(\|.*)?\]\]"

    def _replace(match: re.Match[str]) -> str:
        img_filename = match.group(1)
        alt_text = match.group(2) or ""
        alt_text = alt_text.lstrip("|")

        src_path = vault_dir / "images" / img_filename
        dest_path = Path("images") / img_filename
        if src_path.exists():
            shutil.copy(src_path, dest_path)
        else:
            print(f"  WARNING: image not found: {src_path}")

        return '{{% include image.html url="/images/{}" alt="{}" %}}'.format(
            img_filename, alt_text
        )

    return re.sub(obsidian_img_regex, _replace, content)


def convert_file(filepath: Path, out_dir: Path, category: str, vault_dir: Path, post_index: dict, *, dry_run: bool = False) -> bool:
    """Convert a single Obsidian markdown file to a Jekyll post.

    Returns True if a new file was created, False if skipped.
    """
    content = filepath.read_text()

    # Extract YAML front matter
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print(f"  Skipping {filepath.name} (no YAML front matter)")
        return False
    yaml_data = yaml.safe_load(match.group(1))

    # Title from filename (Obsidian convention)
    # Strip leading date prefix like "2025-07-11 " if present
    title = filepath.stem
    title = re.sub(r"^\d{4}-\d{2}-\d{2}\s+", "", title)
    yaml_data["title"] = title
    yaml_data["category"] = category

    new_filename = get_jekyll_filename(yaml_data)
    new_path = out_dir / new_filename

    if new_path.exists():
        return False

    if dry_run:
        print(f"  [dry-run] Would create {new_path}")
        return True

    print(f"  Creating {new_path}")

    # Strip YAML header from content body
    body = content[match.end():]

    # Convert Obsidian syntax
    body = replace_obsidian_images(body, vault_dir)
    body = resolve_wikilinks(body, post_index)

    new_yaml_str = yaml.dump(yaml_data, default_flow_style=False)
    new_path.write_text(f"---\n{new_yaml_str}---\n{body}")
    return True


def sync_folder(vault_dir: Path, vault_subdir: str, out_subdir: str, category: str, post_index: dict, *, dry_run: bool = False):
    """Sync all .md files from a vault subfolder to a Jekyll posts subfolder."""
    in_dir = vault_dir / vault_subdir
    out_dir = Path("_posts") / out_subdir

    if not in_dir.exists():
        print(f"Skipping {vault_subdir}/ (not found in vault)")
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{vault_subdir}/ -> _posts/{out_subdir}/")
    print("-" * 40)

    created = 0
    skipped = 0
    for filepath in sorted(in_dir.iterdir()):
        if filepath.suffix != ".md":
            continue
        if convert_file(filepath, out_dir, category, vault_dir, post_index, dry_run=dry_run):
            created += 1
        else:
            skipped += 1

    print(f"  {created} new, {skipped} already synced")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("vault_dir", type=Path, help="Path to Obsidian vault root")
    parser.add_argument(
        "--only",
        nargs="+",
        choices=[v[0] for v in SYNC_FOLDERS.values()],
        help="Only sync specific categories (e.g. --only fleeting consumed)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing files")
    args = parser.parse_args()

    assert args.vault_dir.is_dir(), f"Vault directory not found: {args.vault_dir}"

    post_index = build_post_title_index()

    for vault_subdir, (out_subdir, category) in SYNC_FOLDERS.items():
        if args.only and out_subdir not in args.only:
            continue
        sync_folder(args.vault_dir, vault_subdir, out_subdir, category, post_index, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
