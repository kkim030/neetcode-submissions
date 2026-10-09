class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        output = []
        nums.sort()
        sorted_nums = nums
    
        for t in range (0, len(sorted_nums) - 2): # i : target
            if t > 0 and sorted_nums[t] == sorted_nums[t - 1]:
                continue
            i = t + 1
            j = len(sorted_nums) - 1
            while i < j:
                sum = sorted_nums[t] + sorted_nums[i] + sorted_nums[j]
                if sum < 0:
                    i += 1
                elif sum > 0:
                    j -= 1
                else:
                    output.append([sorted_nums[t], sorted_nums[i], sorted_nums[j]])
                    i += 1
                    j -= 1
                    while i < j and sorted_nums[i] == sorted_nums[i - 1]:
                        i += 1
                    while i < j and sorted_nums[j] == sorted_nums[j + 1]:
                        j -= 1
        return output