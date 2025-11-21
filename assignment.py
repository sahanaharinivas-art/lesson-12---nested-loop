num = float(inputI"enter a decimal number:"))
binary = ""

if num ==0:
    binary = "0"
else:
    n = num
    while n > 0:
        remainder = n % 2
        binary = str(reminder) + binary
        n = n // 2

print("binary number:", binary)