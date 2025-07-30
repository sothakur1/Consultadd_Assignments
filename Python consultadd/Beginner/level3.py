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


#opening and reading file

with open("sample.txt","r") as file:
    data = file.read()

words = data.split()
even_words = [w for w in words if len(w)%2 == 0]

print(f"Even words: {even_words}")