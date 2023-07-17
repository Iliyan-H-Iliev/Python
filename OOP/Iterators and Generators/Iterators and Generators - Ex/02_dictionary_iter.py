class dictionary_iter:
    def __init__(self, a_dict):
        self.dict = list(a_dict.items())
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.dict) - 1:
            raise StopIteration

        self.count += 1
        return self.dict[self.count]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
