#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 19-4-3 下午5:48
# @Author : min
# @Site : 
# @function : 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        y=str(x)
        l=len(y)
        i=0
        while i<=l/2:
            if y[i]!=y[l-i-1]:
                return False
            i=i+1
        return True

if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(123))