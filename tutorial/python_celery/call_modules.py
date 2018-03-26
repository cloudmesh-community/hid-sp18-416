from add_module import add_two_numbers
from factorial_module import factorial_of_n
from mat_mul_module import matrix_multiplication  

response = factorial_of_n.apply_async((20000,))
print(response.get())
response = matrix_multiplication.apply_async((20,21))
print(response.get())
response = add_two_numbers.apply_async((4,6))
print(response.get())
