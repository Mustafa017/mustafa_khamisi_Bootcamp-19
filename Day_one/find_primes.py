def find_prime_numbers(n):
    if not isinstance(n,int):
        return "Argument should be an integer"
    else:
        solution = []
        if n < 2:
            return "there are no prime numbers less than 2"
        elif n == 2:
            solution.append(n)
            return solution
        else:
            for i in range(2,n+1):
                for j in range(2,i):
                    if i%j == 0:
                        break
                else:
                    solution.append(i)
            return solution