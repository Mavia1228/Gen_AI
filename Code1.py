



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


# tup = ("hello",)

# tp = tuple(("hello",))

# ls = list((tp))

# ls.append("guru99")
# print(ls)
# tup = tuple((ls))
# print(tup)




# print(type(tp))


# print(type(tup))
# print(type(tup))
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

# Sets
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

# Tuple Practic 1
# ls = ["Mavia",'Hamza','Saad']
# tp = ('Hamza','Nisar','Shaan')
# st1 = set(ls)
# st2 = set(tp)
# st3 = st1 | st2 # ls + tp and st1 union st2
# #print(type(st3))
# print("Union is " , st3)
# st4 = st1 & st2 # st1 intersection st2
# print("Intersection is " , st4)
# st4 = st1.difference(st2) # st1 - st2
# print("Difference is " , st4)

# Tuple Practic 1
# tp = tuple((1,2,3,4,5,6,7,8,9,10))
# (v1,v2,v3,v4,v5,v6,v7,v8,*v9) = tp
# v9.append(11)
# st = set(v9)
# print(st)

# Dictionary
#dic = {"name": "Mavia" , "Age": 25, "Height": 5.7}
dic = dict({"Name": "Mavia" , "Age": 25, "Height": 5.7})
dic["Address"] = "XYZ"
dic.update({"Address" : "xyz","Alpha" : 1.99})
dic.pop("Address")
dic.popitem()
print(dic)
print(dic.keys())
