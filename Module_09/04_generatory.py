def all_variants(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            yield s[i:j]


text = "abc"
for var in all_variants(text):
    print(var)
