num = input("enter a number:")

n = len(num)

if n % 2 == 0:
    mid1 = int(num[n//2-1])
    mid2 = int(num[n//2])
    product = mid1 * mid2
    print(f"middle digits are{mid1} and {mid2}")
    print("product =", product)

else:
    mid = int(num[n//2])
    print(f"middle digits are {mid1}")
    print("product =", mid)
            