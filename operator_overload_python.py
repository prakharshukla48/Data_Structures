Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if (self.a > other.a):
			print ('1st is bigger than 2nd')
	def __lt__(self, other):
		if (self.a < other.a):
			print ('2nd is bigger than 1st')
	def __et__(self, other):
		if (self.a == other.b):
			print ('Both are equal')

>>> ob1 = A(5)
>>> ob2 = A(10)
>>> ob1>ob2
>>> ob1<ob2
2nd is bigger than 1st
>>> ob1>ob2
>>> ob1==ob2
False
>>> class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if (self.a > other.a):
			print ('1st is bigger than 2nd')
		else:
			print ('In else block')
	def __lt__(self, other):
		if (self.a < other.a):
			print ('2nd is bigger than 1st')
	def __et__(self, other):
		if (self.a == other.b):
			print ('Both are equal')
		else:
			print ('Not equal')

>>> ob1=A(5)
>>> ob2 = A(10)
>>> ob1>ob2
In else block
>>> ob1<ob2
2nd is bigger than 1st
>>> ob1==ob2
False
>>> class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if (self.a > other.a):
			print ('1st is bigger than 2nd')
		else:
			print ('In else block')
	def __lt__(self, other):
		if (self.a < other.a):
			print ('2nd is bigger than 1st')
	def __eq__(self, other):
		if (self.a == other.b):
			print ('Both are equal')
		else:
			print ('Not equal')

>>> ob1 = A(5)
>>> ob2 = A(10)
>>> ob1==ob2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    ob1==ob2
  File "<pyshell#29>", line 13, in __eq__
    if (self.a == other.b):
AttributeError: 'A' object has no attribute 'b'
>>> class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if (self.a > other.a):
			print ('1st is bigger than 2nd')
		else:
			print ('In else block')
	def __lt__(self, other):
		if (self.a < other.a):
			print ('2nd is bigger than 1st')
	def __et__(self, other):
		if (self.a == other.a):
			print ('Both are equal')
		else:
			print ('Not equal')

>>> ob1==ob2
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    ob1==ob2
  File "<pyshell#29>", line 13, in __eq__
    if (self.a == other.b):
AttributeError: 'A' object has no attribute 'b'
>>> ob1 = A(5)
>>> ob2 = A(10)
>>> ob1==ob2
False
>>> class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if (self.a > other.a):
			print ('1st is bigger than 2nd')
		else:
			print ('In else block')
	def __lt__(self, other):
		if (self.a < other.a):
			print ('2nd is bigger than 1st')
	def __eq__(self, other):
		if (self.a == other.a):
			print ('Both are equal')
		else:
			print ('Not equal')

>>> ob1 = A(5)
>>> ob2 = A(10)
>>> ob1==ob2
Not equal
>>> 
