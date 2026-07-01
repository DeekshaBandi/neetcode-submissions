class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #have a defaulydict and loop thought every character in the wrod
        # create a new variable that sorts the word 
        # add the sorted and the original if they match if not then stays empty
        #output the defaultydict lsit 

        output = defaultdict(list)
        for s in strs:
            sorts = ''.join(sorted(s)) #create a new variable that has the sorted value
            output[sorts].append(s) #append the sorted value with the new sorted version 
        return list(output.values())