solution = 0

with open("./01/input.txt") as input:
  for line in input:
    solution = solution + int(line)

print(solution)
