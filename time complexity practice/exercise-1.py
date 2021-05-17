def func_one(list):
    # O(n)
    i = 0
    for element in list:
        i=i+1
        print(element)
        if element % 2 == 0:
            print("EVEN STEVEN!")
    print('iterations:',i)

def func_two(list):
    # O(n^2)
    i = 0
    for element in list:
        for element2 in list:
            i=i+1
            print(element, element2)
    print('iterations:',i)
 
def func_three(list):
    # O(1)
    i = 0
    print(list)
    for i in range(0, 100000):
        i = i +1 
        print(i)
    print('iterations:',i)
   
def func_four(list):
    # O(n)
  for element in list:
    print(element)
    
  for element2 in list:
    print(element * element)