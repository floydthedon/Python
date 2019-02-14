#quicksort.py
#Implements the quicksort algorithm using the first index of each partition as the pivot

def quick(slist, start, stop):

    if start >= stop:
        return slist
    else:
        pivot = slist[start-1]
        pivIndex = start - 1

        #moves the numbers that meet the condition in front of the pivot
        #   then partitions the list
        for i in range(start, stop):
            if slist[i] < pivot:
                slist.insert(start-1, slist.pop(i))
                pivIndex += 1
                
        quick(slist, start, pivIndex)
        quick(slist, pivIndex + 2, stop)
        return slist
        

def main():

    start = 1
    
    mylist = [5, 3, 8, 6, 1, 9, 0, 2, 4, 7]

    sortList = list(mylist)

    print(mylist)

    donesort = quick(sortList, start, len(sortList))

    print(donesort)

main()
        
