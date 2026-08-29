class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            before, after = emails[i].split("@")
            before = before.split("+")[0].replace('.','')
            emails[i] = before+'@'+after
        
        return len(set(emails))
