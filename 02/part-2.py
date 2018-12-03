box_ids = []

with open("./02/input.txt") as input:
  for line in input:
    box_ids.append(line)

def solution(box_ids):
  sub_strings = {}

  for box_id in box_ids:
    # create all possible substrings
    # by removing each character one at a time
    for i, char in enumerate(box_id):
      substring = box_id[:i] + box_id[(i + 1):]

      if (substring in sub_strings):
        # append box_id to the list if it is not already there
        if (box_id not in sub_strings[substring]):
          sub_strings[substring].append(box_id)
      else:
        sub_strings[substring] = [box_id] # store a list of containing ids

  # problem asks for the characters that are common between matching ids
  # so, return the key (substring) with more than one containing id
  for key in sub_strings:
    if len(sub_strings[key]) > 1:
      return key

print(solution(box_ids))
