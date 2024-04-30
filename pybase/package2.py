import sys
sys.path.append("/Users/yeryeongseo/Documents/seoyeryeong")
from mypack.calc.calc_mo import calcsum
print("1부터 80까지의 합 = ", calcsum(80))
from mypack.report.human_mo import Human
park = Human("박철순", 56)
park.intro()