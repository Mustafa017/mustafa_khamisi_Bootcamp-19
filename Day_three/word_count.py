def words(n):
    result = {} #output should be a dictionary
    if isinstance(n,dict):  # check if argument is a dictionary
        for key,value in result.items(): #loop over keys and their values in the dictionary
            return key, value
    else:
        for x in n.split():     #separates all whitespace and returns a list of all the words in the string
            try:
                if x not in result: 
                    result[int(x)] = 1  #start count if x does not exist in dictionary
                else:
                    result[int(x)] += 1 #increment count if x exists in dictionary
            except:
                 if x not in result: 
                    result[x] = 1  #start count if x does not exist in dictionary
                 else:
                    result[x] += 1 #increment count if x exists in dictionary
            
        return result