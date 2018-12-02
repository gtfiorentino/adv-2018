box_ids = []
count_of_twos = 0
count_of_threes = 0

with open("./02/input.txt") as input:
  for line in input:
    box_ids.append(line)

# inner loop to check each id for matching letters
def check_id(box_id):
  global count_of_twos
  global count_of_threes
  chars = list(box_id)
  charCount = {}

  for char in chars:
    if char in charCount:
      charCount[char] = charCount[char] + 1
    else:
      charCount[char] = 1

  if 2 in charCount.values():
    count_of_twos = count_of_twos + 1

  if 3 in charCount.values():
    count_of_threes = count_of_threes + 1

# go through each ID and run check on ID
for box_id in box_ids:
  check_id(box_id)

print(count_of_twos * count_of_threes)