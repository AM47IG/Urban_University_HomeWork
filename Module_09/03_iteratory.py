class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        self.start += 2
        if self.start - 2 >= self.end:
            raise StopIteration()
        return result


en = EvenNumbers(start=-9, end=27)
for i in en:
    print(i)
print(1 in en)  # False быстро


en2 = EvenNumbers(end=1_000_000_000)
print(800 in en2)  # True быстро
# print(1 in en2)  # False долго
