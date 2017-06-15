def find_missing(m,n):
            if len(m) == len(n): #check size of lists are the same 
                return 0
            else:
                if len(m) > len(n): #check if length of list m is greater than length of list n
                    for x in m: #check entries in list m
                        if x in n: #check entries in list m with entries in list n
                            continue 
                        else:
                            return x #return entries not present in lists m 
                else:
                    for y in n: #check entries in list n
                        if y in m: #check entries in list n with entries in list m
                            continue
                        else:
                            return y #return entries not present in lists n

