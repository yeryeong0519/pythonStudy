# 방정식 

from fractions import Fraction
import sympy
a = Fraction('2/5')
# print(a)
f = sympy.Eq(x*Fraction('2.5'), 3500)
result = sympy.solve(f)
print("철수가 가진 돈", result)
remain = result[0]-3500
print("남은 돈" ,remain)