#13 Use of lambda function to check for given string start with a given input character
ipstring= "Hello, World!"
ch ="H"
char_check = lambda ch, ipstring: ch == ipstring[0]
print(aa)
#12 signup page creataion with three attempt for passowerd and retyped passweord to be same
usename = input("Enter username")

attempt = 0
result = False
while attempt<3:
    password = input("Enter password")
    retype_password = input("Retype password")
    if password == retype_password:
        print("Password created successfully")
        result = True
        break
    else:
        print("Password does not match. Please try again")
        attempt += 1
if result:
    print("You are singup")
else:
    print("Too many attempt, cannot signup now, try later")


#11 Write a Python program to create a list of given strings individually of the list using the Python map function
input = ['Red', 'Blue', 'Black', 'White', 'Pink']
result =[]

for word in input:
    result.append(list(word))

print(result)

#10  Have doubt for problem 10 as the example is incorrectly and not folooing the give conditions

#9 Write a Python program that executes an operation on a list and handles an IndexError 
# exception if the index is out of range.
list1 = [1,2,3,4,5,6,7]

try:
    list1[len(list1)]
except IndexError:
    print("IndexError exception- trying to access element out of index range")
    
# 8.Write a Python function that counts the number of vowels in a given string
string = "Hello, World!"
vowels ="aeiou"
ct = 0
for c in string:
    if c in vowels:
      ct +=1
print(f"Number of vowels in given string: {ct}")  

#7 Write a Python function that finds the median of a list of numbers
number_list = [7, 2, 5, 1, 9, 3]
number_list.sort()
num_len = len(number_list)
if num_len%2 != 0:
    print("Median element ",number_list[(num_len//2)])
else:
    sum1 = number_list[(num_len//2)-1]+number_list[(num_len//2)]
    print("Median element ", sum1/2)

# 6. Write a Python program to check if a number is a power of two using recursion\
def check_power_of_two(n):
    #except 1,if number is even number and after divinging by 2 iteratively and doest not comes to 0, then ist power of two
    if n == 1:
        return True
    if n == 0 or n%2 != 0:
        return False
    return check_power_of_two(n//2)

result = check_power_of_two(100)
print("is this give number poswer of 2: ", result)

#5 You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a
# specific location and determines the average temperature, highest
# temperature, and lowest temperature.
temperature_readings = [25, 28, 21, 24, 27]
total,ct= 0,0
highest, lowest =temperature_readings[0], temperature_readings[0]

for t in temperature_readings:
    total +=t
    ct +=1
    if t > highest:
        highest = t
    if t< lowest:
        lowest = t

average = total/ct
print("Average temperature:", average)
print("Highest temperature:", highest)
print("lowest temperature:", lowest)
#4  Given an array of size N. The task is to rotate array by D elements towards right
arr = [1, 2, 3, 4, 5]
D = 2
larr = len(arr)
i=0
D = D%larr #to avoid double calculation
print(arr[-D:]+arr[:-D])


#3  Given an array of N integers and an integer K, find the number of 
# pairs of elements in the array whose sum is equal to K
arr = [1, 2, 3, 4, 5]
resultpair=set()
visit = set()
k=6
for x in arr:
    second = k-x
    if second in visit:
        resultpair.add(tuple((x,second)))
    visit.add(x)  

print(f"Number of pairs {len(resultpair)}")


#2. Create a function that takes a list and returns a new list with 
# unique elements of the first list.
list1 = [1, 2, 2, 3, 4, 4, 5, 5]
print("List: ",list(set(list1)))
result = []
for x in list1:
    if x not in result:
        result.append(x)
print("Without using set(): ",result)
        

# 1. Write a Python program to find the common elements between two lists
L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8]
op= []
#for common elements, I can make one list as dictionary 
dict1 = { x:i for i,x in enumerate(L1)}
print(dict1.keys())
for x in L2:
    if x in dict1:
        op.append(x)
print("common element: ", op)
