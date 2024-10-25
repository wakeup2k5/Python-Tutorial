# Write a program that sorts the array using merge-sort algorithm.

def merge_sort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr) // 2]
        rightArr = arr[len(arr) // 2:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
    
    return arr
    
randomNumbers = [ 555, 8, 3, 0, 1, 7, 5, 2, 9, 4, 6 , 11, 200, 4, 2]
print(merge_sort(randomNumbers))