class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return [] 
        listoflist=[]
        column=1
        index=0
        while m !=0:
            listoflist.append([])
            m-=1
        for element in listoflist:
            while column <= n:
                element.append(original[index])
                column+=1
                index+=1
            column=1
        return listoflist
        