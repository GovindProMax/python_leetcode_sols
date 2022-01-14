class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hashmap = {
        ")": "(",
        "]": "[",
        "}": "{"
        }
        my_stack=[]
        
        for char in s:
            if char in bracket_hashmap.keys():
                if my_stack and my_stack[-1] == bracket_hashmap[char]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(char)
        if len(my_stack)==0:
            return True
        else:
            return False