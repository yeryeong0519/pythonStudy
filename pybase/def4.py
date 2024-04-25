# def add_many(*nums, ab):
# def add_many(nums, *ab):
def add_many(choie, *nums):
    if choice == "add":
        sum = 0
        for n in nums:
            sum += n
    elif choice == "mul":
        result = 1
        for n in nums:
            result*=n
    
    return result

defresult = add_many("add", 23, 74, 56)
print("합=",defresult)
defresult2 = add_many("mul", 2, 3, 7, 5, 9)
print("곱 = ", defresult2)