from collections import Counter
s=input() #tree
d=Counter(s)
u_d=sorted(d.items(),key=lambda x:-x[1])
result=""
for key, value in u_d:
    result+=key*value
print(result)
