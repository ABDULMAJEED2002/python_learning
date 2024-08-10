#functions:
"""create a sum function() so it can takes 2 arguments to do do sum"""
"""def sum(a,b):
    print(a + b)


a = int(input("enter your number"))
b = int(input("enter your number"))
sum(a,b)"""

#write a python function to sum all the number in a list
#sample list: [8,2,3,0,7]
"""def sum(number):
    total = 0
    for x in (number):
        total = total + x
        print(total)
number =[1,2,3,4,]
sum(number)"""



#write a function to multiply all the elements in a collection
#write a python function to print even number from a given list
#sample list :- [1,2,3,,4,5,6,7,8,9,]
#expected :- [2,4,6,8]
# def sum(number):
#     total = 0
#     for x in (number):
#         total = total * x
#         print(total)
# number =[1,2,3,4,]
# sum(number)

# def sum(number):
#     total = 0
#     for x in (number):
#         print("even number")
# number(1,2,3,4,5,6,7,8,9)
# sum(number)

def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num % 2, end="")
dectobin(11)
#Return():-
# def dectobin(num):
#     if num>1:
#         dectobin(num//2)
#     return(num % 2, end="")
# print(dectobin(11))
# """sum = 10
# def f1(x):
#     return x + sum
# print(f1(5))"""
""""Return :-is a special keybord that you can use inside a function or method to send the function results back to the caller."""
"""def f(x):
    print(x)
f1(10)"""
1.usage
1.usage new
def f2(x):
    return x
print(f2(10))
#what is the purpose of return?
"""when your return the  value you can decide what gonna do with value """
x = len(input("enter your string"))
print( x**2 )
 def f1(x):
     print(x)
def f1(x):
    return(x)
print(f1(10))
 """sum = 10
 def fum_sum(x):
    a = x + sum
    return a
 print(fun_sum(100))"""

 #write a program to print sum of range of numbers.
 #sample input:- 7
 #expected output :- 28
 """num = int(input("enter your number: "))
 sum = 0
 for i in range(0,num+1)
     sum = sum+1
print(sum)"""
  """Num =  int(input("enter your number"))
  sum = sum(range(1,num+1))
print(sum)"""

  #list comprehension:-
  """it offers you a smaller line of  code that you can create a new list from the existing list """
  list_fruits = ["apple","Banana"."pineapple","mango","kiwi"]
  #print the fruits with the letter "A" in it and store it in new list
  def list_of fruits = ["Apple","Banana","pineappple","mango","kiwi"]
  for list_fruits in (x):
      print(x)
list_fruits
 new_list = []
 for i in list_fruits:
     if "A" in i:
         new_list.append(i)
print(new_list)

list_of fruits = ["Apple","Banana","pineappple","mango","kiwi"]
#new_list = [items(i) for items(i) in "collection name"]
new_list = [x for x in list_fruits if "e" in x]
print(new_list)

#print the new list without "banana"

list_of fruits = ["Apple","Banana","pineappple","mango","kiwi"]
#new_list = [items(i) for items(i) in "collection name"]
new_list = [x for x in list_fruits if x ! = "Banana"]
print(new_list)
#create a new list of numbers in the range of 20 the output must be in multiple of 2.
"""number = [x * 2 for x in range (21)]
print(number)"""
#lamda , filter, map
# lamda is an "anonymous function" means this function doesnt have name.
def f1(x):
    return(x)
print(f1(10))
#syntax for lamda():- "lmda arguments:expression"
#so lamda is an anonymous function it can have many arguments and single expression.
#what is expression?
#expression is some kind of statements/calculator/step using that values to give single
#lamda is an anonymous function how can you call it.
#we are generally use this function where it has some name.
#means we can create a variable to call this function.
"""x = lambda a: a+10
#where your calling the lambda function use the variable name
print(x(5))"""
"""x = lambda a,b,c : a + b + c
print(x(5,6,7))"""
#when we can use lambda function.
#create function tha you can give square of every number?
"""def square(X):
    return X ** 2
def cube(X):
    return X ** 3
def four(X):
    return X** 4"""





def power (n):
    return lambda a: a**n
square = power(2)
cube = power(3)
print(square(6))
print(cube(3))
#similarary try the lambda function for the multiplication.
#Gloabal and Local variable?
#what is global variable?
#global variable is variable that we can create outside the function
x = "amazing"
print(x)
def f():
    return x
print(f())
#what is local variable?
#creating the function variable inside the function is known as local variable.
#local variable is the tempporaray variable ot only losts inside the function
"""def f():
    x = "fantastic"
    return x
print(f())
print(x)"""
""":- even the variables names are same the local varaibles never affect the global variable"""
#Map():
#what map does?
#it uses a function on iterables/.
#what is iterable?
#list,tuple,dict,set,array.
#Map wlll take an function and run it over the iterables.
"""function are the 1st class object. which means one function can act as an arguments for another function"""
#syntax :- map=(function,iterable)
a = ["apple","cherry"."banana","pineapple"]
length = []
for in a:
    length.append(len(i))
#do the same thing lc
l = [len(i) for i in a]
print(l)
"""if you want to display the output bs using the map function we need to decide in which oterbables the output has tober"""
a = ["apple","cherry"."banana","pineapple"]
#length = tuple(map(len,a))
#print(length)
def f1(x):
    return "hello" + x
#print(f1("apple"))
#apply the function for each item in the collection .
"""l = list(map(f1,a))
print(l)"""
#when we have to use the map function?
#when we are having multiple user input collection then we can use the
#user = input()
#print(user)
#print(type(user))
#i want to seprate this values

