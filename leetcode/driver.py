from implementations import Solution

solution = Solution()

# template
# for val in []:
#     print(solution.(val))

# for val in [2, 3]:
#     print(solution.climbStairs(val))

# for val in ["the sky is blue", "  hello world  ", "a good   example",]:
#     print(solution.reverseWords(val))

# for val in [
#     [0,1,0,3,12],
#     [0]
# ]:
#     print(solution.moveZeroes(val))

for val in [
    ["abc", "bca"],
    ["a", "aa"],
    ["cabbba", "abbccc"],
    ["cabbba", "aabbss"]
]:
    print(solution.closeStrings(val[0], val[1]))