def fizz_buzz(n):
    if n%15 == 0:           #divisible by both 3 and 5
        return "FizzBuzz"
    elif n%5 == 0:          #divisible by 5
        return "Buzz"
    elif n%3 == 0:          #divisible by 3 
        return "Fizz"
    else:                   #not divisible by 3 or 5
        return n