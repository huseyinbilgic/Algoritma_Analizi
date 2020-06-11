

import random

def my_search(list1, x):
    s=0
    for i in list1:
        s+=1
        if x == i:
            return True,s
    return False,s

list1=[0,1,2,5]

list1[1]=-10

for i in range(10):
    list1.append(i*10)



def check_prime(n):
    s=0
    if n!=1:
        for factor in range(2,n):
            s+=1
            if n%factor == 0:
                return False,s
    else:
        return False,s
    return True,s


print(check_prime(10),check_prime(13),check_prime(23),check_prime(310))




numbers=[10,13,23,310,69,49]

for num_ in numbers:
    print(num_, check_prime(num_))

x=1
print(my_search(numbers,x))






def getMyList(s):
    list1=[]
    for i in range(s):
        t=int(random.uniform(0,1000))
        list1.append(t)
    return list1

def getMyNumber():
    return int(random.uniform(0,1000))


myList = getMyList(10)
myNumber = getMyNumber()
print(myNumber, myList)
print(my_search(myList,myNumber))

print("Liste boyutu " ,len(myList))





mySearchNumbers=[2,45,78,-34,55]
t=0
for x in mySearchNumbers:
    t1=my_search(myList,x)[1]
    t=t+t1
#print("Ortalama değer ",b)
t, t/len(mySearchNumbers)


def my_search_complexity(numOfItem=10, numOfTrials=5):
    my_list = getMyList(numOfItem)
    
    mySearchNumbers=getMyList(numOfTrials)
    
    print("Liste boyutu " ,len(my_list))
    t=0
    for x in mySearchNumbers:
        t1=my_search(my_list,x)[1]
        t=t+t1
    #print("Toplam değer, Ortalama değer")
    print(t, t/len(mySearchNumbers))

my_search_complexity(10,5)
my_search_complexity(50,25)
my_search_complexity(100,50)
my_search_complexity(1000,500)
my_search_complexity(1000,800)
my_search_complexity(1000,900)










