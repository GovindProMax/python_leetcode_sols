class Solution:
    def singleNumber(self, nums: List[int]) -> int:      
        mydict={}
        for n in nums:
            if n in mydict:
                mydict[n] = True
            else:
                mydict[n] = False
        key_list = list(mydict.keys())
        val_list = list(mydict.values())
        position = val_list.index(False)
        return key_list[position]