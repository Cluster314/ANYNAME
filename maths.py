from fractions import Fraction
pi = 3.141592653589793
e = 2.718281828459045
tau = pi*2
class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius*2
        self.cercumfrence = self.diameter*pi
        self.area = pi*(self.radius**2)
def rad(deg):
    a = str(Fraction(deg, 180))
    b3 = a.index("/")
    b1 = a[:b3]
    b2 = a[b3+1:]
    c = b1+"π/"+b2
    return c
plane = """
       ^
       |
       |
<-------------->
       |
       |
       v
"""
circle = """         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
"""
def nums(s,e):
    return range(s,e+1)
