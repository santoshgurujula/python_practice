import random
numberofStreaks=0
def checkCount(l):
    prevChr=''
    numberofStreaks =0
    streak=0
    for i in range(len(l)):
        if prevChr!=l[i]:
            prevChr=l[i]
            if(streak//6 >0):
                print('Count:',streak)
                print('list',i)
                print(l)
            numberofStreaks=numberofStreaks+( streak//6)
            streak=0
            
        else:
            streak+=1
    #print(numberofStreaks)
    return numberofStreaks


for experimentNumber in range(2):
    newList =[]
    for listcount in range(101):
        if(random.randint(0,1) ==0):
            newList.append('T')
        else:
            newList.append('H')
    numberofStreaks+=checkCount(newList)
print('Chance of streak: %s%%' %(numberofStreaks/100))    

