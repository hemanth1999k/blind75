class Solution:
    def intToRoman(self, num: int) -> str:
        potti={1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        vidai=""
        summa=0
        l=sorted(list(potti.keys()),reverse=True)
        n=0
        while summa<num:
            print(n)
            if l[n]<=num and (summa+l[n])<=num:
                summa+=l[n]
                vidai+=potti[l[n]]
            else:
                n+=1
        return vidai

            