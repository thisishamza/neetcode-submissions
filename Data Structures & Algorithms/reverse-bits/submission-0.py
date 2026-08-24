class Solution:
    def reverseBits(self, n: int) -> int:
        binary_32bit = f"{n:032b}"
        return int(binary_32bit[::-1],2)
