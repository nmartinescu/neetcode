class StringIterator:

    def __init__(self, compressedString: str):
        self.pointer = 0
        self.length = len(compressedString)
        self.compressedString = compressedString
        self.char = None
        self.number = 0
        self.get_next_letter()

    def get_next_letter(self) -> void:
        if self.pointer < self.length:
            self.char = self.compressedString[self.pointer]
            self.pointer += 1
            self.number = 0
            while self.pointer < self.length and self.compressedString[self.pointer].isnumeric():
                self.number = self.number * 10 + int(self.compressedString[self.pointer])
                self.pointer += 1
        else:
            self.char = None
            self.number = 0

    def next(self) -> str:
        if self.hasNext():
            char = self.char
            self.number -= 1
            if not self.number:
                self.get_next_letter()
            return char
        else:
            return " "


    def hasNext(self) -> bool:
        return self.char is not None


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
