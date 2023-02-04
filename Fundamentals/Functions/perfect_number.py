def perfect_number(n):
    result = [i for i in range(1, n) if n % i == 0]
    return result


number = int(input())

if sum(perfect_number(number)) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
