def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        # Initially, assume the first element of the unsorted part as the minimum.
        minimum = i

        for j in range(i+1, n):
            if (arr[j] < arr[minimum]):
                # Update position of minimum element if a smaller element is found.
                minimum = j
        # Swap the minimum element with the first element of the unsorted part.
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
    return arr

# # Driver code
arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(selectionSort(arr))

