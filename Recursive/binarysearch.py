import math

def mid(l):
    l.sort()
    lenList = len(l)
    if lenList % 2 == 0:
        median = math.floor((0.5*((lenList/2) + ((lenList/2) + 1) )))
        return median
    elif lenList % 2 != 0:
        median = math.floor((lenList+1)/2)
        return median

def binarySearch(l, t, m):
    if not l :
        return 'there is no data'
    else:
        entryTest = m
        if l[entryTest] == t:
            return 'data found from entry '+ str(t)
        if t < l[entryTest]:
            return binarySearch(l, t, entryTest -1 )
        if t > l[entryTest]:
            return binarySearch(l, t, entryTest + 1 ) 
            
        



list = [0,1,3,4,5,6,7,8,1,9,7,12]
name = ['ana', 'dean', 'rafi', 'idan', 'rusel', 'arif']
# print(binarySearch(list, 9, mid(list)))
print(binarySearch(name, '', mid(name)))
