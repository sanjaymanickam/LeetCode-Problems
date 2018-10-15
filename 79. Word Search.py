"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

import numpy as np
class Solution(object):
    temp = list();
    def recur(self,board,i,j,word):
        print(i,j,board[i][j],word)
        self.temp[i][j] = 1
        if word == "":
            return True;
        t1 = False
        t2 = False
        t3 = False
        t4 = False
        if j-1>=0 and board[i][j-1] == word[0] and self.temp[i][j-1]!=1:
            t3 = self.recur(board,i,j-1,word.replace(board[i][j-1],"",1))
        if j+1<len(board[0]) and board[i][j+1] == word[0] and self.temp[i][j+1]!=1:
            t4 = self.recur(board,i,j+1,word.replace(board[i][j+1],"",1))
        if i-1>=0 and board[i-1][j] == word[0] and self.temp[i-1][j]!=1:
            t1 = self.recur(board,i-1,j,word.replace(board[i-1][j],"",1))
        if i+1<len(board) and board[i+1][j] ==word[0] and self.temp[i+1][j]!=1:
            t2 = self.recur(board,i+1,j,word.replace(board[i+1][j],"",1))
        if t1==t2==t3==t4==False:
            self.temp[i][j]=0
        return t1 or t2 or t3 or t4
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.temp = np.zeros((len(board), len(board[0])))
                    if self.recur(board,i,j,word.replace(board[i][j],"",1)):
                        return True
        return False
