# String data type


# literal assignment
#name = 2
#print(type(name))
#print(type(name)== int)


#Question: Write a Python function hello() that returns a JSON response {"message": "Hello, World!"}.
#Find the length of the list and simply swap the first element with (n-1)th element.
def swapList(newList):
    size = len(newList)
     
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = input("enter the list: \n")
 


 

  


