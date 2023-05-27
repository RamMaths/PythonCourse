def binary_search(list1, value, low, high):
    mid = int((high+low)/2)
    if(list1[mid]>value):
        return binary_search(list1, value, low, mid)
    elif(list1[mid]<value):
        return binary_search(list1, value, (mid+1), high)
    else:
        return mid
