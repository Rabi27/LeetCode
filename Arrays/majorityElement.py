class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #We can use a HashMap that maps elements to counts in order to count 
        #occurrences in linear time by looping over nums. Then, we simply return the key with         #maximum value.
        counts = collections.Counter(nums)
        
        return max(counts.keys(),key=counts.get)
        
        