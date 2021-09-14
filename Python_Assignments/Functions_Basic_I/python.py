# 1
# def a():
#     return 5
# print(a())


# 2
# def a():
#     return 5
# print(a()+a())


# #3
# def a():
#     return 5
#     return 10
# print(a())


# #4
# def a():
#     return 5
#     print(10)
# print(a())

# #5
# def a():
#     print(5)
# x = a()
# print(x)


# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))


# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))


# 8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
# 	    return 10
#     return 7
# print(a())


# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))



# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)


# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)



# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)



# #14
# def a():    #1 
#     print(1)  #2, print 1,
#     b()        #3 go to function b
#     print(2)
# def b():        #4  
#     print(3)    #5, print 3, #6, go to function b, print 2
# a()             
#1,3,2


# #15
# def a():
#     print(1)    #1 first print 1
#     x = b()      #2  #5 ->5  
#     print(x)      #6 print 5  
#     return 10      #7 5->10
# def b():          #3  
#     print(3)      #4 second print 3, 3->5 print 5
#     return 5 
# y = a()             #8 10
# print(y)            #9 print 10



