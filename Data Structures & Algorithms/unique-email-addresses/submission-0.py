class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            after = emails[i].split("@")[1]
            before = emails[i].split("@")[0].split("+")[0].replace('.','')
            emails[i] = before+'@'+after
        
        return len(set(emails))
