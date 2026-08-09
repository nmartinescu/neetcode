class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = students.count(1)
        zeros = students.count(0)
        n = ones + zeros
        i = 0
        while i < n:
            if sandwiches[i]:
                if not ones:
                    break
                else:
                    ones -= 1
            else:
                if not zeros:
                    break
                else:
                    zeros -= 1
            i += 1
        return ones if not zeros else zeros