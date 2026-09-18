class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        stk = []

        for index, temp in enumerate(temperatures): 
            while stk and stk[-1][1] < temp: 
                stkIndex, stkTemp = stk.pop()
                temps[stkIndex] = (index - stkIndex)
            stk.append((index, temp))
        
        return temps

