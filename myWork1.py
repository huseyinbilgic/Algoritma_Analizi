import random

#random sayıları oluşturmak için kullanıldı.
def random_numbers(n,min,max):
    numbers=[]
    for i in range(n): 
        numbers.append(random.randint(min,max))
    return numbers


def getModeMedian(list_1): #total complexity=>O(n^2+n+n+1)~O(n^2) diyebiliriz.
    n=len(list_1)
    frequency_max=-1 # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
    mode=-1
    frequency_dict={} 

    for i in range(n-1,-1,-1):#listeyi sıralamak için bubble sort kullanıldı. complexity=> O(n^2+...)~O(n^2)
        for j in range(0,i):
            if not(list_1[j]<list_1[j+1]):
                temp=list_1[j]                          #=>swap işlemi kullanılarak sıralandı.
                list_1[j]=list_1[j+1]      
                list_1[j+1]=temp
    print("List: "+str(list_1))


    for item in list_1:#listenin histogramı alındı.complexity=> O(n)
        if (item in frequency_dict):#eğer eleman histogramda varsa sayısını 1 arttır
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1#yoksa değerini 1 yap
    print("Dict of List: "+str(frequency_dict))
    
    #Median bulundu.#complexity=>O(1)
    median=0
    if n%2==1:# tek sayıda eleman varsa ortadaki alırız.
        middle=int(n/2)
        median=list_1[middle]
    else:# çift sayıda eleman varsa ortadaki iki elemanın ortalamasını alırız.
        middle_1=list_1[int(n/2)-1]
        middle_2=list_1[int(n/2)]
        median=(middle_1+middle_2)/2

    #Histogramdan Mod bulundu. complexity=>O(n)
    mode=0
    for key in frequency_dict.keys():     #her bir key adedine bakarak en büyük olanı alırız.
        if frequency_dict[key]>frequency_max:
            frequency_max=frequency_dict[key]
            mode=key


    return mode,median



list_1=random_numbers(10,-4,4)
mode,median=getModeMedian(list_1)
print("mode: {} median:{}".format(mode,median))

