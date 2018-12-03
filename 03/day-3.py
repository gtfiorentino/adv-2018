#!/usr/local/bin/python3
import re

# test data
# raw_cuts = [
#   "#1 @ 1,3: 4x4",
#   "#2 @ 3,1: 4x4",
#   "#3 @ 5,5: 2x2"
# ]

all_cuts = {}

raw_cuts = []
with open("./03/input.txt") as input:
  for line in input:
    raw_cuts.append(line)


# use regex to read and structure the input line
def parse_line(line):
  return {
    "id": int(re.search(r"(?<=#).*(?=\s\@)", line).group(0)),
    "left": int(re.search(r"(?<=@\s).*(?=,)", line).group(0)),
    "top": int(re.search(r"(?<=,).*(?=:)", line).group(0)),
    "width": int(re.search(r"(?<=:\s).*(?=x)", line).group(0)),
    "height": int(re.search(r"(?<=x).*", line).group(0))
  }

def parse_lines(raw_cuts):
  cut_defs = []
  for raw_cut in raw_cuts:
    cut_defs.append(parse_line(raw_cut))

  return cut_defs

def set_shape(cut):
  for w in range(cut["left"], cut["left"] + cut["width"]):
    for h in range(cut["top"], cut["top"] + cut["height"]):
      if (w, h) in all_cuts:
        all_cuts[(w, h)].append(cut["id"])
      else:
        all_cuts[(w, h)] = [cut["id"]]

def set_all_shapes(cut_defs):
  for cut in cut_defs:
    set_shape(cut)

def count_overlapping_cuts():
  count = 0

  for key in all_cuts:
    if len(all_cuts[key]) > 1:
      count = count + 1

  return count

def find_overlaps(cut_defs, all_cuts):
  cut_overlaps = {}

  # set each to True by default
  for cut in cut_defs:
    cut_overlaps[cut["id"]] = True

  for key in all_cuts:
    if len(all_cuts[key]) > 1:
      for cut_id in all_cuts[key]:
        cut_overlaps[cut_id] = False

  return cut_overlaps

print("Parsing lines")
cut_defs = parse_lines(raw_cuts)

print("Setting shapes")
set_all_shapes(cut_defs)

print("Counting overlaps")
print("Overlapping cuts:", count_overlapping_cuts())

print("Calculating overlaps")
cut_overlaps = find_overlaps(cut_defs, all_cuts)

print("Finding non-overlapping cuts")
for key in cut_overlaps:
  if cut_overlaps[key]:
    print("Non-overlapping shape:", key)
