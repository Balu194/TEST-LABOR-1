total_size = 1.44
numbers_pages = 100
numbers_of_line = 50
numbers_of_symbols = 25
symbol_size = 4

size_of_all_symbols = (symbol_size + numbers_of_symbols + numbers_of_line + numbers_pages) / 1024 * 2
numbers_books = total_size // size_of_all_symbols

print(size_of_all_symbols)
print(numbers_books)
