'''
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution1:#直接暴力解决，但是时间和空间开销很大
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
        return []
#time cost:5028 ms space cost:14.8 MB

class Solution2:#巧妙使用字典的哈希性质，减少了一趟循环
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_temp={}
        for i in range(len(nums)):
            if str(target-nums[i]) in dict_temp.keys():
                return [i,dict_temp[str(target-nums[i])]]
            else:
                dict_temp[str(nums[i])]=i
        return []
#time cost:64 ms space cost:15.5 MB

class Solution3:#将solution2中的字典的索引key值从str类型变为int类型，可是反而耗时更多
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_temp={}
        for i in range(len(nums)):
            if target-nums[i] in dict_temp.keys():
                return [i,dict_temp[target-nums[i]]]
            else:
                dict_temp[nums[i]]=i
        return []
#time cost:120 ms	space cost:15 MB
