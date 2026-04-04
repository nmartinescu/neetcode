class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = list(zip(position, speed))
        points.sort(reverse=True)
        stack = []
        for point in points:
            if not stack:
                stack.append(point)
            else:
                [top_position, top_speed] = stack[-1]
                [position, speed] = point
                if (target - position) * top_speed > (target - top_position) * speed:
                    stack.append(point) 
        return len(stack)