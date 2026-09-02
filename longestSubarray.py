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
    #subproduct less than k

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l,rp,res = 0,1,0
        for r in range(len(nums)):
            rp *= nums[r]
            while rp>=k:
                rp /= nums[l]
                l+=1
            res+=r-l+1
        return res
      #whose sum is greater than or equal to target

    
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        if sum(nums)<k:
            return 0
        l,csum ,res= 0,0,float('inf')
        for r in range(len(nums)):
            csum+=nums[r]
            while csum>=k:
                res=min(res,r-l+1)
                csum-=nums[l]
                l+=1

        return res
        
