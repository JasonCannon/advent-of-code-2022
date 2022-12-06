s, val = input(), 14

for i in range(val, len(s)):
    if len(set(s[i-val:i])) == val:
        print(i)
        break
