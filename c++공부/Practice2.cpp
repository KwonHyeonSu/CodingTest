//함수의 데폴트

#include <iostream>

int Adder(int a = 1, int b = 2) {
	return a + b;
}

int main(void) {

	int a = 10;
	int b = 20;

	std::cout << Adder() << std::endl;
	std::cout << Adder(a) << std::endl;
	std::cout << Adder(a, b) << std::endl;

	return 0;
}