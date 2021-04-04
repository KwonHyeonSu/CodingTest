#include <iostream>
using namespace std;

void add(int a, int b, int *sum) {
	*sum = a + b;
}

int main() {
	int a = 3, b = 4;
	int sum = 0;
	add(a, b, &sum);
	cout << sum;
	return 0;
}