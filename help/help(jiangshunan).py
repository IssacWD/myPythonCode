def f(x):
	if x > 1:
		return x * f(x - 1)
	else:
		return 1
def main():
	n = eval(input("Please input a number"))
	m = eval(input("Please input a number"))
	s = n + m
	c = f(n) / (f(a) * f(m))
	print("C(N,M)=", c)

main()
