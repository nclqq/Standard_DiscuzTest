import os


#点表示上一级，所以abspath('.')表示：E:\DiscuTest
p=os.path.abspath('.')
#E:\DiscuTest\aaa.py
p1=os.path.abspath(__file__)
#E:\DiscuTest
p2=os.path.realpath('.')
#E:\DiscuTest\aaa.py
p3=os.path.realpath(__file__)
#dirname表示上一级，所以下面表示为：E:\
p4=os.path.dirname(os.path.abspath('.'))
# E:\DiscuTest
p5=os.getcwd()

print(p)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
