import os
import re
from datetime import datetime

# The GitHub action will pass the current timezone as Africa/Lagos
hour = datetime.now().hour

print(f"Current server hour: {hour}")

# Your custom rotation logic
if 7 <= hour < 12:
    img = "profile-season.svg"
elif 12 <= hour < 18:
    img = "profile-gitblock.svg"
elif 18 <= hour < 24:
    img = "profile-night-view.svg"
else:  # 12am to 7am
    img = "profile-night-rainbow.svg"

print(f"Applying image: {img}")

# Read the current README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# The HTML string we want to inject
replacement = (
    f'<!-- 3D-PROFILE-START -->\n'
    f'<div align="center">\n'
    f'  <img src="profile-3d-contrib/{img}" alt="3D GitHub Contribution Graph" width="700"/>\n'
    f'</div>\n'
    f'<!-- 3D-PROFILE-END -->'
)

# Use regex to find everything between START and END markers and replace it
pattern = re.compile(r'<!-- 3D-PROFILE-START -->.*?<!-- 3D-PROFILE-END -->', re.DOTALL)
new_content = pattern.sub(replacement, content)

# Write the changes back to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
