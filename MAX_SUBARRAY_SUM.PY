#maximum sum of subarray
def maxSubArray(nums):
    maxsum=nums[0]
    cursum=0
    for n in nums:
        if cursum<0:
            cursum=0
        cursum=cursum+n
        maxsum=max(cursum,maxsum)
    return maxsum
maxSubArray()
