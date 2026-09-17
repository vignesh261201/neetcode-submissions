class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapper={}
        for num in nums:
            freq_mapper[num]= freq_mapper.get(num,0)+1
        
        values=sorted(freq_mapper.items(), key=lambda x: x[1], reverse = True)[:k]

        output=[]
        for value in values:
            output.append(value[0])
        
        return output