

# 采用 % 格式化操作符
# C风格的格式字符串，在Python里四个缺点
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))


# 内置的format函数和str类的format函数
# 逗号表示千分位分隔符，^表示居中对齐
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

print("str.format 方法只剩下历史意义了，推荐使用f-string")
# 插值格式字符串
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')







