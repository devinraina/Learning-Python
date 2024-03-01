import re 
  
  
match = re.search(r'portal', 'GeeksforGeeks: A computer science for geeks portal') 
print(match) 
print(match.group()) 
  
print('Start Index:', match.start()) 
print('End Index:', match.end())
print("\n \n")

def function():
    print("function \n")
    print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: computer science portal for geeks'))
    print("\n \n")
    
def function1():
    print("function1 \n")
    print('Range',re.search(r'[a-zA-Z]', 'x'))
    print("\n \n")

def function2():
    print("function2 \n")
    print(re.search(r'[^a-z]', 'c'))
    print("\n \n")
    
def function3():
    print("function3 \n")
    print(re.search(r'G[^e]', 'Geeks'))     
    print("\n \n")
    
def function4():
    print("function4 \n")
    print('Geeks:', re.search(r'\bGeeks\b', 'Geeks'))
    print('GeeksforGeeks:', re.search(r'\bGeeks\b', 'GeeksforGeeks'))
    print("\n \n")
    
def function5():
    print("function5 \n")
    match = re.search(r'^Geek', 'Campus Geek of the month')
    print('Beg. of String:', match)
    
    match = re.search(r'^Geek', 'Geek of the month')
    print('Beg. of String:', match) 
    # End of String 
    match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks')
    print('End of String:', match)
    print("\n \n")
    
def function6():
    print("function 6 \n")
    print('Any Character', re.search(r'p.th.n', 'python 3'))  
    print('\n \n')
    
def function7():
    print("Function 7 \n")
    print('Color',re.search(r'colou?r', 'color'))
    print('Colour',re.search(r'colou?r', 'colour'))
    print("\n \n")
    
def function8():
    print("function 8 \n")
    print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '18-08-2020'))
    print("\n \n")
    
def function9():
    print("function 9 \n")
    print('Three Digit:', re.search(r'[\d]{3,4}', '189'))
    print('Four Digit:', re.search(r'[\d]{3,4}', '2145'))
    print("\n \n")

def function10():
    print("function 10 \n")
    print(re.search(r'[\d]{1,}','5th Floor, A-118,\ Sector-136, Noida, Uttar Pradesh - 201305'))
    print("\n \n")
    
    
# Calling functions 
function()  
function1()  
function2()  
function3() 
function4() 
function5() 
function6() 
function7() 
function8()  
function9()
function10()