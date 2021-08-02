# def sum_numbers(number, sum=0):
#     if number ==0:
#         return sum
#     sum += number
#     return sum_numbers(number-1, sum)

def sum_numbers(number):
    if number <= 1:
        return number
    return number + sum_numbers(number-1)
    
print(sum_numbers(10))