#10 check for the computer availability and return the cout of customers whoe where not server beacuse of already occupied computers
def check_availability(N, S):
    occupied_ct = 0
    cafe={}
    unserved = 0
    for customer in S:
        if customer not in cafe:
            if occupied_ct< N:
                occupied_ct +=1
                cafe[customer] = True #which say that customer have oppcioed a available computer
            else:
                unserved +=1
                cafe[customer] = False
        else:
            if cafe[customer]== True:
                occupied_ct -= 1
            del cafe[customer]    
    return unserved

    
print(check_availability(3,"GACCBDDBAGEE" ))
#9 return rin legth of encoded sting
inputstring ="wwwwaaadebbbbbw"
def runLength(inputstring):
    encodedstring = ""
    ct = 1 #as I am staring from index 1 so, ct should be 1 by default
    for i in range(1,len(inputstring)):
        if inputstring[i] == inputstring[i-1]:
            ct +=1
        else:
            encodedstring += inputstring[i-1]+str(ct)
            ct =1
    return encodedstring
            
print(runLength(inputstring))

#8 accept the encoded and parse it 
encoded_input = "Robert000Smith000123"

def encoded(encoded_input):
    parts = [data for data in encoded_input.split('0') if data !='']
    return f"First name {parts[0]} | Last Name {parts[1]} | ID {parts[2]}"

print(encoded(encoded_input))

#7 dictionary should map the students with their
# respective subjects. Let’s see how to do this using for loops and
# dictionary comprehension.
names =  ["Sam", "Alice", "Mona"]
subjects =["Commerce", "Science", "Computer"]
maping ={}
for i in range(len(names)):
    maping[names[i]]= subjects[i]

print(f"Mapping of name to subject:{maping}")


#6 Python classes which have methods and attributes and implement single inheritance, multiple inheritance,
# and multilevel inheritance
#single inheritance
class Person:
    def __init__(self, person_name):
        self.name = person_name
    
    def intro(self):
        print(f"{self.name} is a Person")

class Student(Person):
    def study(self):
        print(f"{self.name} is a student")
        
class Intern:
    def job_role(self):
        print(f"{self.name} is an Intern")

#multilevel inheritence as CPTStudent inherit from more then one class
#multiple inheritance as well, as CPTStudent inherit from student class which inherit from Person class
class CPTStudent(Student, Intern):
    def summerIntern(self):
        print(f"{self.name} is a CPT student and summer intern")
    
cpt = CPTStudent("Lee")
cpt.summerIntern()
cpt.study()
cpt.job_role()

cpt.intro()




#5 class Time and display time -> hrs and min , diplay time only in min -> total min
class Time():
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute
    def addTime(self,t):
        total_min = self.minute+ t.minute
        total_hour = self.hour + t.hour + total_min // 60
        remaining_mins = total_min % 60
        return Time(total_hour, remaining_mins)
    
    def displayTime(self):
        print(f"Time: {self.hour} hr and {self.minute} mins")
    
    def displayMins(self):
        totatl_min= self.hour * 60 + self.minute
        print(f"Total mins: {totatl_min} mins")
        

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 =t1.addTime(t2)
t3.displayTime()
t3.displayMins()

#4.Shape parent class, Square is sub class
class Shape():
    def area(self):
        print("Shape area is 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area of square:", self.length* self.length)
s1 = Shape()
print(s1.area())

s2 = Square(10)
print(s2.area())

#3 reada file and cover J to I
with open('words.txt', 'r') as file:
    data = file.read()

new_data = data.replace('J','I')
print(f"Updated data: {new_data}")

#2 program to count the lines in a file
with open("sample.txt","r") as file:
    count =0
    for line in file:
        count += 1
print(f"Lines in file: {count}")


#1 opening and reading file

with open("sample.txt","r") as file:
    data = file.read()

words = data.split()
even_words = [w for w in words if len(w)%2 == 0]

print(f"Even words: {even_words}")