#take a set of numbers being separated with the spaces
user = inout()
print(user)
print(type(user))
#if i want to seprate this number.
#how to convert this string of elements in list to integers?
"""user = imt(input().split())
print(user)
print(type(user))
number = []
for x in user:
    number,append(int(x))
print(number)
print(type(number))"""
""user = input().split()
number = tuple(map(int,input().split()))
print(number)"""
# Note:- before executing the map() we need to decide in what type of collection, do we need
# how can we print the following 10 20 30 40 50 in double that in tuple?
# lambda:- you can have many arguments but single expression
"""number = tuple(map(int,input().split()))
double = tuple(map(lambda a : a * 2, number))
print(double)"""
# map(int,input().split())--> map storing entire thing/data, if we want it to be in a readable

# ====================================================================================================================================================
"""filter()---> collection name(filter(function,iterable))
filter gives out put of the collection if the condition is true"""
age = [18,48,31,24,16,56,35,45,12,14]
"""def adult(x):
    if x >= 18:
        return x
f1 = list(filter(adult,age))
print(f1)"""
f1 = list(filter(lambda a: a>= 18,age))
print(f1)
# how can i give more expression when i am using the conditional statements.
# we shall use logical operator in lambda if we 
f1 = list(filter(lambda a: a >= 18 and a <= 30, age))
print(f1)
# """so filter basically filters your original collection that returns true or false,
# any value that comes out to be true thr original value can be stored as a collection (list, tuple, set) off items."""
# list comprehension, lambda , map, filter along with sending one function as the arguments to another function.
# Regular expression:- is a built in package which is known as "re"
# A RegEx, or regular expression is a  sequence of characters that forms
# import re
# txt = "hello world!"
# search weather world is present or not
# x = re,search("world!",txt)
# print(x)
# regular expression function
# findall()--->returns a list conating all the matches
# search---> return matche object
# split----> return a list
#sub---> replace one or many matches with string

#GENERATORS:-
"""A generators is a function that returns an iterator that produce a sequence of values when iterator is over."""
# when we have to use those generators?
"""generators are use when we want to produce large sequence of values,we don't want to store all of them in the memory at once"""
#use "def", instead of "return" use "yield"
def my_generator(n):
    value = 0
    #loop untile counter is less than n
    while value < n:
        yield value
        value += 1 # value +1

    for value in my_generator(3):
        print(value)

"""Note:- when ure using the integer directly in to for loop it through's an error
 use itwith range function when ure using generators the instead return se yield it 
 support int object in for loop  """

# pickling:-
# The processing of converting any type of object in python for example (list,tuple,set--etc) on to nytes is known as "serialisation", "deserialisation
"""when it c0mes to python these pickling coversion is kown as "serialisation"", "deserialsation"."""

#what is bytes?
#0's and 1's is known as bytes
#to do the pickling use package called "pickle"
import pickle
#conversation of 2D data format to 1D data and store it
#and in same time conversation of 1D data in to 2D is known as pickle

import pickle
#open a pickle file.text
pickle_file = open("pickle2.txt","wb") #eb is known as work and bytes
#use pickle.dump to dump the file
my_dict = {'1'""a","2":"b"}
pickle,dump(my_dict,pickle_file)
#pickle.dump(collection_name,pickle_file name(where you want to store the data
pickle_file = open("pickle2.txt","r")
#load the data that you have stored
new_dict = pickle.load(pickle.file)
print(new_dict)

#step1:- import the pickle from library
#step2:- creating a pickle file in "wb"
#srep:- use "pickle.dump" to convert the data.
#step4:- read the actual data by using "open(pickle filename", "rb")
#step5:- after that load the load into gguyiuuiuhkjhvfdhvdfgjkdgvkntnfd,msnjs,======================================================================================================================
===========================================================c=======================================07-08-2024
#python pip:- is basically a package manager for python package or modules
#what is package?
# package is basically something that contains all files you needs
#so packages conatins all the files you need for the certain modules.
#what is module?t
#modules are code library which you can include om your project
#Numpy
#pandas
#matplotlib and seaborn
#pendulam
#python image processing
#movie py
#tkinter
#pyqt
#py32
#py test
#how to install this packages?
#what is global package and what is local package?
"""py -m pip install "package name" when you use CMD"""
"""!pip install "package name" ---> colab notebook and juypter notebook"""

# what is global pacakge and local package?
import camelcase()
x = camelcase.camelcase()
a = "hi there! this is the message to check each word of letters are comfort"
print(x.hump(a))
#how to unistall package from CMD?
#py -m unistall "package name"
#how to check what are all packages present in your system?
#py -m pip list
#how to upgrade your pip
#py -m pip install  --upgrade pip
#how to check the version of yur pip
#py -m pip --version
#pip = python install package


# jave script object notations
#it is basically  a syntax that storing and exchanging the data.(it is used in web servers)
# """{first_name":shaul,
#       "last_name":"sk",
#       address : {street:3rd bsnl office,
#                  "city":}"""
# import json
# #what is parse?
# """it is a method where one string of data is coverting into another form of data """
# person = {'name':"andrew"}
#           "language":['english','french']}
# #convert this is to json format
# person_dict = json.dumpa(person)
# print(person_dict)
# print(type(person_dict))

#lets open json file by using "with open"
with open(loc) as f:
    data = json.load(f)
print(data)
print(type(data))

#data structures:
#linkes list
#hash map
#tress
#arrays