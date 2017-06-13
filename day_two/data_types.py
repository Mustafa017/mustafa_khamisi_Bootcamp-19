def data_type(n):
    if isinstance(n,str):#check if argument is string 
        return len(n)   #return length of argument
    elif isinstance(n,bool): #check if argument is boolean
        return n
    elif isinstance(n,int): #check if argument is integer
        if n == 100:
            return "Equal to 100" 
        elif n > 100:
            return "more than 100"
        else:
            return "less than 100"
    elif isinstance(n,list): #check if argument is list
        if len(n) >= 3: #check if length of list is greater than or equal to 3 
            return n[2] # return item in position 3
        else:
            return None # return None if length of list is less than 3
    else:
        return "no value" # return no value if the argument is not among the data types defined above.