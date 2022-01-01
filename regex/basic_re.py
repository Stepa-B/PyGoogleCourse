import re
print(re.search(r"or","boRozdin)",re.IGNORECASE))
print(re.search(r"[^a-z]","boRozdin )"))
print(re.findall(r"[a-z| ]","boRozdin boRozdin boRozdin boRozdin boRozdin )"))