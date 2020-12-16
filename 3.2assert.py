"""
#3.2.8
assert abs(-42) == -42, "Should be absolute value of a number"
#составное сообщение об ошибке
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

#составной assert
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", f"Wrong language, got {catalog_text} instead of 'Каталог'"


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

x=test_input_text(11,111)
"""
"""
#3.2.9 составные сообщения об ошибках и поиск подстроки
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert str(substring) in str(full_string), f"expected '{substring}' to be substring of '{full_string}'"

x = test_substring(some_text,some)
"""