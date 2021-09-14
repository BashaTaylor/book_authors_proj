#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    myNumbers = []
    for i in range (num,-1,-1):
        myNumbers.append(i)
    return myNumbers
print(countdown(50))

# 2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2


def ugh():
    a = 4
    print(a)
    if a > 20:
        return 6
    else:
        return 7
print(ugh())


#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
                                    #my seudo code:
practice = [10,20,30,40,50]         #creatin and naming my list
def first_plus_length(my_list):     #creating the function
    sum = my_list[0] + len(my_list) #defining the sum
    print(sum)                      #printing the sum
first_plus_length(practice)         #calling the function

#extra one for more practice
your_list = [1,7,8,-3]
first_plus_length(your_list)


# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
try_this = [2,4,6,7,9,11]
new = []
def values_grater_than_second(list):
    for val in list:
        if val > list[1]:
            new.append(val)
    for val in new:
        if len(new) < 2:
            return False
    return new

print(values_grater_than_second([2,4,6,7,9,11]))
print(len(new))

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

new = []
def this_length_that_value(size, value):
    for b in range(size):
        new.append(value)
    return new

print(this_length_that_value(2,9))





