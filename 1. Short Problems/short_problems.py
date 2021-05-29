# Question 1
def is_multiple(n, m):
    return n % m == 0


test = is_multiple(6, 3)
print("1. (R-1.1) Write a short Python function, is_multiple( n, m), that takes two integer values and returns True "
      "if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.")
print(">>> Testing is 6 a multiple of 3:", test)

# Question 2
power = 2
results = [power ** i for i in range(9)]
print("\n2. (R-1.11) Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, "
      "32, 64, 128, 256]")
print(">>> Producing comprehension list for powers of two up to 256:", results)


# Question 3
def is_different(values):
    if len(set(values)) == len(values):
        return True
    else:
        return False


print("\n3. (C-1.15) Write a Python function that takes a sequence of numbers and determines if all the numbers are "
      "different from each other (that is, they are distinct).")
numbers = [1, 2, 3, 4, 5]
print(">>> Testing is_different() with values:", numbers)
if is_different(numbers):
    print(">>> Result: Each number is different! :)")
else:
    print(">>> Result: There are duplicates!")


# Question 4
def harmonic_gen(n):
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
        yield h


print("\n4. The n-th harmonic number is the sum of the reciprocals of the first n natural numbers. For "
      "example, H3= 1 + ½ + ⅓ = 1.833. A simple Python function for creating a list of the first n harmonic "
      "numbers follows:"
      "\n"
      "def harmonic_list(n):"
      "\n\tresult = []"
      "\n\th = 0"
      "\n\tfor i in range(1, n + 1):"
      "\n\t\th += 1 / i"
      "\n\t\tresult.append(h)"
      "\n\t return result"
      "\nConvert this function into a generator harmonic_gen(n) that yields each harmonic number.")
test_value = 3
count = 0
harmonics = harmonic_gen(test_value)
print(">>> Generating harmonic values using the number 3...")
for harmonic in harmonics:
    count += 1
    print(">>> Harmonic", count, ":", harmonic)
