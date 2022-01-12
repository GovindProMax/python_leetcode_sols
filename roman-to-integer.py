class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I': '1', 'V' : '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        dict_for_I={'V': '4', 'X': '9'}
        dict_for_X={'L': '40', 'C': '90'}
        dict_for_C={'D': '400', 'M': '900'}
        number=0
        index=0
        
        while index <= (len(s)-1):           
            if s[index]=='C' and index != (len(s)-1):
                if (s[index+1] in dict_for_C.keys()):
                    number=number+int(dict_for_C.get(s[index+1]))
                    index=index+2
                else:
                    number=number+int(roman.get(s[index]))
                    index=index+1
            elif s[index]=='X' and index != (len(s)-1):
                if (s[index+1] in dict_for_X.keys()):
                    number=number+int(dict_for_X.get(s[index+1]))
                    index=index+2
                else:
                    number=number+int(roman.get(s[index]))
                    index=index+1
            elif s[index]=='I' and index != (len(s)-1):
                if (s[index+1] in dict_for_I.keys()):
                    number=number+int(dict_for_I.get(s[index+1]))
                    index=index+2
                else:
                    number=number+int(roman.get(s[index]))
                    index=index+1
            else:
                    number=number+int(roman.get(s[index]))
                    index=index+1
        return number