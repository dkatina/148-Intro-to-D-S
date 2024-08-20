
#Constant Time

#Assignment ops
from hashlib import algorithms_available


x = 2

#Math Ops (+,-,*,/,%)

y =7

z = y + x

#Comparison Ops
z > x


#Logrithmic: Binary Search 


#Linear: Operations for each piece of data input into the solution

def double_evens(alist):
    output = [] # Constant assignment

    for num in alist: #Linear Loop
        if num % 2 == 0: #Constant math, and comparison
            output.append(num*2) #Constant append
        else:
            output.append(num)

    return output

#Stacked for loops are okay

def double_split(alist):

    evens = []
    odds = []

    for num in alist:
        if num % 2 == 0:
            evens.append(num*2)

    for num in alist:
        if num % 2 != 0:
            odds.append(num*2)

    return (evens, odds)

#Linear Log : Sorting .sort() and sorted()

def sort_nums(alist):

    return sorted(alist) #Anytime you sort within a function you are creating a O(n logn)


#Quadratics: Nested Linear operations
def small_run(alist):
    for num2 in alist:
            print(num2)

def nesting(alist):

    for num1 in alist:
        print('Run:', num1)
        small_run(alist)
        



alist = [2,3,4,5,6,7,8,9,10]

nesting(alist)


#BE CAREFUL OF ADDING METHODS INSIDE OF A FOR LOOP


def count_repeats(alist):

    for num in alist:
        repeates = alist.count(num)
        print(str(num) + "repeats" + str(repeates) + "times")

count_repeats([1,1,2,6,7,2,1,5,9])


if 1 in alist: #Membership checks in a list are linear
    print("got 1")



