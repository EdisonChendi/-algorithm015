import unittest
from typing import List
from pprint import pprint


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        # no dp solution
        # just stack
        stack = []
        for ch in s:
            # 0 - not matched
            # 1 - matched
            if ch == "(":
                stack.append([ch, 0])
            else:
                for j in reversed(range(len(stack))):
                    if stack[j][1] == 0:
                        if stack[j][0] == "(":
                            stack[j][1] = 1
                            stack.append([ch, 1])
                            break
                        else:
                            # stack[j][0] == ")"
                            stack.append([ch, 0])
                            break
                    else:
                        # stack[j][1] == 1
                        continue
                else:
                    stack.append([ch, 0])

        longest = 0
        cur_strike = 0
        for _, color in stack:
            if color == 0:
                longest = max(longest, cur_strike)
                cur_strike = 0
            else:
                # color == 1
                cur_strike += 1
        longest = max(longest, cur_strike)
        return longest

    def longestValidParentheses2(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        stack = []
        poped = [None]*len(s)
        for i, ch in enumerate(s):
            if ch == ")" and stack and stack[-1][1] == "(":
                o_idx, _ = stack.pop()
                poped[o_idx] = 1
                poped[i] = 1
            else:
                stack.append((i, ch))
        longest = 0
        cur = 0
        for z in poped:
            if z == 1:
                cur += 1
            else:
                longest = max(longest, cur)
                cur = 0
        longest = max(longest, cur)
        return longest

    def longestValidParentheses3(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        stack = [(-1, None), ]
        longest = 0
        for i, ch in enumerate(s):
            if ch == ")" and stack and stack[-1][1] == "(":
                stack.pop()
                if stack:
                    longest = max(i-stack[-1][0], longest)
                else:
                    stack.append((i, ch))
            else:
                stack.append((i, ch))
        return longest

    def longestValidParentheses4(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0

        def count(s, reverse=False):
            left, right = 0, 0
            longest, cur = 0, 0
            if reverse:
                s = s[::-1]
            for ch in s:
                if ch == "(":
                    left += 1
                else:
                    right += 1
                if not reverse:
                    if left == right:
                        longest = max(longest, left+right)
                    elif right > left:
                        left, right = 0, 0
                else:
                    if left == right:
                        longest = max(longest, left+right)
                    elif left > right:
                        left, right = 0, 0

            return longest

        return max(count(s), count(s, True))

    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0

        # ()
        # ))
        N = len(s)
        dp = [0]*N
        for i, ch in enumerate(s):
            if ch == "(":
                continue
            if i >= 1 and s[i-1] == "(":
                dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
            elif i >= 1 and s[i-1] == ")":
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = 2 + dp[i-1] + \
                        (dp[i-dp[i-1]-2] if i - dp[i-1]-2 >= 0 else 0)
        return max(dp)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "(()"
        expected = 2
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = ")()())"
        expected = 4
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = ")()(())"
        expected = 6
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = ")()((((((())"
        expected = 4
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "()"
        expected = 2
        self.assertEqual(sol.longestValidParentheses(s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
