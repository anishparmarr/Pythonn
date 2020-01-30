Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input("Enter the no:"))
Enter the no:3
>>> for i in range(1,11):
	print(n*i)

3
6
9
12
15
18
21
24
27
30
>>> for i in range(1,11):
	print(n, "X", i"=" n*i)
	
SyntaxError: invalid syntax
>>> for i in range(1,11):
	print(n, 'x', i, '=', n*i)

	
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
>>> 
