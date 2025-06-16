x = 10
y = 5
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f'{x} * {y} = {x*y}')
print(f'{x}/{y} = {x/y}')
print(f'{x}%{y} = {x%y}')
print(f'{x}^{y} = {x**y}') # Exponentiation x^y
print(f'{x}//{y} = {x//y}') # Floor division

print("\n")
a = 2 # 10 in binary
b = 1 # 01 in binary

a+=b # Similar for other operators a = a+b
print(f'a+=b is {a}')
a=2 # restoring original value
a&=b # AND
print(f'a&=b is {a}')
a=2
a|=b # OR
print(f'a|=b is {a}')
a=2
a^=b # XOR
print(f'a^=b is {a}')
a=2
a<<=b # a: 00000010 b: 00000001 now shifts a bits to left by b(i.e, 1 here) bits
print(f'a<<=b is {a}')
a>>=b # right shift

print(a:=2) # a=2 and print(a)