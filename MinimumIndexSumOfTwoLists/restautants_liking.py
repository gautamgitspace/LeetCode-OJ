class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        likes = list(set(list1)&set(list2))
        if len(likes) == 1:
            return likes
        common = collections.defaultdict(list)
        for restaurant in likes:
            index1 = list1.index(restaurant)
            index2 = list2.index(restaurant)
            index_sum = index1 + index2
            common [index_sum].append(restaurant)
        return common[min(common.keys())]
