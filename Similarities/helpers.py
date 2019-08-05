from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    aline=a.split('\n')
    bline=b.split('\n')
    result=set()
    for x in aline:
        if x in bline:
            result.add(x.strip("\n"))
    return result



def sentences(a, b):
    """Return sentences in both a and b"""
    a=sent_tokenize(a, language='english')
    b=sent_tokenize(b, language='english')
    result=set()
    for x in a:
        if x in b:
            result.add(x)
    return result


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
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
    return result