ls = ['laHOre','kaRAchi','mulTan','bahaWALpur','pisHAwar']
ls1 = []
for x in ls:
    x = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
    ls1.insert(0,x)
ls = ls1
del ls1
print(ls)



#ls[0::2] = ["Sahiwal","bahalwapur"]
#ls = ['lahore','karachi','multan','bahawalpur','pishawar']
# ls1 = []
# for x in ls:
#     s = ls.pop()
#     s = s[0:1].upper() + s[1:-1] + s[-1:].upper()
#     s = s[0:1] + s[1:2].upper() + s[2:-2] + s[-2:-1].upper() + s[-1:]
#     ls.insert(0,s)
# ls = ls1
# print(ls)