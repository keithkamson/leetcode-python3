class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s            
        matrix = [[] for i in range(numRows)]     
        row = 0                             
        step = 1                         
        for char in s:
            matrix[row].append(char)               
            row += step                     
            if row == 0 or row == numRows-1:  
                step = -step
        
        words = ["".join(m) for m in matrix]     
        return "".join(words)  