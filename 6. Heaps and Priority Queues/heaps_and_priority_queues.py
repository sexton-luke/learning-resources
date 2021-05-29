from reference_classes.references_priority_base_queues import HeapPriorityQueue

# Question 1
print("1. Suppose we have a list [5, 6, 3, 1, 2, 7, 9, 8]. Show the list at each stage when using:\n")


# Question 1a
def insertion_sort(array):
    """Sort list of comparable elements into ascending order."""
    for index in range(1, len(array)):
        print(">>> STARTING ITERATION", index)
        current = array[index]
        previous_index = index - 1
        print(">>> Current value =", current)
        print(">>> Previous value =", array[previous_index])
        while previous_index >= 0 and current < array[previous_index]:
            print(">>>", current, "is less than", array[previous_index])
            array[previous_index + 1] = array[previous_index]
            print(">>> Inserting value", array[previous_index], "to index", previous_index + 1)
            print(">>>", array)
            previous_index -= 1
        print(">>> Inserting current value:", current, "to index", previous_index + 1)
        array[previous_index + 1] = current
        print(">>>", array)
    return array


print(">>> 1a --> INSERTION SORT:")
test_array = [5, 6, 3, 1, 2, 7, 9, 0, 8]
insertion_sort(test_array)
print("Final result using Insertion Sort:", test_array)


# Question 1b
def selection_sort(array):
    for i in range(len(array)):
        print(">>> STARTING ITERATION", i)
        print(">>> Pre-swap array:", array)
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        print('>>> Swapping:', array[i], 'and', array[min_index])
        array[i], array[min_index] = array[min_index], array[i]
        print(">>> Post-swap array:", array)
        print("")


print("\n>>> 1b --> SELECTION SORT::")
test_array = [5, 6, 3, 1, 2, 7, 9, 0, 8]
selection_sort(test_array)
print("Final result using Selection Sort:", test_array)

# Question 2
print("\n2. Show the state of an initially empty heap at each point as the following keys are added: 5, 1, 4, 7, 3, 9, "
      "0, 2, 8.")

heap = HeapPriorityQueue()
print(heap.data)

heap.add(5, 0)
print(heap.data)

heap.add(1, 0)
print(heap.data)

heap.add(4, 0)
print(heap.data)

heap.add(7, 0)
print(heap.data)

heap.add(3, 0)
print(heap.data)

heap.add(9, 0)
print(heap.data)

heap.add(0, 0)
print(heap.data)

heap.add(2, 0)
print(heap.data)

heap.add(8, 0)
print(heap.data)
