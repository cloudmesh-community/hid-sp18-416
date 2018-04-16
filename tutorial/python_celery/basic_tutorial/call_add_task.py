from add_module import add_two_numbers

response = add_two_numbers.apply_async((4,6))
print(response.get())
