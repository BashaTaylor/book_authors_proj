#1
# for i in range(1, 10, 1):
#     print(i)

# Answer; 1,2,3,4,5,6,7,8,9

# 2
# for t in range(1, 10, 3):
#     print(t)

# Output: 1,4,7

#3
# for y in range(5):
#     if y < 5:
#         print(y)
#     elif y == 3:
#         print("y is 3")

# output: 0,1,2,3,4

#4
# for j in range(20, 1, -3):
#     print(j)

# output: 20,17,14,11,8,5,2

#5
# cities = ["London", "Paris", "Tokyo"]
# for city in cities:
#     print(city)

# output:
# London Paris Tokyo

#6
# numbers = [7, 13, 8, 42]
# for x in range(0, len(numbers)):
#     print(x)
#     print(numbers[x])
# if numbers[len(numbers) - 1] == 42:
#     print("The answer to life, the universe, and everything.")

# output: 0,7,1,13,2,8,3,42

#6
# numbers = [7, 13, 8, 42]
# for x in range(0, len(numbers)):
#     print(x)
#     print(numbers[x])
# if numbers[len(numbers) - 1] == 42:
#     print("The answer to life, the universe, and everything.")

# if the length of numbers (which is 4) minus 1 (which is 3) == 42, then the POSITION 5 OF THE ARRAY (that is 42) equals to 42, then we print it

# output: 0,7,1,13,2,8,3,42,The answer to life, the universe, and everything.

#7
# for num in range(10):
#     if num % 2 == 0:
#         print("Hello")
#     elif num % 4 == 0:
#         print("World")
#     else:
#         print(num)

# output: Hello, 1, Hello, 3, Hello, 5, Hello, 7, Hello, 9

#8
# for num in range(10):
#     if num % 4 == 0:
#         print("Hello")
#     elif num % 2 == 0:
#         print("World")
#     else:
#         print(num)

# output: Hello, 1, Hello, 3, Hello, 5, Hello, 7, Hello, 9

#9
# pet_info = {
# "name": "Fido", 
# "age": 4, 
# "trick": "rolls over"
# }
# for key in pet_info:
#     print(key)
#     print(pet_info[key])

# output:
# name, Fico, age, 4, trick, rolls over

#10
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)

# output:
# First, I will use the 20 minute rule and use the platform and other resources to find my answer
# Second, I will ask my classmates for help, like how I would ask a fellow employee at my job
# Third, I will ask an available TA in a public setting, so everyone can benefit from my question
# Fourth, I will ask an available instructor





