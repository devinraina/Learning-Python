# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)



# Python3 Program to Create list
# with integers within given range

def createList(r1, r2):
    if (r1 == r2):
        return r1
    else:
        res = []
        while(r1 < r2+1 ):
            res.append(r1)
            r1 += 1
    return res

# Driver Code
r1, r2 = -1, 5
print("\n")
print("createList1 ")
print(createList(r1, r2))
print("\n")


def createList2(r1, r2):
    print("createList2 ")
    return [item for item in range(r1, r2+1)]
     
# Driver Code
r1, r2 = -1, 10
print(createList2(r1, r2))