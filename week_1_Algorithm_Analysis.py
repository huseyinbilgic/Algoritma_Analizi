import random



random.random()


s=random.randint(1,100)
print(s)


def get_n_random_numbers(n=10,min_=-5,max_=5):#-5 ve 5 aralığında 10 sayı üretildiç
    numbers=[]
    for i in range(n): # complexity -> n
        numbers.append(random.randint(min_,max_))
    return numbers
get_n_random_numbers()



my_list=get_n_random_numbers(15,-4,4)
print(my_list)



#histogram with two methods



# for a list [0, -4, 8, -1, 0, -3, 6, 3, 0, 1]
# get the histogram , with array of tuples format
histgram_1=[
(-4,1),
(-3,1),
(-1,1),
(0,2),
(1,1),
(3,1),
(6,1),
(8,1),
]


print(sorted(my_list))#dizi sıralandı



def my_frequency_with_dict(list): #complexity ->len(list)
    frequency_dict={} # dict()={}
    for item in list:
        if (item in frequency_dict):#eğer eleman histogramda varsa sayısını 1 arttır
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1#yoksa değerini 1 yap
    return frequency_dict



print(my_frequency_with_dict(my_list))


def my_frequency_with_list_of_tuples(list_1):  #complexity -> BİG O(N2) 
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if (list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list



my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
print(result_1,result_2)


#mode of a list with histogram


my_list_1=get_n_random_numbers(5,-2,2) #dizi üreteldi
my_hist_d=my_frequency_with_dict(my_list_1) #dizinin histogramını oluşturuldu.
print(my_hist_d)



my_hist_l=my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_l)


# to get mode , we have to search all keys on hist_dict
frequency_max=-1 # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
mode=-1
for key in my_hist_d.keys():
    print(key,my_hist_d[key])
    if my_hist_d[key]>frequency_max:
        frequency_max=my_hist_d[key]
        mode=key
print(mode,frequency_max)



# to get mode , we have to search all keys on hist_dict
def my_mode_with_dict(my_hist_d): #complexity -> BİG O(N) 
    frequency_max=-1 # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
    mode=-1
    for key in my_hist_d.keys():
        # print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max



my_list_100=get_n_random_numbers(100,-40,40)
my_hist_1=my_frequency_with_dict(my_list_100)
print(my_mode_with_dict(my_hist_1))



print(sorted(my_list_100))



#mode of a list with histogram ( a list of tuples)


my_list_1=get_n_random_numbers(10)
my_hist_list=my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_list)


# to get mode , we have to search all keys on hist_dict
frequency_max=-1 # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
mode=-1
for item,frequency in my_hist_list:
    print(item,frequency)
    if frequency>frequency_max:
        frequency_max=frequency
        mode=item
print(mode,frequency_max)


#with method
# to get mode , we have to search all keys on hist_dict
def my_mode_with_list(my_hist_list): #complexity -> BİG O(len(my_hist_list))
    frequency_max=-1 # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
    mode=-1
    for item,frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max


my_list_100=get_n_random_numbers(20,-4,4)
my_hist_1=my_frequency_with_list_of_tuples(my_list_100) #histogramı olusturuldu
print(my_mode_with_list(my_hist_1))#modu bulundu


#linear search on list ->doğrusal arama



def my_linear_search(my_list,item_search): #complexity -> BİG O(N)  , iyi durumda -> O(1)
    s=0
    found=(-1,-1) # default, eğer listede yoksa
    n=len(my_list)
    for indis in range(n):
        s+=1
        if my_list[indis]==item_search:
            found=(my_list[indis],indis) # listede bulundu, return bulunn sayı, indisi
            break #uncomment for last found
    return found,s



my_list=get_n_random_numbers(10,-5,5)
print(my_list)


print(my_linear_search(my_list,-3)) #break koyarsak 1 adımda bulur fakat koymassak bulsa dahı lıstenın sonuna kadar arama yapılır yanı 10 olur


#mean of list



my_list=get_n_random_numbers(10,-50,50)
print(my_list)





def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
        mean_=t/s
    return mean_



print(my_mean(my_list))



my_list=get_n_random_numbers(4,-5,5)
print(my_list)
print(my_mean(my_list))


#sort the list


print(my_list)


n=len(my_list)
print(my_list)
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if not(my_list[j]<my_list[j+1]):
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
print(my_list)





# with function
def my_bubble_sort(my_list): #complexity -> BİG O(N2) 
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list



my_list=get_n_random_numbers(4,-5,5)
print(my_list)
print(my_bubble_sort(my_list))



#binary search on a sorted list


def my_binary_search(my_list, item_search): #complexity -> BİG O(LOG n ) 
    found=(-1,-1)
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:#yeni alt liste
            high = mid - 1
        else:
            low = mid + 1#yeni alt liste
    return found # None



my_list_1=get_n_random_numbers(10)
print("liste ",my_list_1)
my_list_2=my_bubble_sort(my_list_1)
print("sırali liste",my_list_2)
print(my_binary_search(my_list_2,3))


#median of a list

size=input("dimension")
size=int(size) # convert str to int
my_list_1=get_n_random_numbers(size)
print("list ",my_list_1)


my_list_2=my_bubble_sort(my_list_1)

print(my_list_2)


def my_median(my_list):
    my_list_2=my_bubble_sort(my_list)
    print(my_list_2)
    n=len(my_list_2)
    print(n)
    if n%2==1:
        middle=int(n/2)
        median=my_list_2[middle]
        print(median)
    else:
        middle_1=my_list_2[int(n/2)-1]
        middle_2=my_list_2[int(n/2)]
        median=(middle_1+middle_2)/2
        print (median)
    return median


my_list_2=get_n_random_numbers(5,-10,10)
print(my_median(my_list_2))

