def collatz(userval):
    if userval%2==0:
        ret = userval//2
        
    else:
        ret= 3*userval+1
    print(ret)
    return ret

print('Enter number:')
try:
    userval=int(input())
    while(userval!=1):
        userval=collatz(userval)
except ValueError:
    print('invalid number')


