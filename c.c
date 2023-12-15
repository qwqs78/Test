#include <stdio.h>

int main(void)
{
    printf("Hello world\n");

    int num1, num2;

    printf("두 수를 입력하세요 : \n");
    printf("%d,%d", &num1,&num2);

    int sum = num1+num2;
    printf(sum);
    


    return 0;

}
