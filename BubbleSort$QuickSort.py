
# Bubble Sort
def sort1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


 # Quick Sort (Using recursion)
def sort2(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return sort2(left) + middle + sort2(right)

def main():
    # List 1
    list1 = [8, 3, 6, 5, 7, 2, 1, 9, 4]
    print("Before sorting , List1:", list1)
    sort1(list1)
    print("After sorting , list1:", list1)

    # List 2
    list2 = [14, 19, 11, 13, 15, 17, 12, 16, 18]
    print("Before sorting , list2:", list2)
    list2 = sort2(list2)
    print("After sorting , list2:", list2)


if __name__ == "__main__":
    main()

