#test for substrings

a="tests"
b="tests"
n=4
j=0
k=n
i=0
l=n
result=set()
alist=[]
blist=[]
for x in range((len(a))-(n-1)):
    alist.append(a[j:k])
    j+=1
    k+=1
for x in range((len(a))-(n-1)):
    blist.append(b[i:l])
    i+=1
    l+=1
for x in alist:
    if x in blist:
        result.add(x)
print (alist)
print (blist)
print (result)