#################################################### **Loops in python** ####################################################
# **** While Loop ***

# count = 0
# while (count < 5):   
#     count = count + 1
#     print("Python 3.x")

# **** for Loop ***

# lst = ["I", "Love", "Pakistan"]
# for index in range(len(lst)):
#     print(lst[index])

#################################################### **Continue statement** ####################################################

# for i in 'python': 
#     if i == 'o':
#          continue
#     print ('Current Letter is : ', i)

#################################################### **Break statement** ####################################################

# for i in "python": 
#     if i == 'o':
#          break
#     print ("Current Letter is : ", i)

#################################################### **Pass statement** ####################################################

# for i in "python":
#     pass
# print("ok")

#################################################### **Looping technique** ####################################################
# **** enumerate ***
# for key, value in enumerate(['I', 'Love', 'Pakistan']):
#     print(key, value)

# **** enumerate ***
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'circle']
# for question, answer in zip(questions, answers):
# 	print("What is your {}? I am {}.".format(question, answer))

# **** sorted ***
# lis = [1, 3, 5, 6, 2, 5, 8, 6, 3]
# for i in sorted(lis):
#     print(i, end=" ")

# **** reversed ***
# lis = [1, 3, 5, 6, 2, 5, 8, 6, 3]
# for i in reversed(lis):
#     print(i, end=" ")

#################################################### **Range vs xrange** ####################################################

# for i in range(2,20,3):
#     print(i)

#* xrange use in place of range in python 2.x.

#################################################### **printing pyramid technique** ####################################################
# for i in range(0, 6):
#     for j in range(0, i+1):
#         print("* ",end=" ")
#     print("\r")

#################################################### **Chaining comparison** ####################################################
# a = 12
# b = 10
# c = 5

# if a > b > c:
#     print("a is greatest number")

#################################################### **else with for loop** ####################################################
# **** With break statemet ***
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i, end="_")
# else :
#     print("With break statment")
    

# **** Without break statemet ***
# for i in range(1,10):
#     print(i, end="_")
# else :
#     print("\n")
#     print("Without break statment")

#################################################### **switch function** ####################################################
# def switch(argument):
#     switcher = {
#         0: "zero",
#         1: "one",
#         2: "two",
#         3: "three",
#         4: "four",
#         5: "five"
#     }

#     return switcher.get(argument, "Not Found")

# argument=6
# print("Yor Result is : ",switch(argument))

#################################################### **Using iteration effectively** ####################################################
# **** enumerate ***
# for key, value in enumerate(['I', 'Love', 'Pakistan']):
#     print(key, value)

# **** enumerate ***
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'circle']
# for question, answer in zip(questions, answers):
# 	print("What is your {}? I am {}.".format(question, answer))

# **** sorted ***
# lis = [1, 3, 5, 6, 2, 5, 8, 6, 3]
# for i in sorted(lis):
#     print(i, end=" ")

# **** reversed ***
# lis = [1, 3, 5, 6, 2, 5, 8, 6, 3]
# for i in reversed(lis):
#     print(i, end=" ")



#################################################### **Python Itertools** ####################################################
# **** Infinite iterators ***
# import itertools
# for i in itertools.count(5, 10):
#     if i == 105:
#         break
#     else:
#         print(i, end =" ")


# **** Combinatoric iterators ***
# **** Infinite iterators ***
# from itertools import combinations
# print(list(combinations(range(5), 3)))


# **** Terminating iterators ***
# import itertools
# list_1 = [2, 55, 4, 8, 7]
# list_2 = [3, 5, 8, 7, 26]
# list_3 = [8, 9, 1, 15, 26]
# print (list(itertools.chain(list_1, list_2, list_3)))

#################################################### **iter() and next()** ####################################################
# listA = ["i", "AM", "LEARNING", "PYTHON"]
 
# F_list = iter(listA)
 
# try:
#     print(next(F_list))
#     print(next(F_list))
#     print(next(F_list))
#     print(next(F_list))
#     print(next(F_list))
#     print(next(F_list))
# except:
#     print("                    ***terminated***")


#################################################### **iterable vs iterator** ####################################################
# color = ["red", "black", "blue", "white", "green"]

# var = iter(color)
# print(var)

# print(next(var))
# print(next(var))
# print(next(var))


#################################################### **Generators in python** ####################################################
# def myFun():
#     print('First value')
#     yield 100

#     print('Second value')
#     yield 150

#     print('Last valuse')
#     yield 250

# print(myFun())

# print(next(myFun()))
# print(next(myFun()))
# print(next(myFun()))

#################################################### **Generators expression** ####################################################
# my_list = [1, 3, 6, 10]

# a = (x**2 for x in my_list)             # Generators expression
# print(next(a))

# print(next(a))

# print(next(a))

# print(next(a))

# ##next(a)                   # This will through an error
