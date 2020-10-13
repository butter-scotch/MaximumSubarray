class Solution:
  def maxSubArray(self, nums):

    bigSum = nums[0]
    curSum = nums[0]

    for i in nums[1:]:
      curSum = max(i, curSum + i)
      bigSum = max(bigSum, curSum)
    return bigSum



result = Solution()
print(result.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# 次の要素を足した値と、次の要素単体の2つを比べる
# bigSum = max(i, curSum + i)

# 大きい方の値をcurSumに入れて更新する
# curSum = bigSum

# curSum = -1, -3, 4, 3, 5, 6, -1, 4
# bigSum = -1, -1, 4, 4, 5, 6, 6, 6