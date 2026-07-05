# Given an array with some integer type values. Write a python script to sort the array values. 

def sort():
    #making the array ---> 
    import array as arr
    my_array = arr.array('i', [5,3,8,9,4,45,23,89,91,12])
    print("The given array is: ", my_array)

    #now sorting the array with bubble sort ---> 
    #nested for loops will be used, 1 loop for passes and 2nd loop for number of passes. 

    for i in range(0, len(my_array)-1, 1):    #passes loop
        for j in range(0, len(my_array)-i-1, 1): #comparisons loop
            if my_array[j+1]<my_array[j]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    
    print("The sorted array is: ", my_array)

# Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.

def int_pop():
    l = [1, "Ayush", 2, "Rahul", 3, "Abhinav", 4, "Pushkar", 5.5, "lalit", "This    is an element", 6.7, 4.543]

    popped =[]

    for i in range(len(l)-1, -1, -1):   #try to implement for loops from backwards when popping elements.
        if isinstance(l[i], int) == False:
            popped.append(l.pop(i))

    print("The list with all integer values is: ", l)
    print("The removed non integer elements are: ", popped)



# Write a python script to calculate the average of all the elements in a list


l = []

def making_list():
    n = int(input("Enter the number of elements you want to find the average of: "))
    
    for i in range(n):
        elem = int(input("Enter element: "))
        l.append(elem)

    print("The elements are: ", l)
    return l

def avg(list):
    print("The average of the given list is: ", sum(list)/len(list))

avg(making_list())

# Write a python script to create a list of first N prime numbers. 

def prime_num():
    n = int(input("Enter the no. of prime numbers required: "))
    prime_num = []
    non_prime_num = []
    j = 2

    while len(prime_num) < n:
        for i in range(2, int(j*0.5)+1):
            if j%i != 0:
                prime_num.append(j)

            elif j%i == 0:
                non_prime_num.append(j)

            else:
                print("Unexpected error occured, please retry with valid int values.")
            
        j = j+1

    print("The required Prime numbers are: ", prime_num)
    print("The non-Prime numbers are: ", non_prime_num)


# Write a python script to create a list of first N terms of a Fibonnacsi series.

def fibonacci():
    n = int(input("Enter the no. of terms required of Fibonnaci series: "))
    terms = []
    j = 1
    for i in range(n):
        if len(terms) == 0 or len(terms) == 1:
            terms.append(1)
        
        elif len(terms) >= 2:
            next_term = terms[-2] + terms[-1]  #we can also acccess the list from backside, idea is to add the last two terms as in Fibonnaci series. 
            terms.append(next_term)
        
        else:
            print("An unexpected error occured, please try again and don't enter non int invalid values.")
    
    print("The fibonacci series is: ", terms)

fibonacci()
prime_num()
int_pop()
sort()