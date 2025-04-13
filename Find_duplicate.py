# In the Python file, you are provided with a function named find_duplicate_integer which takes a list
# of integers from 1 to n as its argument. This list contains n + 1 integers, implying one duplicate.

# Your task is to modify the function to return the duplicated integer from the list.
# The starter code has two logical errors that needs to be corrected.

# Example Input
# [1, 3, 4, 2, 2]

# Example Output
# 2


def find_duplicate_integer(integers):
  dic = {}
  for k in integers:
    dic[k] = dic.get(k, 0) +1
  for key, val in dic.items():
    if val != 1:
      return key

# do not modify the values below
print(find_duplicate_integer([1, 3, 4, 2, 2]))
