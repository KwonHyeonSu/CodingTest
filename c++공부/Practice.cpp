#include <iostream> //라이브러리

int main(void) {
	// '<<'는 무언갈 더 하고 싶을 때 사용하는 이음표같은것.
	// std::endl은 개행
	std::cout << "Hello World" << std::endl;
	std::cout << "Hello" << "World" << std::endl;

	int a = 10;
	int b;
	char c = 'a';
	float d = 1.50f;
	double e = 1.50;

	b = 20;

	std::cout << a << " " << b << std::endl;
	std::cout << c << std::endl;
	std::cout << d << std::endl;
	std::cout << e << std::endl;

	std::cout << "숫자를 입력해주세요: ";
	std::cin >> a;

	std::cout << "a의 변수값 : " << a << std::endl;

	if (a == 10) {
		std::cout << "일치!" << std::endl;
	}
	else {
		std::cout << "불일치!" << std::endl;
	}

	return 0;
}