# The goal of this challenge is to find the intersection between two sorted strings of numbers.
"""
Have the function FindIntersection(strArr) read the array of strings
stored in strArr which will contain 2 elements: the first element will
represent a list of comma-separated numbers sorted in ascending order,
the second element will represent a second list of comma-separated numbers (also sorted).
Your goal is to return a comma-separated string containing the numbers
that occur in elements of strArr in sorted order. If there is no intersection,
return the string false.

For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] the output
should return "1,4,13" because those numbers appear in both strings.
The array given will not be empty, and each string inside the array will be
of numbers sorted in ascending order and may contain negative numbers.
"""

def FindIntersection(strArr):

  str_1 = strArr[0].split(', ')
  str_2 = strArr[1].split(', ')
  ans = list()
  l1 = len(str_1)
  l2 = len(str_2)
  for i in range(l1):
    for j in range(l2):
      if str_1[i] == str_2[j]:
        ans.append(str_1[i])
  ans = ','.join(ans)
  return ans

# keep this function call here
print(FindIntersection(input()))
