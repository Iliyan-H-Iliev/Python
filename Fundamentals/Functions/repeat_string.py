# def repeat_string(string, n):
#     result = string * n
#     return result
#
#
# input_string = input()
# repeat_number = int(input())
#
# print(repeat_string(input_string, repeat_number))


input_string = input()
repeat_number = int(input())

repeat_string = lambda string, numb: string * numb

print(repeat_string(input_string, repeat_number))
