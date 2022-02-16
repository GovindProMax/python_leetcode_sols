class Solution:
    def countSegments(self, s: str) -> int:
        myList=[]
        temp=""
        if not s:
            return 0
        listS= list(s)
        
        for index,char in enumerate(listS):
            if char == " " and temp:
                myList.append(temp[:])
                temp=""
            elif (index == len(listS)-1) and char != " ":
                myList.append(listS[index])
                
            elif char != " ":
                temp=temp+char
        return len(myList)