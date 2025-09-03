from collections import defaultdict
strs=list(map(str,input().split()))
d=defaultdict(list)
for word in strs:
    s_word= "".join(sorted(word))
    d[s_word].append(word)
result = sorted(d.values(), key=lambda x:-len(x))
print(result) 
