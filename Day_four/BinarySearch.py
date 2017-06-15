class List:
    def __init__(self):
        pass

class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        self.append(b)
        len_list = 1
        while len_list < a: #Loop to generate the list
            self.append(self[len_list - 1] + b)
            len_list += 1 #increment the length of list

        
    def search(self, item):
        first = 0
        last = self.length - 1
        found = False
        location = {'count': 0, 'index': -1} #initialize count to 0 and index to -1

        if item == self[first]: #item is found in the first position
            location['index'] = 0 # index of item is 0
            return location
        elif item == self[last]: #item is found in the first position
            location['index'] = last # index of item is at the end
            return location
   
        while first <= last and not found:
            midpoint = (first + last)//2 #to find the midpoint integer
            if self[midpoint] == item: # item is found at midpoint
                location['count'] += 1 #increment count
                location['index'] = midpoint # get the index
                found = True
            else:
                if item < self[midpoint]: #consider the left side only
                    last = midpoint-1 # last item of the left side list is before the midpoint 
                else:
                    first = midpoint+1 #first item is immediately after the midpoint
  
        return location