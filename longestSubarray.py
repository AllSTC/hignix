class Solution:
  def longestSubarray(self,nums: list[int],k:int)->int:

    left,curr_sum,max_len =0,0,0

    for right in range(len(nums)):
          curr_sum += nums[right]
          while curr_sum>k and left<=right:
            curr_sum-=nums[left]
            left+=1
          max_len = max(max_len,right-left+1)
    return max_len
