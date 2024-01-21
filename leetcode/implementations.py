class Solution:
    # 70 - easy
    def climbStairs(self, n: int, memo: dict={}) -> int:
        # return base cases
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n-1] = self.climbStairs(n-1, memo)
            memo[n-2] = self.climbStairs(n-2, memo)
            return memo[n-1] + memo[n-2]

    def reverseWords(self, s: str) -> str:
        # grab each word
        # reverse the order
        if s == "": return ""
        list = s.split(" ")
        list.reverse()
        new_list = [ item for item in list if item != "" ]
        return " ".join(new_list)