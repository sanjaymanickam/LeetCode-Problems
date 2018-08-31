"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""
import numpy as np
import math
class Solution:
    def euclid(self,t1,t2):
        return math.sqrt(math.pow(t1[0]-t2[0],2)+math.pow(t1[1]-t2[1],2))
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dist = list()
        dist.append(self.euclid(p1,p2))
        dist.append(self.euclid(p1,p3))
        dist.append(self.euclid(p1,p4))
        dist.append(self.euclid(p2,p3))
        dist.append(self.euclid(p2,p4))
        dist.append(self.euclid(p3,p4))
        set_temp = set(dist)
        if(len(set_temp)!=2):
            return False
        else:
            temp = list()
            for nums in set_temp:
                temp.append(nums)
            temp.sort()
            if round(math.sqrt(2)*temp[0],2) == round(temp[1],2):
                return True
            else:
                return False
