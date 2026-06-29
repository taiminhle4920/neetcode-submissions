class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            name, domain = e.split("@")
            name = name.split("+")[0]
            name = name.replace(".", "")
            res.add((name, domain))
        return len(res)