class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        original_len=len(nums)
        new_arr=[]
        res_dct = {nums[i]: 0 for i in range(0, len(nums), 1)}
        
        print(res_dct)
        
        
        for i in range(1,original_len+1):
            if i not in res_dct:
                new_arr.append(i)
        return new_arr