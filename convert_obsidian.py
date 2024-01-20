import re
import shutil
import sys
from pathlib import Path
from dateutil.parser import parse

import yaml

posts_dir = Path(sys.argv[1])

for filename in posts_dir.iterdir():
    if filename.suffix != ".md":
        continue
    with open(filename) as f:
        content = f.read()

    # Extract YAML front matter
    match = re.search(r"^---\n(.*)\n---", content, re.DOTALL)
    yaml_header = match.group(1)

    # Parse YAML
    yaml_data = yaml.safe_load(yaml_header)

    # Add title
    title = filename.stem
    yaml_data["title"] = title

    # Remove the original yaml header from the content
    content = content[match.end() :]
    # Dump YAML back to string
    new_yaml_str = yaml.dump(yaml_data)

    # Parse out the date from the "created" field
    created_dt = yaml_data["created"]
    if isinstance(created_dt, str):
        created_dt = parse(created_dt)

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
        src_path = posts_dir.parent / "images" / filename
        dest_path = Path("images") / filename
        shutil.copy(src_path, dest_path)

        return '{{% include image.html url="/images/{}" alt="{}" %}}'.format(
            filename, alt_text
        )

    content = re.sub(obsidian_img_regex, replace_obsidian_image, content)

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

    new_filename = f"{created_dt.strftime('%Y-%m-%d')}-{safe_title}.md"

    # Write new file
    with open(new_filename, "w") as f:
        f.write("---\n" + new_yaml_str + "---\n")
        f.write(content)
