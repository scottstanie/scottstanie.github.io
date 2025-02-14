#!/usr/bin/env python
import re
import shutil
import sys
from pathlib import Path
from dateutil.parser import parse

import yaml


def get_jekyll_title(yaml_data: yaml.YAMLObject) -> str:
    title = yaml_data["title"]
    # make a safe post filename for jekyll as YYYY-mm-dd-title-with-bad-chars-stripped
    # Trim trailing/leading space from title
    # Convert title to lowercase and replace spaces with hyphens
    # Also trim backticks, periods, and replace double hyphens with single hyphens
    # Replace a leading dash with nothing
    safe_title = re.sub(r"[^a-z0-9]+", "-", title.lower())
    safe_title = re.sub(r"^-", "", safe_title)
    safe_title = re.sub(r"-+$", "", safe_title)
    safe_title = re.sub(r"[\[\]\(\)\{\}\.\'`]", "", safe_title)
    safe_title = re.sub(r"--+", "-", safe_title)
    safe_title = re.sub(r"^-+", "", safe_title)

    # Parse out the date from the "created" field
    created_dt = yaml_data["created"]
    if isinstance(created_dt, str):
        created_dt = parse(created_dt)
    new_filename = f"{created_dt.strftime('%Y-%m-%d')}-{safe_title}.md"
    return new_filename


def convert_obsidian_md(in_dir: Path, out_dir: Path, category: str):
    print(f"Creating posts for {category}")
    print("=" * 20)
    for filename in in_dir.iterdir():
        if filename.suffix != ".md":
            continue
        with open(filename) as f:
            content = f.read()

        # Extract YAML front matter
        match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        yaml_header = match.group(1)

        # Parse YAML
        yaml_data = yaml.safe_load(yaml_header)
        # Add the original title to the YAML header
        title = filename.stem
        yaml_data["title"] = title

        # Add category
        yaml_data["category"] = category

        new_filename = get_jekyll_title(yaml_data)
        new_path = out_dir / new_filename

        # Continue if we've already created this:
        if new_path.exists():
            print(f"Already created {new_filename}, skipping")
            continue
        else:
            print(f"Creating {new_path}")

        # Remove the original yaml header from the content
        content = content[match.end() :]
        # Dump YAML back to string
        new_yaml_str = yaml.dump(yaml_data)

        # Find all the Obsidian-specific links for images
        # for example:
        # ![[How SNAPHU treats correlation and looks-1677852084283.jpeg|1/2]]
        # (the |1/2 is optional)
        # This needs to become something with the image template:
        # {% include image.html url="/images/...(file)"  %}
        # We need to do this for all the images in the post

        obsidian_img_regex = r"!\[\[(.*?)(\|.*)?\]\]"

        def replace_obsidian_image(match: re.Match[str]) -> str:
            filename = match.group(1)
            alt_text = match.group(2)

            # Copy image file to destination
            src_path = in_dir.parent / "images" / filename
            dest_path = Path("images") / filename
            shutil.copy(src_path, dest_path)

            return '{{% include image.html url="/images/{}" alt="{}" %}}'.format(
                filename, alt_text
            )

        content = re.sub(obsidian_img_regex, replace_obsidian_image, content)

        # Write new file
        with open(new_path, "w") as f:
            f.write("---\n" + new_yaml_str + "---\n")
            f.write(content)


def _to_site_name(vault_name: str):
    return vault_name.lower().replace(" ", "-")


if __name__ == "__main__":
    try:
        vault_dir = Path(sys.argv[1])
    except IndexError:
        print("Usage: python convert_obsidian.py <path to obsidian vault directory>")
        sys.exit(1)

    subdirs = ["TIL", "Consumed"]  # , "Book Reviews" ]
    post_dir = Path("_posts")
    for d in subdirs:
        name = _to_site_name(d)
        convert_obsidian_md(
            in_dir=vault_dir / d, out_dir=post_dir / name, category=name
        )

    # convert_obsidian_md(out_dir=Path("_posts/til"), category="til")
    # convert_obsidian_md(out_dir=Path("_posts/consumed"), category="consumed")
    # convert_obsidian_md(out_dir=Path("_posts/books"), category="book-review")
