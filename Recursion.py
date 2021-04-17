# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return sum_to_one(n-1) + n

#print(sum_to_one(7))

# Define factorial() below...
def factorial(n):
  if n < 2:
    return 1
  return factorial(n-1) * n

#print(factorial(7))

# Define power_set() below...
def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

# for set in power_set_of_universities:
#   print(set)

# define flatten() below...
def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):
      print("List found!")
      flat_list = flatten(i)
      result += flat_list
    else:
      result.append(i)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

#print(flatten(planets))

# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  return fibonacci(n-2)+fibonacci(n-1)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

# Binary search trees
# Define build_bst() below...
def build_bst(my_list):
  if not my_list:
    return "No Child"
  middle_idx = len(my_list)//2
  middle_value = my_list[middle_idx]
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))
  tree_node = {'data':middle_value}
  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx+1:])
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
