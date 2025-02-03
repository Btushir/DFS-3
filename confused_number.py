"""
Brute force: traverse the numbers from 1 to n and then check for each number of confusing or not.
For example, 161 -> 191
If after 180 degree transformations, the 2 numbers are same then it is not confusing number.
how to get 161 from the 191?
already available number * 10 + current number
already available number = 0
how to get the each digit of 161?
get the first digit: 161%10 = 1, then second digit:
for 161: 0*10+1 =1 , 1*10+ (9: confusing digit of 6) = 19, 19*10+1 = 191
TC: O(n)

A confusing number can only be formed by confusing digits.
                                0
                        / /                     /   /   /
                       0 1                  6   8   9
                        /    /     /   /   /
                        10  11    16 18  19
Generate all possible confusing numebrs.
TC: pow(5,n)
SC: O(number of digits in n)
Note: It is just traversal of the tree then we could BFS. In this method when we append 0 we will keep adding 0 to
the queue.
Todo: DFS
"""

from collections import deque


class Solution:
    def isConfusing(self, num, hmap):
        # new number
        transformed = 0
        original_num = num
        while num > 0:
            # get the last digit
            last_digit = num % 10
            # form the new digit from the hmap
            transformed = transformed * 10 + hmap[last_digit]
            # remove the last digit from the number
            num = num // 10

        if transformed == original_num:
            return False
        else:
            return True

    def confusingNumberII(self, n: int) -> int:
        hmap = {1: 1, 0: 0, 6: 9, 9: 6, 8: 8}
        q = deque()
        q.append(0)
        count = 0
        while q:
            curr_num = q.popleft()

            # check if it's confusing number then increment count
            if self.isConfusing(curr_num, hmap):
                count += 1
            # traverse through hmap
            for key in hmap:
                # form the new number
                newNum = curr_num * 10 + hmap[key]
                # if new number is less than n then only append to queue
                if newNum != 0 and newNum <= n:
                    q.append(newNum)

        return count






