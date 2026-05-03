import re

file_path = '/Users/moc/Projects/lovesaokhue.github.io/pages/Lộ_Trình_Giáo_Dục_Waldorf_12_Năm.md'
with open(file_path, 'r') as f:
    text = f.read()

pattern = r'(\.|,|\?|!|"|\)|[a-zà-ỹA-Z])([1-9]|1[0-9]|2[0-1])(?=[\s\.\,\;\:]|$)'

works_cited_idx = text.find('#### **Works cited**')
if works_cited_idx != -1:
    main_text = text[:works_cited_idx]
    works_cited = text[works_cited_idx:]
else:
    main_text = text
    works_cited = ""

new_main_text = re.sub(pattern, r'\1[\2](#works-cited)', main_text)
new_text = new_main_text + works_cited

with open(file_path, 'w') as f:
    f.write(new_text)

print("File updated successfully.")
