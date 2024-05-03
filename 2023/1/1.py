input = open('input.txt').read()

sum = 0
for line in input.split("\n"):
    digits = []
    for char in line:
        if char in "0123456789":
            digits.append(char)
    sum += int(f"{digits[0]}{digits[-1]}")
print(sum)