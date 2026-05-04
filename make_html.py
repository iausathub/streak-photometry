#--------------------------------------------------------------------------------------------------#
# make_html.py                                                                                     #
# Developed by Kiyoaki Okudaira * University of Washington / Kyushu University / IAU CPS SatHub    #
#--------------------------------------------------------------------------------------------------#
# Description                                                                                      #
#--------------------------------------------------------------------------------------------------#
# Make HTML file showing results of SatChecker                                                     #
# This code is written for ASTR 499 undergraduate research with Dr. Meredith                       #
#--------------------------------------------------------------------------------------------------#

import os
import re

# Settings
input_txt = "/astro/store/shire/kiyoaki/ASTR499/path_list.txt"
output_dir = "/astro/store/shire/kiyoaki/ASTR499/output/satchecker/plot"
output_html = os.path.join(output_dir, "image_gallery.html")
images_per_row = 3

# Extract L number
def extract_L_number(filepath):
    filename = os.path.basename(filepath)
    match = re.search(r"L(\d{4})", filename)
    return int(match.group(1)) if match else 9999

# Read PATH list
with open(input_txt, "r") as f:
    paths = [line.strip() for line in f if line.strip()]

# Sort by L number
paths_sorted = sorted(paths, key=extract_L_number)

# Make HTML
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>SatChecker Image Gallery</title>
<style>
body { font-family: Arial, sans-serif; margin: 20px; }
.gallery-row { display: flex; gap: 12px; margin-bottom: 20px; }
.image-container { width: 260px; text-align: center; }
.image-container img {
    max-width: 260px;
    height: auto;
    border: 1px solid #ccc;
}
.filename {
    font-size: 12px;
    margin-top: 6px;
    word-break: break-all;
}
</style>
</head>
<body>
<h2>SatChecker Image Gallery (Sorted by L Number)</h2>
"""

for i in range(0, len(paths_sorted), images_per_row):
    html += '<div class="gallery-row">\n'
    for path in paths_sorted[i:i+images_per_row]:
        filename = os.path.basename(path)
        html += f"""
        <div class="image-container">
            <img src="{filename}">
            <div class="filename">{filename}</div>
        </div>
        """
    html += "</div>\n"

html += """
</body>
</html>
"""

# Save
with open(output_html, "w") as f:
    f.write(html)

print(f"HTML created: {output_html}")