def convertlist(l):
    max=len(l)
    st=''
    for r in range(max):
        if r == max-1:
            concateStr = ' and '
        else:
             concateStr = ', '

        if r == 0:
            st = l[r]
        else:
            st += concateStr + l[r]
    return st  

l=[]
st=convertlist(l)
print(st)