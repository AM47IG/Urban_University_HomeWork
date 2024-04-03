class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        if self.start % 2 != 0:  # Главное начать с четного :)
            self.start += 1
        return self

    def __next__(self):
        self.start += 2  # До исключения, потому что end не включительно!
        if self.start >= self.end:
            raise StopIteration()
        return self.start


en = EvenNumbers(start=-9, end=26)
for i in en:
    print(i)
print(1 in en)  # False быстро


en2 = EvenNumbers(end=1_000_000_000)
print(800 in en2)  # True быстро
# print(1 in en2)  # False долго
