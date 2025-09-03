s= "hello hii heyy"
ns=s.split(" ")[::-1] #slicing operator used to reverse the list
print(*ns) #* is used to print in string format
print(" ".join(ns)) 
print(ns)

k="cea"
print(sorted(k))
print(" ".join(sorted(k)))
