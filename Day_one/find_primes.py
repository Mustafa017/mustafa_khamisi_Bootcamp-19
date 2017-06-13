def find_prime_numbers(n):
    if not isinstance(n,int):
        return "Argument should be an integer" #the data type of the argument should be integer
    else:
        solution = []
        if n < 2:
            return "there are no prime numbers less than 2" # 0 and 1 are not prime numbers
        elif n == 2:
            solution.append(n)
            return solution
        else:
            for i in range(2,n+1): # to loop from 2 upto n
                sqrt =int(i**0.5) # find the squareroot of i and assign to the variable sqrt
                for j in range(2,sqrt+1): # to loop from 2 upto sqrt
                    if i%j == 0: #to check if i has factors
                        break # move to the next number if i has factors.
                else:
                    solution.append(i) #add i to the list of solution
            return solution # give the entire list of result.
