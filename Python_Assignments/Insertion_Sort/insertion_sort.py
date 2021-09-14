# Create a function to do insertion sort
# Traverse through 1 to len(arr)
# Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
# Specify the array
# Call the function
# Specify and print new array


def insertionSort(arr):
    for index in range(1,len(arr)):

        currentvalue = arr[index]
        position = index

        while position>0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position = position-1

        arr[position]=currentvalue

arr = [6,5,3,1,8,7,2,4]
insertionSort(arr)
print(arr)