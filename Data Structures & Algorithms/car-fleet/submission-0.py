class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = list(zip(position, speed))
        points = list(reversed(sorted(points)))
        stack = []
        for point in points:
            if len(stack) == 0:
                stack.append(point)
            else:
                top = stack[-1]
                top_position = top[0]
                top_speed = top[1]
                position = point[0]
                speed = point[1]
                if (target - position) * top_speed > (target - top_position) * speed:
                    stack.append(point) 
        return len(stack)