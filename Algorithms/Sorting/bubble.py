def bubble(slist):
    swap = 0
    passes = 0

    swapped = True
    
    slist = list(slist)

    while swapped:
        swapped = False
        for j in range(len(slist)-1):
            if slist[j] > slist[j+1]:
                temp = slist[j]
                slist[j] = slist[j+1]
                slist[j + 1] = temp
                swap += 1
                swapped = True

        passes += 1

    print("Swaps:", swap)
    print("Passes:", passes)
    print()
    return slist

def revbubble(slist):
    swaps = 0
    passes = 0

    swapped = True

    slist = list(slist)

    while swapped:
        swapped = False
        for j in range(len(slist)-1):
            if slist[j] < slist[j+1]:
                temp = slist[j]
                slist[j] = slist[j+1]
                slist[j + 1] = temp
                swaps += 1
                swapped = True

        passes += 1

    print("Reverse Swaps:", swaps)
    print("Reverse Passes:", passes)
    print()
    return slist

def main():

    mylist = [0, 1, 2, 4, 3, 6, 5, 7, 8, 9]

    donesort = bubble(mylist)
    rev = revbubble(donesort)

    
    print(mylist)
    print(donesort)
    print(rev)

main()
