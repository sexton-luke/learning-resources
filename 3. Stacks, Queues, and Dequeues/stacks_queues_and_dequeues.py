import collections

from reference_classes.array_stack import ArrayStack
from reference_classes.array_queue import ArrayQueue

# Question 1
print("1. (R-6.1) What values are returned during the following series of stack operations, if executed upon an "
      "initially empty stack? push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), "
      "push(7), push(6), pop(), pop(), push(4), pop(), pop().")
stack = ArrayStack()

stack.push(5)
print('>>>', stack.data)

stack.push(3)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

stack.push(2)
print('>>>', stack.data)

stack.push(8)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

stack.push(9)
print('>>>', stack.data)

stack.push(1)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

stack.push(7)
print('>>>', stack.data)

stack.push(6)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

stack.push(4)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)

pop = stack.pop()
print('>>> Return:', pop)
print('>>>', stack.data)


# Question 2
print("\n2. (R-6.2) Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, "
      "and 10 pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current size "
      "of S?")
print(">>> Only 7 pop operations removed elements as pop errors do not remove any elements from the stack."
      "\n>>> Stack size = 25 (push operations) - 7 (pop operations that removed elements from the stack)"
      "\n>>> Stack size = 18")


# Question 3
def transfer(original_stack, transferred_stack):
    while not original_stack.is_empty():
        transferred_stack.push(original_stack.pop())
    return transferred_stack


print("\n3. (R-6.3) Implement a function transfer(S, T) that transfers all elements from stack S onto stack T, "
      "so that the element that starts at the top of S is the first to be inserted onto T, and the element at the "
      "bottom of S ends up at the top of T.")
stack_one = ArrayStack()
stack_one.push(1)
stack_one.push(2)
stack_one.push(3)
stack_one.push(4)
stack_one.push(5)
print(">>> Length of stack one:\t", len(stack_one))
print(">>> Top of stack one:\t", stack_one.top())

stack_two = ArrayStack()
new_stack = transfer(stack_one, stack_two)
print(">>> Length of stack two:\t", len(new_stack))
print(">>> Top of stack two:\t", new_stack.top())


# Question 4
print("\n4. (R-6.7) What values are returned during the following sequence of queue operations, if executed on an "
      "initially empty queue?")
q = ArrayQueue()
print('>>>', q.data)

q.enqueue(5)
print('>>>', q.data)

q.enqueue(3)
print('>>>', q.data)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

q.enqueue(2)
print('>>>', q.data)

q.enqueue(8)
print('>>>', q.data)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

q.enqueue(9)
print('>>>', q.data)

q.enqueue(1)
print('>>>', q.data)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

q.enqueue(7)
print('>>>', q.data)

q.enqueue(6)
print('>>>', q.data)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

q.enqueue(4)
print('>>>', q.data)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

dequeue = q.dequeue()
print('>>> Return:', dequeue)

print('>>>', q.data)


# Question 5
print("\n5. (R-6.8) Suppose an initially empty queue Q has executed a total of 32 enqueue operations. 15 dequeue "
      "operations were also executed, 5 of which raised Empty errors that were caught and ignored. What is the "
      "current size of Q?")
print(">>> Size of Q:"
      "\n>>> 32 enqueue operations - 10 dequeue operations (5 empty errors did not alter the size of Q) Size of Q = 22")


# Question 6
print("\n6. (R-6.13) Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8), in this order. Suppose "
      "further that you have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other "
      "variables) and results in D storing the elements in the order (1,2,3,5,4,6,7,8).")

deque = collections.deque([1, 2, 3, 4, 5, 6, 7, 8])
print(">>>", deque)
queue = ArrayQueue()
while not len(deque) == 0:
    queue.enqueue(deque.popleft())
print('>>> Queue - Length:  ', len(queue))
print('>>> Queue - First Element: ', queue.first())


# Question 7
print("\n7. (R-6.14) Repeat the previous problem using the deque D and an initially empty stack S.")

deque = collections.deque([1, 2, 3, 4, 5, 6, 7, 8])
stack = ArrayStack()
print(">>>", deque)
while not len(deque) == 0:
    stack.push(deque.popleft())
print('>>> Stack - Length: ', len(stack))
print('>>> Stack - Top Element: ', stack.top())
