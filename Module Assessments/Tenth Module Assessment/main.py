# Write a program that sorts an array using the insertion-sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        compareValue = arr[i]
        previousIndex = i - 1
        
        while previousIndex >= 0 and arr[previousIndex] > compareValue:
            arr[previousIndex + 1] = arr[previousIndex]
            previousIndex -= 1
        arr[previousIndex + 1] = compareValue
    return arr
    
randomNumbers = [ 555, 8, 3, 0, 1, 7, 5, 2, 9, 4, 6 , 11, 200, 4, 2]
print(insertion_sort(randomNumbers))