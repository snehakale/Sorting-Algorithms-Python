"""
    Following program implements quick sort algorithm.
    It takes one input list and prints sorted output list.
"""

# Function to call for quicksort algorithm 
def quicksort(array, low, high):
    if low < high:
        splitpoint = getSplitPoint(array, low, high)
        quicksort(array, low, splitpoint-1);
        quicksort(array, splitpoint+1, high);
    return array;

# Function to get split point (pivot)
def getSplitPoint(array, low, high):
    pivot = array[high];
    i = low -1;
    
    for j in range(low, high):
        if(array[j] <= pivot):
           i= i+1;
           array[i],array[j] = array[j],array[i];
           
    array[i+1],array[high] = array[high],array[i+1];
    return (i+1);

# testing with an input
test = [20, 10, 60, 50, 30]

# setting value for 'high'
high = len(test)-1;

# printing output
print("Before sorting : " + str(test))
print("After soerting : " + str(quicksort(test, 0, high)))
