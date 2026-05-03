import re

file_path = '/Users/moc/Projects/lovesaokhue.github.io/pages/Lộ_Trình_Giáo_Dục_Waldorf_12_Năm.md'
with open(file_path, 'r') as f:
    text = f.read()

# Pattern matches the current format: [number](#works-cited)
# Note that we need to escape [ and ] in regex
pattern = r'\[([0-9]+)\]\(#works-cited\)'

# New format: <sup>[number](#works-cited)</sup>
# This will make it a superscript link
replacement = r'<sup>[\1](#works-cited)</sup>'

new_text = re.sub(pattern, replacement, text)

with open(file_path, 'w') as f:
    f.write(new_text)

print("Citation style updated to superscript.")
