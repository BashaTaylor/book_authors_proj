# 1. Basic - Print all integers from 0 to 150.
for i in range(1, 151, 1):
    print(i)
    
    
# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for num in range(5, 1000, 1):
    if num % 5 == 0:
        print(num)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1, 100, 1):
    if num % 5 == 0:
        print("Coding")
    else:
        print(num)

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

minNum = 0
maxNum =500000
Oddtotal = 0

for number in range(0, 500000+1):
    if number in range(minNum, maxNum+1):
        if(number % 2 != 0):
            print("{0}".format(number))
            Oddtotal = Oddtotal + number
            
print(number,Oddtotal)

# Output is: all odd numbers from 1 - 500,000 and the total of odd's 62500000000

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for num in range(2018,1,-1):
    if num % 4 == 0:
        print(num)


#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 300
mult = 3
for num in range (2,300,1):
    if num % 3 == 0:
        print(num)

