from reference_classes.references_linked_lists import SinglyLinkedList, CircularLinkedList, PositionalList

# Question 1
print("1. (R-7.1) Give an algorithm for finding the second-to-last node in a singly linked list in which the last "
      "node is indicated by a next reference of None.")

linked_list = SinglyLinkedList()
print('>>> Initial Singly Linked List', linked_list)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print('>>> Full Singly Linked List', linked_list)
print('>>> Second to last node:', linked_list.second_to_last())

# Question 2
print("\n2. (R-7.5) Implement a function that counts the number of nodes in a circularly linked list.")

circular_list = CircularLinkedList()
circular_list.append(2)
circular_list.append(4)
circular_list.append(6)
circular_list.append(8)
circular_list.append(10)
circular_list.print_list()


# Question 3
def list_to_positional(elements):
    positional_list = PositionalList()
    for element in elements:
        positional_list.add_last(element)
    return positional_list


print("\n3. Using PositionalList write a function list_to_positional_list(L) which takes a "
      "built-in Python list L and creates a new PositionalList containing the same elements in the same order.")

values = [1, 2, 8]
positional_values = list_to_positional(values)
print(">>> Positional list length:", len(positional_values))
for value in positional_values:
    print(">>>", value)


# Question 4
print("\n4. (R-7.11) Implement a function, L.max(), that returns the maximum element from a PositionalList instance "
      "L. Assume all values in L are numbers.")
# def max(self):
#    return max(element for element in self)
print('>>> Maximum:', positional_values.max())
