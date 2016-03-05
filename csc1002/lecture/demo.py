import test

a = [1, 'python']
a = 'a string'
c = 1
d = 2
c, d = d, c
def func():
  a = 1
  b = 257
  print(a + b)

print(a)
func()
test.add(1, 2)