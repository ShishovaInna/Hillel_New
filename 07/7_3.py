def second_index(text, some_str):
  index_1 = text.find(some_str)
  index_2 = text.find(some_str, index_1 + 1)
  if index_1 == -1 or index_2 == -1:
    return None
  else:
    return index_2

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
