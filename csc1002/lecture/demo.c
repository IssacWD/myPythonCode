#include <stdio.h>

int add(int a, int b){
	int c;
	c = a + b;
	return c;
}

int main(void){
	int a, b;
	a = 10;
	b = 13;
	int c = 1;
	int d;
	d = add(c, a);
	printf("%d\n", d);
	return 0;
}
