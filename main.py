#Given an unsorted integer array, find the first missing positive integer.

def first_missing_positive_integer(integers):
  Dict = {}
  count = 0
  for x in range (0,len(integers)):
    if integers[x]>0:
      Dict[count]=integers[x]
      count = count + 1
  if len(Dict) == 0:
    return 1
  val = Dict[0]
  for x in range (0, len(Dict)):
    if Dict[x] < val or Dict[x] == val+1:
      val = Dict[x]
    
  return (val+1)