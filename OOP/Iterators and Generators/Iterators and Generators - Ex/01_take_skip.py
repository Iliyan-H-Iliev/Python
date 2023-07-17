class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0 - self.step
        self.start_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.start_count >= self.count - 1:
                raise StopIteration
            self.start_count += 1
            self.start += self.step
            return self.start


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
