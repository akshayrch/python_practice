def mergesort(a,left,right):
    if left < right:
        mid = (left + right)//2
        mergesort(a,left,mid)
        mergesort(a,mid+1,right)
        merge(a,left,mid,right)


def merge(a,left,mid,right):
    i = left
    j = mid + 1
    k = left
    b = [0] * (right + 1)
    while i <=mid and j<=right:
        if a[i] < a[j]:
            b[k] = a[i]
            i = i+1
            k = k+1
        else:
            b[k] = a[j]
            j = j+1
            k = k+1
    while i <=mid:
        b[k] = a[i]
        i = i+1
        k = k+1
    while j <= right:
        b[k] = a[j]
        j = j+1
        k = k+1
    for x in range(left,right+1):
        a[x] = b[x]

list_is = [1,5,3,2,4]

mergesort(list_is,0,len(list_is)-1)
print(list_is)