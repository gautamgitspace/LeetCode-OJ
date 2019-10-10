class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            to, domain = email.split("@")
            to = self.process_to(to)
            # we don't really care about domains.
            # all new domains need to be considered
            unique.add(to + "@" + domain)
        return len(unique)

    def process_to(self, to):
        copy = to
        if '.' in copy:
            copy = copy.replace('.', "")
        if '+' in copy:
            index = copy.find('+')
            copy = copy[:index]
        return copy
