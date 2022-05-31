import time 
import random 


def sel_sort(a):
    n = len(a)
    
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    
def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    
    pivot = ls[len(ls) // 2]
    less_ls, equal_ls, greater_ls = [], [], []
    for num in ls:
        if num < pivot:
            less_ls.append(num)
        elif num > pivot:
            greater_ls.append(num)
        else:
            equal_ls.append(num)
    return quick_sort(less_ls) + equal_ls + quick_sort(greater_ls)

   
ls = [x for x in range(10001)] 
random.shuffle(ls) 
ls2 = ls[:] 

start = time.time()   
sel_sort(ls) # selection sort time
sel_time = time.time() - start 

start = time.time()
quick_sort(ls2) # quick sort time
quick_time = time.time() - start

print('selection sort time: ', sel_time)
print('quick sort time: ', quick_time)