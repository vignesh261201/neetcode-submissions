class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for string in strs:
            s= s + str(len(string)) + '#' + string 
        return s

    def decode(self, s: str) -> List[str]:
        output=[]
        index=0

        while index < len(s):
            j=index
            
            while s[j] != '#':
                j+=1
            
            length= int(s[index:j])
            output.append(s[j+1: j+1+length])
            index=j+1+length
        
        return output




       