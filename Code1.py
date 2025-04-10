



# ls = ['laHOre','kaRAchi','mulTan','bahaWALpur','pisHAwar']
# ls1 = []
# for x in ls:
#     x = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     ls1.insert(0,x)
# ls = ls1
# del ls1
# print(ls)

#ls[0::2] = ["Sahiwal","bahalwapur"]
#s = s[0:1].upper() + s[1:-1] + s[-1:].upper()

#ls = [x for x in range(10)]

# while x < len(ls):
#     print(ls[x])
#     x = x+1

#list Comprihension
#ls2 = [x for x in ls if 'a' in x] 
#ls2 = [x.capitalize() for x in ls]
#ls2 = [x[0].upper() + x[1:] for x in ls]


# TUPLE
# tup = ("hello",)
# tp = tuple(("hello",))
# ls = list((tp))
# ls.append("guru99")
# print(ls)
# tup = tuple((ls))
# print(tup)


# print(tup[1])
# print(tup[0:-1])

# tup1 = ("tup 1",)
# tup2 = ("tup 2",)

# tup3 = tup1 + tup2
# print(tup3)

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# print(tup3[7:]+ tup3[:7])
# ls = list(tup3)
# ls2 =[]
# for i in  ls:
#     ls2.insert(0, i)
# tup4 = tuple(ls2)
# print(tup4)
# print(ls)

# tup = ("faisalabad","Jaranwala","Lahore")
# (tup1,tup2,*tup3) = tup
# print(tup3)

# SETS
# st = {"Mavia","Hamza","Huzaifa"}
# st2 = set((7,4,8,10)) 
# st2.add(20)
# st3 = set((0,1,True,False))
# st.update(st2)
# st.update(st3)
# #st4 = st.difference(st2)
# st4 = st | st2 #st4 = st.union(st2)
# st4 = st & st2 #st4 = st.intersection(st2)
# print(st)

# Tuple Practic 1
# st = {"item1","item2"}
# (it1,it2) = st
# it1 = "item3"
# it2 = "item4"
# ls = []
# ls.append(it1)
# ls.append(it2)
# tp = tuple(ls)
# print(tp)

# Tuple Practic 2
# ls = ["Mavia",'Hamza','Saad']
# tp = ('Hamza','Nisar','Shaan')
# st1 = set(ls)
# st2 = set(tp)
# st3 = st1 | st2 # ls + tp and st1 union st2
# print("Union is " , st3)
# st4 = st1 & st2 # st1 intersection st2
# print("Intersection is " , st4)
# st4 = st1.difference(st2) # st1 - st2
# print("Difference is " , st4)

# Tuple Practic 3
# tp = tuple((1,2,3,4,5,6,7,8,9,10))
# (v1,v2,v3,v4,v5,v6,v7,v8,*v9) = tp
# v9.append(11)
# st = set(v9)
# print(st)

# DICTIONARY
# dic = {"name": "Mavia" , "Age": 25, "Height": 5.7}
# dic = dict({"Name": "Mavia" , "Age": 25, "Height": 5.7})
# dic["Address"] = "XYZ"
# dic.update({"Address" : "xyz","Alpha" : 1.99})
# dic.pop("Address")
# dic.popitem()
# print(dic.items())
# print(dic.keys())
# print(dic.values())

# Pass  by value & Pass by refrence
# Non-Premitive data types(list,tuple,set,dictionaries) and Premitive data type

# Dic Practic 1
# dic = {"st1":{"Name":"Mavia","Age":25},"st2":{"Name":"Hamza","Age":21},"st3":{"Name":"Saad","Age":23}}
# dic.update({"st3":{"Name":"Saad","Age":24}})
# dic.update({"st4":{"Name":"Shaan","Age":30}})
# #print(dic.values())
# del dic["st3"]["Age"]
# for x in dic:
#     print(dic[x].values())

#kivi android apps
#tkinter5

# REGULAR FUNCTIONS
# def fun(**krgs): # Arbitorary Keywords Arrguments
#     print(krgs["name"] + " " + str(krgs["age"]))
# fun(name = "Mavia" , age = 25)

# def fun1(*krgs): # Arbitorary Arrguments
#     print(krgs[0] + " " + str(krgs[1]))
# fun1("Mavia",25)

# def fun():
#     pass
# fun()

# ANONYMOUS FUNCTIONS
# x = lambda a,b:a**b
# print(x(5,2))

# EXCEPTION HANDELING
# x = 3
# try:
#     print(y)
# except:
#     print("Error : Variale is not defined. Line 152")
# finally:
#     print("This is always executed. It means try or except is executed")

# Function Practic 1
# def fun(city):
#     ls = ["Lahore","Sadiqabad","Multan","Karachi","Pishawar","Is Clean"]
#     print([x for x in ls if city in x] + ls[-1:])    
# fun(input("Enter Any City : "))

# Function Practic 2

# def fun(num):
#     flag = False
#     if (num <= 500 and num >= 50):
#         flag = True
#     print(flag)
#     print(50+70-20*2/5)
# fun(50+70-20*2/5)

# Split method
# st = "Hello my name is Mavia"
# st = print(st.split("a"))

# string formating
# def sum(a,*b):
#     print(f"hello world {a} : {b[0]} : {b[1]}")
#     print(type(b))
# sum(10,20,'Mavia')

# Class
# class sum:
#     def setter(this,value1,value2):
#         this.value1 = value1
#         this.value2 = value2
#     def getter(this):
#         print(f"Value 1 is {this.value1} and value 2 is {this.value2}")
#     def findSum(this):
#         print("Sum is : " , this.value1 + this.value2)
# s = sum()
# s.setter(5,5)
# s.getter()
# s.findSum()

class Employee:
    def __init__(this,Name,Age):
        this.Name = Name
        this.Age = Age
    def setter(this,Name,Age):
        this.Name = Name
        this.Age = Age
    def getter(this):
        print(f"{this.Name} : {this.Age}")


e = Employee('Ameer Mavia','25')
e1 = Employee('Shayaan','24')
e2 = Employee('Ahmed','23')
e3 = Employee('Gufraan','22')
e4 = Employee('Raza','21')

e.getter()
e1.getter()
e2.getter()
e3.getter()
e4.getter()

# class sum:
#     def setter(this,*values):
#         this.value1 = values[0]
#         this.value2 = values[1]
#     def getter(this):
#         print(f"Value 1 is {this.value1} and value 2 is {this.value2}")
#     def findSum(this):
#         print("Sum is : {this.value1 + this.value2}")
# s = sum()
# s.setter(5,10)
# s.getter()
# s.findSum()