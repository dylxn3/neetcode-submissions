class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            stack.append((target - p)/s)
            # two stack elements
            # if top of stack < stack [2] it means that at some point
            # if time is greater than prev time will never catch up
            # not making it a fleet
            # they will collide = joing/creating a fleet
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

