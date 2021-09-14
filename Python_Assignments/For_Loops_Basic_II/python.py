#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     print(list)
# biggie_size([-1, 3, 5, -5])


#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def positives(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             count += 1
#     arr[-1] = count
#     return arr
# print(positives([-1,1,1,1,1,5]))

#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def totalsum(arr):
#     count = 0
#     for i in range(len(arr)):
#         count = count + arr[i]
#     return count
# print(totalsum([2,3,4,5]))
# print(totalsum([-1,8,-3,5]))

#4 Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def Average(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum / len(arr)
# print(Average([1,3,5,8]))
# print(int(Average([1,2,4,5])))

#5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(list):
#     count = 0

#     for i in list:
#         count += 1
    
#     return count

# print(length([37,2,1,-9]))
# print(length([]))

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def mini(arr):
#     min = arr[0]
#     if len(arr) == 0:
#         return False
#     for i in arr: 
#         if i < min:
#             min = i
#     return min
# print(mini([37,2,1,-9]))
# print(mini([]))

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(list):
#     maximum=list[0]
#     i=1
#     if len(list)<=1:
#         return False
#     for i in range(len(list)):
#         if maximum<list[i]:
#             maximum=list[i]
#     print(maximum)
# maximum([37,2,1,-9])
# maximum([])

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(list):
#     sumTotal = 0
#     size = len(list)
#     minimum = list[0]
#     maximum = list[0] 

#     for i in range (0, size, 1):
#         sumTotal += list[i]
#         if (list[i] > maximum):
#             maximum = list[i]
#         if (list[i] < minimum):
#             minimum = list[i]

#     average = sumTotal / size
#     dict = {
#         'sumTotal': sumTotal,
#         'average': average,
#         'minimum': minimum,
#         'maximum': maximum,
#         'length': size
#     }
#     return dict

# print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    for i in range (0, int(len(list) / 2), 1):
        temp = list[i]
        list[i] = list[len(list) - i - 1]
        list[len(list) - 1 - i] = temp
    return list
print(reverse_list([37,2,1,-9]))