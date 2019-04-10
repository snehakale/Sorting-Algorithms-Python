"""
    This program implements merge sort.
    It takes a list and prints a sorted list.
"""

# Function to call merge sort
def mergesort(arr):
    if len(arr) > 1:
        # middle of the array
        mid = len(arr) // 2
        
        # Dividing into two halves
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # recursiely calling merge sort
        mergesort(leftArr)
        mergesort(rightArr)

        # initialising variables
        i = j = k = 0

        # while loop for comparing and merging
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i = i + 1
            else:
                arr[k] = rightArr[j]
                j = j + 1
            k = k + 1

        # while loop fo copying elements of left half
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i = i + 1
            k = k + 1

        # while loop for copying elements of right half
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j = j + 1
            k = k + 1
                

# test list
test = [10, 3, 87, 15, 6, 34, 48, 87, 48]
print("Before sorting : " + str(test))
# calling and printing mergesort
mergesort(test)
print("After sorting : " + str(test))
