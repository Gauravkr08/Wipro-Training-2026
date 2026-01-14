class NumberIterator:
    def __init__(self, n):
        self.current = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

n = 5
for i in NumberIterator(n):
    print(i)





