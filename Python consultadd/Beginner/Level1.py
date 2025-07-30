#12 Write a Python program to reverse a number using a while loop.
num = 12345
revnu = 0
while num>0:
    digit = num%10
    revnu = revnu *10 + digit
    num = num//10
    
print(revnu)

    



#11 Write a Python program to calculate the sum of digits of a given number until the sum
# becomes a single-digit number
num = 987

def sumdigit(n):
    while n>= 10:
        temp = 0
        while n>0:
            temp += n % 10
            n = n//10
        n = temp
    return n
print("Sum of digit: ",sumdigit(num))

final = sumdigit(num)
#10 Write a Python program to reverse the order of words in a given sentence

Input_sentence = "Hello, World! Welcome to Python programming"
words = Input_sentence.split()

#iterating from last to first index
reverse_words = words[::-1]

reversesentence = ' '.join(reverse_words)
print("Reverse words: ", reversesentence)




#9. Write a Python program to count the frequency of each element in a list.
import collections
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
print(collections.Counter(Input_list))

#another logic without using collections,
#used hashmap
freq={} 
for x in Input_list:
    if x in freq:
        freq[x] +=1
    else:
        freq[x] = 1
print(f"Using hashmap to find the frequency: {freq}")

#8 Write a Python program to calculate the LCM (Least Common Multiple) of two numbers
#logic is to get max and then keep diving the given two number with that max number and if 
# reminder is zero, tham ,axnumber if the LCm or keep incrementing the maxnumber by 1 and repeat
num1 =(int(input("Enter the first number")))
num2 =(int(input("Enter the second number"))) 

maxnum= max(num1, num2)
while True:
    if maxnum % num1 == 0 and maxnum % num2 == 0:
        print(f"LCM: {maxnum}")
        break
    maxnum+=1

#7 Write a Python program to check if a string is an anagram of another string
import collections
string1 =((input("Enter the first string")))
string2 =((input("Enter the second string")))

if collections.Counter(string1) == collections.Counter(string2):
    print(True)
else:
    print(False)

#6 Write a Python program to check if a given number is a perfect number. 
no =(int(input("Enter the number to check for perfect no")))
divNo = []
#first to find the divisors
for i in range(1,no):
    if no% i == 0:
        divNo.append(i)
#print(divNo)
#print(sum(divNo))
if sum(divNo) == no:
    print("Yes")
else:
    print("No")

#5 Write a Python program to find the factorial of a number using a for loop
no =(int(input("Enter the number")))
factorial = 1
while no>0:
    factorial = factorial * no
    no -=1

print(f"Factorial is: {factorial}")

#4Write a Python program to find the sum of all odd numbers
#between two given numbers.
start =(int(input("Enter the start")))
end =(int(input("Enter the end")))
sumvalue = 0
for i in range(start, end+1):
    if i % 2 != 0:
        sumvalue += i
print("Sum: "+sumvalue)

#31
physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))

#totatl marks calcaulated 
total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Display the result
print(f"Percentage: {percentage }%")
print(f"Grade: {grade}")

#2 Write a program that accepts a string as input from the user and calculates the number of digits and letters.
inputStr =(input("Enter the input"))
digit, letter = 0,0
for c in inputStr:
    if c.isdigit():
        digit += 1
    elif c.isalpha():
        letter += 1

print(f"Alpha count: {letter} and digit count: {digit}")
    

#1
a=int(input("Enter the number  "))

if a % 3 ==0 and a % 5 ==0:
    print('Consultadd - Python Training')
elif a % 3 ==0:
    print('Consulteadd')
elif a% 5 == 0:
    print('Python Training')
else:
    print('Nothing')
    