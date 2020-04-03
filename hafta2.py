def my_f_1(l1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(l1)
    s=0
    maxsum=0
    for i in range(n):
        for j in range(i,n):
            t=0
            for k in range(i,j):
                t+=l1[k]
                s+=1
            if t>maxsum:
                maxsum=t
    return maxsum,s

def my_f_2(l1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(l1)
    maxsum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            #print(i,j)
            t+=l1[j]
            #print("toplam"+str(t))
            if t>maxsum:
                maxsum=t
    return maxsum


def my_f_3(l1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(l1)
    s=0
    maxsum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            #print(i,j)
            t+=l1[j]
            s+=1
            #print("toplam"+str(t))
            if t>maxsum:
                i_1,i_2=i,j
                maxsum=t
    return maxsum,i_1,i_2,s

print(my_f_1(),my_f_2(),my_f_3())


def my_f_recursive(l1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(l1)
    if n==1:
        return l1[0]
    else:
        left=l1[0:n//2]
        right=l1[(n//2):n]

        left_sum=my_f_recursive(left)
        right_sum=my_f_recursive(right)
        center_sum=0
        temp_sum_left=0
        t=0
        for i in range(n//2,-1,-1):
            t=t+l1[i]
            if t>temp_sum_left:
                temp_sum_left=t
        temp_sum_right=0
        t=0
        for i in range(n//2,n):
            t=t+l1[i]
            if t>temp_sum_right:
                temp_sum_right=t
        center_sum=temp_sum_left+temp_sum_right
        return max_of_three(left_sum,right_sum,center_sum)
def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
def max_of_three(a,b,c):
    return (max_of_two(a,max_of_two(b,c)))

print(my_f_recursive())