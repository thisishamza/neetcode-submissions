class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1,numRows+1):
            row = [0]*i
            row[0] = 1
            if i > 1:
                row[-1] = 1
            if i>2:
                prev_row = triangle[-1]
                for j in range(1,i-1):
                    row[j] = prev_row[j] + prev_row[j-1]                
            triangle.append(row)
        return triangle
            
