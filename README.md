### Lecture notes

#### Importance of Data Structures


- **Efficient Retrieval of Data**
- **Optimized Storage Utilization**
- **Enhanced Algorithmic Performance**


#### Data Structures:
With the primary function of data structures being to store information, each data structure has it's own unique features that lend it to being useful in specific scenarios

##### Lists:
Lists are ordered collections of items, allowing for sequential storage and retrieval
```python
# Example of a list in the library
fiction_books = ["Dune", "1984", "Brave New World", "Neuromancer"]
```

##### Dictionaries:
Dictionaries are key-value pairs, providing a fast and flexible way to retrieve information.

```python
# Example of a dictionary in the library
book_locations = {
    "Dune": "Fiction Section, Shelf 1",
    "1984": "Fiction Section, Shelf 2",
    "Brave New World": "Fiction Section, Shelf 3",
    "Neuromancer": "Fiction Section, Shelf 4"
}
```

##### Linked Lists:
Are products of OOP constisting of a Node Class, and a List Class. Node objects carry a value or "data", and also have an attribute "next" which points to the next node in the chain. You build your list by starting with a Head node and continually adding the next node

![Linked List](https://media.geeksforgeeks.org/wp-content/uploads/20220829110944/LLdrawio.png)

```python
# Example of a linked list in the library
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a linked list
head = Node("Book1")
head.next = Node("Book2")
head.next.next = Node("Book3")

# Resulting linked list:
#   Book1 -> Book2 -> Book3
```

#### Others we will talk more about:
- **Stacks:** Collections that follow the LIFO order (Last in First out) *(stack of pancakes)*
- **Queues:** Collections that follow the FIFO order (First in First out) *(song queue)*
- **Binary Trees:** Similar to linked lists we create TreeNode objects that have data, but instead of a "next" attribute they have a left and right attributes that point to other TreeNodes, creating a Node Heirarchy commonly used to store categories with sub-categories
- **Graphs:** Just wait and see :)

#### Time and Space Complexity

**Time Complexity**: How we denote/ measure the execution time of our code as it scales with input size

**Space Complexity**: Measures the memory usage of our algo, also taking into account how it will scale with input.

#### Big O Notation
Big O notation is the measurement scale we use to lable the efficiency of our solutions, O representing the number of operations we do, and n the size of our input.

|| Big O | Efficiency | 
|-----|-------|--------|
| Best|O(1)| Constant|
||O(Log n)| Logrithmic|
||O(n)| Linear|
||O(n logn)| Linear Logrithmic|
|Worst..|O(n^2)| Quadratic

![Big O Graph](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

**Constant**: Assignment operations, math operations, and comparison operations.
**Logrithmic**: Binary Search (we'll learn this later)
**Linear**: for loops, many built-in methods(count,index,replace,etc.) (any time you need to perform an operation FOR every item in the input)
**Linear Logrithmic**: Sorting functions (.sort(), sorted())
**Quadractic**: Whenever you have nested Linear operations you (Nested for loops, .count() inside a for loop)