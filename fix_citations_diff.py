import re
import difflib

file_path = '/Users/moc/Projects/lovesaokhue.github.io/pages/Lộ_Trình_Giáo_Dục_Waldorf_12_Năm.md'
with open(file_path, 'r') as f:
    text = f.read()

# Pattern: match 1 to 21 immediately preceded by punctuation or letter, and followed by space or punctuation or EOF.
pattern = r'(\.|,|\?|!|"|\)|[a-zà-ỹA-Z])([1-9]|1[0-9]|2[0-1])(?=[\s\.\,\;\:]|$)'

# Be careful with the Works Cited section itself!
# "#### **Works cited**" is at the end. We shouldn't touch anything in or after it.
works_cited_idx = text.find('#### **Works cited**')
if works_cited_idx != -1:
    main_text = text[:works_cited_idx]
    works_cited = text[works_cited_idx:]
else:
    main_text = text
    works_cited = ""

new_main_text = re.sub(pattern, r'\1[\2](#works-cited)', main_text)

new_text = new_main_text + works_cited

# generate diff
diff = list(difflib.unified_diff(
    text.splitlines(keepends=True),
    new_text.splitlines(keepends=True),
    fromfile='Original',
    tofile='Modified'
))
print(''.join(diff))
