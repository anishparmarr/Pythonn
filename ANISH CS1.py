Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> a=10
>>> print(a)
10
>>> a=2.3
>>> print(a)
2.3
>>> a=2.3
>>> print("hello")
hello
>>> type(a)
<class 'float'>
>>> a=2
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> a= input("Enter number : ")
Enter number : 
>>> 23
23
>>> name = input("Enter name")
Enter nameanish
>>> print(a)

>>> print (name)
anish
>>> a,b=input("Enter nos : ")
Enter nos : 2 3
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a,b=input("Enter nos : ")
ValueError: too many values to unpack (expected 2)
>>> a=int(input("Enrer first no :"))
Enrer first no :1
>>> b=int(input("Enter sec:"))
Enter sec:2
>>> c=a+b
>>> print(c)
3
>>> 
