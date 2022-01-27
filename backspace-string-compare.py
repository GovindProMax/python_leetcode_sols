class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for n in s:
            if n == '#' and stack_s:
                stack_s.pop()
            elif n == '#' and not stack_s:
                print("meh")
            else:
                stack_s.append(n)
        for n in t:
            if n == '#' and stack_t:
                stack_t.pop()
            elif n == '#' and not stack_t:
                print("meh")
            else:
                stack_t.append(n)
        print(stack_s)
        print(stack_t)
        return stack_s == stack_t