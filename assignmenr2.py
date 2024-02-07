

# AlgoExpert 1: Two Number Sum
# Difficulty: Easy
# Two Number Sum: Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

# numbers sum up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum. You can assume that there will be at most one pair of numbers summing up to the target sum.
# Sample Input:
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output:
# [-1, 11] // the numbers could be in reverse order

def target_array(my_array, target_sum):
    numbers = set()
    for num in my_array:
        potential_match = target_sum - num
        if potential_match in numbers:
            return [potential_match, num]
        else:
            numbers.add(num) 
    return []  

my_array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10
result = target_array(my_array, target_sum) 
print(result) 



# AlgoExpert 1: Two Number Sum
# Difficulty: Easy
# Two Number Sum: Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum. You can assume that there will be at most one pair of numbers summing up to the target sum.
# Sample Input:
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output:
# [-1, 11] // the numbers could be in reverse order