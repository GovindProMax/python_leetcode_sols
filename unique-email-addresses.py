class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        finalEmail=set()
        
        for email in emails:

            
            local, domain = email.split("@")
            local = local.split("+")[0]
            local=local.replace(".", "")
            temp=local+"@"+domain
            finalEmail.add(temp)
        return len(finalEmail)