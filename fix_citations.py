import re

with open('/Users/moc/Projects/lovesaokhue.github.io/pages/Lộ_Trình_Giáo_Dục_Waldorf_12_Năm.md', 'r') as f:
    text = f.read()

# Pattern: we want to match 1-21 when they appear as citations.
# They seem to appear immediately after a dot (.), comma (,), parenthesis ()), question mark (?), exclamation (!), or quote (")
# or right after a word. Wait, let's find all numbers that are not part of other words/phrases.
# Actually, looking at the text, the citations are 1 to 21 attached directly to the preceding word/punctuation.
# Let's search for: `(\.|,|\?|!|"|\)|[a-zà-ỹ])([1-9]|1[0-9]|2[0-1])(?=\s|$)`
# Wait, "Lớp 1" has a space before 1. So it wouldn't match.
# "từ 3 đến 4" has spaces. So they won't match.
# Let's see what this regex finds.

matches = re.finditer(r'(\.|,|\?|!|"|\)|[a-zà-ỹA-Z])([1-9]|1[0-9]|2[0-1])(?=[\s\.\,\;\:]|$)', text)
for m in matches:
    print(f"Matched: '{m.group(0)}' at context: '{text[max(0, m.start()-10):min(len(text), m.end()+10)]}'")
