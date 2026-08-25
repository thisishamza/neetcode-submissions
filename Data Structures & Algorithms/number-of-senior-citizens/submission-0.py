class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for det in details:
            if int(det[11:13]) > 60:
                seniors +=1
        return seniors
        