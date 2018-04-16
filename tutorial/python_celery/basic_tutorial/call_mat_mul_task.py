from mat_mul_module import matrix_multiplication  

response = matrix_multiplication.apply_async((20,21))
print(response.get())
