def find_max_min(n):
    for i in range(len(n)):
        if not isinstance(n,list): #check if argument is a list
            raise ValueError("Input should be a list")
        else:
            result = []
            smallest = min(n)
            largest = max(n)
            if smallest == largest: #check if smallest is equal to largest
                result.append(n[i]) # enter the number in the list called result
                return result
            else:
                result.extend([smallest, largest]) # enter the number in the list called result
                return result


print(find_max_min([3, 3, 3]))