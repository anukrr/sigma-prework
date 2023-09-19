def minmax(num):
  highest = num[0]
  lowest = num[0]
  for value in num:
    if value > highest:
      highest = value
    elif value < lowest: 
      lowest = value
  return [lowest, highest]

print(minmax([2, 4, 1, 0, 2, -1]))
