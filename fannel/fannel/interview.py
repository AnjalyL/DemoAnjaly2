'''for i in range(1,4):
    print(i)
else:
    print("No Break")


example = "snow world"
print("%s" % example[4:7])
print(max("what are you"))

list = ["a","b","c"]
list += "de"
print(list)


a=1
def func(a):
    return a**2
a = func(a)**2
print(func(a))



i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")


i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")


List = ['He', 'Loves', 'To', 'Code', 'In', 'Python']
shuffle(List)
print(List)

x, y = 10, 20
count = x if x < y else y
print(count)

age=20
def fun():
    global age
    age=age+1
    print(age)
fun()
'''

global age
age=20
def fun():
    age=20
    age=age+1
    print(age)
def fun1():
    age=20
    age = age + 5
    print(age)
fun()
fun1()
print(age)





