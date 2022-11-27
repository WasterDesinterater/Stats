class stats:
    import math
    def mode(self,collection):
        #A function whose job is to find the most common elements and their frequency
        cell,apex=set(),2
        for piece in collection:
            count=collection.count(piece)
            if {piece}.isdisjoint(cell) and count>=apex:
                if count>apex:
                    apex,cell=count,set()
                    cell.add(piece)
                elif count==apex:
                    cell.add(piece)
        if len(cell)==0:
            return set(collection),1
        return cell,apex
    
    def median(self,collection):
        #A function whose job is to find the midddle number
        if len(collection)%2==1:
            return set([collection[int(len(collection)/2)]])
        return sum(set([collection[len(collection)//2-1]]+[collection[len(collection)//2]]))/2
    
    def mean(self,collection):
        #A function whose job is to find the typical calculated value across a given list
        return sum(collection)/len(collection)

    def varience(self,collection):
        avg=self.mean()
        return sum([(x-avg)**2 for x in collection])/(len(collection))
    
    def STD(self,collection):
        #A function whose job is to determine how far each variable is from the mean
        return self.math.sqrt(self.varience())
   
    def percentile(self,collection,per):
        #A function whose job is to determine the largest value which the percentage ranges from the lowest to the highest
       return max(collection[:int(len(collection)*(per/100))+1])
    
statistics=stats()
"""To use this function, type "from stats import statistics" to use the functions"""

