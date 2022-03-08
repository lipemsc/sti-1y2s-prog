#include <stdio.h>

int main() {
	long long n=0, n1=0, n2=1, op;
	printf("Insira o número: ");
	scanf("%lld", &op);
	while(n < op) {
		n = n2 + n1;
	    	printf("%lld\n", n);
	    	n1 = n2;
	    	n2 = n;
	}
}
