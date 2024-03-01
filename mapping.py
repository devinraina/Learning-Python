def addition(n):
    return n + n
 
# We double all numbers using map()
numbers = (2, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

def multi(i, x, y):
    return i*x*y

res=[1, 2 , 3, 4 ,5]
res2=[5, 4 , 3, 2 ,1]
res3=[2, "4" ,5, 3 ,1] 
print("multiplied three arrays via mapping \n ",  list(map(multi, res, res2, res3)))

str= ["Hello World", "Python is Fun", "Learning Python"]
print("using map function to derive the length of an array conataing different strings \n", list(map(len, str)))

print("\n\nConverting strings to uppercase and lowercase")
print(list(map(lambda s:s.upper(), str)))
print(list(map(lambda s:s.lower(), str)))

try:
    print("\n\nDividing each element by its next element in the array.")
    div_arr = list(map(lambda x, y : x/y if y !=0 else None, [1,2,3,4,5], [2,4,6,8,10]))
    #Removing 'None' from the list
    div_arr = [i for i in div_arr if i is not None]
    print(div_arr)
except ZeroDivisionError as e:
    print("Encountered an error:",e)    