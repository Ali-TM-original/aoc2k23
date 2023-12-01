import re
from Loader import LoadInputs

lines = LoadInputs("../inputs/day1")
Sanitized = lines.split("\n")  # List of all the input line wise


def PartA(inp: str) -> int:
    sum = 0
    for element in inp:
        Stack = []
        for char in element:
            if char.isdecimal():
                Stack.append(char)
        sum += int(Stack[0] + Stack[-1])

    return sum


# IMO regular expressions are the best way of solving this
def PartB(inp: str) -> int:
    sum = 0
    hashed = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "twone": "21",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    for line in inp:
        stringNums = re.findall(pattern, line)
        proper = [hashed.get(i) if hashed.get(i) is not None else i for i in stringNums]
        sum += int(proper[0] + proper[-1])
    return sum


print(PartB(Sanitized))
