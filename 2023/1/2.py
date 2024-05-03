input = open('input.txt').read()

data = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


sum = 0

for line in input.split("\n"):
    digits = []
    for index, char in enumerate(line):
        for word in data.keys():
            if char == word[0] and line[index:index+len(word)] == word:
                digits.append(data[word])
        try:
            digits.append(int(char))
        except ValueError:
            continue
    sum += int(f"{digits[0]}{digits[-1]}")
print(sum)