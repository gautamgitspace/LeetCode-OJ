class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # will act as the container for all the elements
        self.nums = []
        # will store the index of all elements in the
        # container, this will facilitate the removal
        # in O(1). {val : idx}
        self.positions = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.positions:
            # append if idx not found in dict, takes O(1) time
            self.nums.append(val)
            # update idx in dict
            self.positions[val] = len(self.nums)-1
            return True
        return False
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions:
            idx = self.positions[val]
            last = self.nums[-1]
            # put last elem to the removed elem's place
            self.nums[idx] = last
            # update idx of last in dict as it has been
            # copied to the idx of  the removed element
            self.positions[last] = idx
            # remove the extra element as it has been
            # copied to idx position. pop in a list is
            # always O(1)
            self.nums.pop()
            # remove the idx mapping of val from dict
            self.positions.pop(val, 0)
            return True
        return False
