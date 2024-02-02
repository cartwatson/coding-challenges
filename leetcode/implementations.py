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
    
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        notes = [ index for index, element in enumerate(nums) if element == 0 ]
                
        # for index, element in enumerate(nums):
        #     if element == 0:
        #         notes.append(index)

        removed = 0
        for index in notes:
            nums.pop(index - removed)
            nums.append(0)
            removed += 1

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        def count_letters(word: str) -> list[int]:
            counter = {}
            for i in range(len(word)):
                letter = word[i]
                if letter in counter:
                    counter[letter] += 1
                else:
                    counter[letter] = 1

            temp = list(counter.values())
            temp.sort()
            return temp

        if count_letters(word1) == count_letters(word2): return True
        return False
