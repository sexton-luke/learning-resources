# Question 1
import math

print("1. Suppose S is a list of n bits, that is, n 0s and 1s. How long will it take to sort S with the merge-sort "
      "algorithm? What about quick-sort?")
print(">>> Merge-Sort Time: O(n log n) as it divides the input data creating the height of the tree (lg n) and sorts "
      "the input data by comparing nodes at the lowest depth (n). "
      "\n>>> Quick-Sort Time: O(n log n) is to be expected, however, if the pivot point of 1 is chosen, then the data "
      "set will be divided into two segments in one iteration: "
      "\n\tSegment 1: All elements equal to 1"
      "\n\tSegment 2: All elements Less than 1"
      "\n>>> Therefore, Quick-Sort Time: O(n)")


# Question 2
def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
    end1 = start + inc  # boundary for run 1
    end2 = min(start + 2 * inc, len(src))  # boundary for run 2
    x, y, z = start, start + inc, start  # index into run 1, run 2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1  # increment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1]  # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]  # copy remainder of run 2 to output


def merge_sort(sequence):
    """Sort the elements of sequence using the merge-sort algorithm."""
    n = len(sequence)
    log_n = math.ceil(math.log(n, 2))
    src, destination = sequence, [None] * n  # make temporary storage for destination
    for i in (2 ** k for k in range(log_n)):  # pass i creates all runs of length 2i
        for j in range(0, n, 2 * i):  # each pass merges two length i runs
            merge(src, destination, j, i)
        src, destination = destination, src  # reverse roles of lists
    if sequence is not src:
        sequence[0:n] = src[0:n]  # additional copy to get results to S


def remove_duplicates(S):
    seen = set()
    seen_add = seen.add
    return [x for x in S if not (x in seen or seen_add(x))]


print("\n2. Suppose we are given two n-element sorted sequences A and B that may contain duplicate entries. Describe "
      "an O(n)-time method for computing a sequence representing all elements in A or B with no duplicates.")

# Create Initial Sequences
sequence_one = [4, 2, 3, 1, 5]
sequence_two = [9, 8, 7, 6, 5]

# Sort each Sequence
merge_sort(sequence_one)
merge_sort(sequence_two)
print(">>> Sequence one:\t\t\t\t\t\t\t", sequence_one)
print(">>> Sequence two:\t\t\t\t\t\t\t", sequence_two)

# Add sequence one to sequence 2
sequence_one.extend(sequence_two)
sequence_three = sequence_one
print(">>> Sequence three:\t\t\t\t\t\t\t", sequence_three)

# Create new list with no duplicates
sequence_three_remove_duplicates = remove_duplicates(sequence_three)
print(">>> Removing duplicates from sequence three:", sequence_three_remove_duplicates)

# Question 3
print("\n3. Given an array A of n entries with keys equal to 0 or 1, describe an in-place method for ordering A so "
      "that all 0s are before every 1.")


def inplace_quick_sort(sequence, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    print(">>>", sequence)  # Show the stage of the list
    if a >= b:
        return  # range is sorted
    pivot = sequence[b]  # last element of range is pivot
    left = a  # will scan rightward
    right = b - 1  # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and sequence[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < sequence[right]:
            right -= 1
        if left <= right:  # scans did not strictly cross
            sequence[left], sequence[right] = sequence[right], sequence[left]  # swap values
            left, right = left + 1, right - 1  # shrink range

    # put pivot into its final place (currently marked by left index)
    sequence[left], sequence[b] = sequence[b], sequence[left]
    # make recursive calls
    inplace_quick_sort(sequence, a, left - 1)
    inplace_quick_sort(sequence, left + 1, b)


array = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
inplace_quick_sort(array, 0, 9)

# Question 4
print("\n4. Suppose we are given an n-element sequence S such that each element in S represents a different vote for "
      "president, where each vote is given as an integer representing a particular candidate. Design an O(n lg "
      "n)-time algorithm to see who wins the election S represents, assuming the candidate with the most vote wins - "
      "even if there are O(n) candidates")
candidates = {1: 'Justin', 2: 'Linda', 3: 'Paul', 4: 'Melissa', 5: 'Danny'}
votes = [1, 2, 1, 3, 4, 5, 4, 2, 3, 1, 2, 2, 5, 4, 5, 5, 5, 5]
# Justin: 3 votes, Linda: 4 votes, Paul: 2 votes, Melissa: 3 votes, Danny: 6 votes

# Use Merge Sort Algorithm (Running Time: O(n lg n))
merge_sort(votes)
print(">>> Votes:", votes)

# Determine Winner (Running Time: O(n)
vote_count = 0
winner = 0
for vote in votes:
    current_vote_count = votes.count(vote)
    current_winner = vote
    if current_vote_count > vote_count:
        vote_count = current_vote_count
        winner = current_winner
print('>>> The winner is:', candidates.get(winner), 'with', vote_count, 'votes.')

# Question 5
print("\n5. Consider the voting problem from above, but now suppose the number of candidates are a smallconstant "
      "number. Describe an O(n)-time algorithm for determining who wins the election.")


def bucket_sort(values):
    largest = max(values)
    length = len(values)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(values[i] / size)
        if j != length:
            buckets[j].append(values[i])
        else:
            buckets[length - 1].append(values[i])

    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


def insertion_sort(values):
    for i in range(1, len(values)):
        temp = values[i]
        j = i - 1
        while j >= 0 and temp < values[j]:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = temp


candidates = {1: 'Danny', 2: 'Linda', 3: 'Paul', 4: 'Melissa', 5: 'Justin'}
votes = [1, 2, 1, 3, 4, 5, 4, 2, 3, 1, 2, 2, 5, 4, 4, 4, 4, 4]
# Justin: 2 votes, Linda: 4 votes, Paul: 2 votes, Melissa: 7 votes, Danny: 3 votes

print(">>> Votes:", votes)
# Use Bucket Sort
votes = bucket_sort(votes)
print(">>> Votes after bucket sort:", votes)

# Determine Winner (Running Time: O(n)
vote_count = 0
winner = 0
for vote in votes:
    current_vote_count = votes.count(vote)
    current_winner = vote
    if current_vote_count > vote_count:
        vote_count = current_vote_count
        winner = current_winner
print('The winner is:', candidates.get(winner), 'with', vote_count, 'votes.')


# Question 6
print("\n6. Demonstrate merge-sort on the numbers [1000, 80, 10, 50, 70, 60, 90, 20].")
numbers = [1000, 80, 10, 50, 70, 60, 90, 20]

print(">>> Numbers before merge sort:", numbers)
merge_sort(numbers)
print(">>> Numbers after merge sort:", numbers)
