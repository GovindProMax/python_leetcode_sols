class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        finalList=list()
        def backtracking(n, s,openP,closedP,finalList):
            
            if len(s)== n*2:
                finalList.append(s)
                return
            
            if openP < n:
                #s=s+"("
                backtracking(n, s+"(",openP + 1,closedP,finalList)
            if closedP < openP:
                #s=s+")"
                backtracking(n, s+")",openP,closedP + 1,finalList)
                #s.pop()
        
        backtracking(n,"",0,0,finalList)
        return finalList
        