class Solution:
    def modify(self):
        self.chars[self.index] = self.char
        self.index += 1
        if self.count == 1:
            return
        number = str(self.count)
        for i in range(len(number)):
            self.chars[self.index] = number[i]
            self.index += 1

    def compress(self, chars: List[str]) -> int:
        self.chars, self.char, self.count, self.index = chars, chars[0], 1, 0
        for i in range(1, len(chars)):
            if chars[i] == self.char:
                self.count += 1
            else:
                self.modify()
                self.char, self.count = chars[i], 1
        self.modify()
        return self.index
        
