instructions = []
with open("./01/input.txt") as input:
  for line in input:
    instructions.append(int(line))

def find_frequencies(instructions):
  frequencies = [0]
  solution = 0
  found = False
  
  while not found:
    for instruction in instructions:
      solution = solution + instruction
    
      if solution in frequencies:
        found = True
        return solution

      frequencies.append(solution)

test = [7, 7, -2, -7, -4]
print(find_frequencies(instructions))