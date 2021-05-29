# Question 1
def find_maximum_element(sequence, sequence_length):
    # Base case: If sequence only contains one element, return the element
    if sequence_length == 1:
        return sequence[0]
    else:
        previous_value = find_maximum_element(sequence, sequence_length - 1)
        current_value = sequence[sequence_length - 1]
        print(">>> Comparing", previous_value, "and", current_value)
        if previous_value > current_value:
            print(">>> Returning", previous_value)
            return previous_value
        else:
            print(">>> Returning", current_value)
            return current_value


print("1. (R-4.1) Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements. "
      "What is your running time and space usage?")
numbers = [1, 3, 5, 7, 9]
print("\n>>> Maximum element =", find_maximum_element(numbers, len(numbers)))

# Question 2
print("\n2. (R-4.2) Draw the recursion trace for the computation of power(2,5), using the traditional function "
      "implemented below:")
print("Recursion trace:"
      "\npower(2, 5) = return 2 x 2 x 2 x 2 x 2 = 32"
      "\npower(2, 4) = return 2 x 2 x 2 x 2 = 16"
      "\npower(2, 3)= return 2 x 2 x 2 = 8"
      "\npower(2, 2) = return 2 x 2 = 4"
      "\npower(2, 1) = return 2 x 1 = 2"
      "\npower(2, 0) = return 1")

# Question 3
print(
    "\n3. (R-4.3) Draw the recursion trace for the computation of power(2,18), using the repeated squaring algorithm, "
    "as implemented below:")
print("Recursion trace:"
      "\npower(2, 18) = return 512 * 512 = 262144"
      "\npower(2, 9) = return 16 * 16 (because 9 % 2 = 1) = 512"
      "\npower(2, 4) = return 4 * 4 = 16"
      "\npower(2, 2) = return 2 * 2 = 4"
      "\npower(2, 1) = return 1 * 1 (because 1 % 2 = 1) = 1"
      "\npower(2, 0) = return 1")


# Question 4
def product(m, n):
    if n == 1:
        return m
    else:
        return m + product(m, n - 1)


print(
    "\n4. Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and "
    "subtraction.")
print(product(2, 3))
