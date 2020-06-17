class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        
        getting from word[0] to word[-1] involves finding
        a path from word[0] to word[-1]. knowing if a path
        exists or not, we should do a dfs.
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # dfs helper
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            # all chars are visited
            return True
        # check out of bounds and first char of word matches the starting pt.
        if i < 0 or i >= len(board) or\
           j < 0 or j >= len(board[0]) or\
           word[0] != board[i][j]:
            return False
        # store starting point in temp so that the
        # next iteration picks up the original board
        temp = board[i][j]
        # mark it as '#' and avoid visiting again
        board[i][j] = '#'
        # actual dfs in all directions
        res = self.dfs(board, i+1, j, word[1:]) or\
              self.dfs(board, i-1, j, word[1:]) or\
              self.dfs(board, i, j+1, word[1:]) or\
              self.dfs(board, i, j-1, word[1:])
        # restore board in original form
        board[i][j] = temp
        return res
