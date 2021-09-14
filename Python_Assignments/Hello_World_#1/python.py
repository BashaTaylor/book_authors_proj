# 1. TASK: print "Hello World"
# print("Hello World")


# 2. print "Hello {{your name}}!" with the name in a variable
	# with a comma
# # print("Hello" + " " + name)	# with a +; or:
# print("hello " + name)

# 3. print "Hello 22!" with the number in a variable
# name = 22
# name = ("22!") #made it a string to avoid the error message
# # print("Hello", name,"!")	# with a comma
# print("Hello " + name +"!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print("I love to eat", fave_food1, "and", fave_food2) # with .format()
# fave_food1 = "sushi"
# fave_food2 = "pizza"

# print("I love to eat {} and {}.".format(fave_food1, fave_food2))
# # with an f string

# my_fave_food1 = "sushi"
# my_fave_food2 = "filet mignon"
# print("I love to eat", my_fave_food1, "and", my_fave_food2)

# my_fave_food1 = "sushi"
# my_fave_food2 = "filet mignon"
# print("I love to eat " + my_fave_food1 + " " + "and " + my_fave_food2)

#Bonus
firstName = "Basha"
lastName = "Taylor"
state = "CT"
print("My name is %s %s and I'm from %s." % (firstName, lastName, state))