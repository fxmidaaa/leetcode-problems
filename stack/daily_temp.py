class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                previous_day = stack[-1]
                stack.pop()
                answer[previous_day] = curr_day - previous_day
            
            stack.append(curr_day)
        return answer