#litrals is a raw data given in a varriable.
"""
numeric
string
boolean
special
"""
#numeric
a=0b010101#binary
b=100 #decimal
c=0o310 #octal
d=0xcde12#hexa

#float
f1=10.5
f2=1.5e2
f3=1.5e-3

#complex
x=5+3.14j

print(a,b,c)
print(f1,f2,f3)
print(x,x.imag,x.real)

#strins 
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#boolean
a = True + 4   # True == 1
b = False + 10 # False == 0

print("a:", a)
print("b:", b)

#special
a = None
print(a)