
#First approach

class Solution(object):
    def reverse(self,nums,i,j):
      li=i
      ri=j
      while li<ri:
        temp=nums[li]
        nums[li]=nums[ri]
        nums[ri]=temp
        li+=1
        ri-=1

      

    def rotate(self, nums, k):
        k=k%len(nums)
        if k<0:
            k+=len(nums)
        self.reverse(nums,0,len(nums)-k-1);
        self.reverse(nums,len(nums)-k,len(nums)-1);
        self.reverse(nums,0,len(nums)-1)
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """



                                #OR


# Second Approch


def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0 or k==len(nums):
          return nums
        nums[:]=nums[-k:]+nums[:len(nums)-k]
