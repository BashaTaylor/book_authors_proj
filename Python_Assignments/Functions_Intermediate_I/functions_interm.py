# #Here's a little bit of code to get you started, with some test cases and expected outputs. Test each function call one at a time and a few times each to make sure you're getting the correct range.

# #print(randInt()) 		    # should print a random integer between 0 to 100
# import random
# def randInt(min=0, max=100):
#     num = round(random.random()*(max - min)+ min)
#     return num
# print(randInt())


# #print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# import random
# def randInt(max=50):
#     num = round(random.random()*50)
#     return num
# print(randInt(max=50))


# # print(randInt(min=50))            # should print a random integer between 50 to 100
# import random
# def randInt(min=50):
#     num = round(random.random()*50 + 50)
#     return num
# print(randInt(min=50))


# #print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
# import random
# def randInt(min=0, max=100):
#     num = round(random.random()*(max - min)+ min)
#     return num
# print(randInt(min=0, max=500))



# # BONUS: account for any edge cases (eg. min > max, max < 0)
import random
def randInt(min=0, max=100):
    num = round(random.random()*(max - min)+ min)
    if max < min:
        return False
    elif max < 0 or min < 0:
        return False
    else:
        return num
print(randInt(min=10, max=0))



