#include <stdio.h>
#include <string.h>		//strlen 사용
//#include <stdlib.h>
#include <stdbool.h>	//bool함수 사용
#define _CRT_SECURE_NO_WARNINGS
#define MAX_ARRAY 51


typedef struct {
	int top;
	int stack[MAX_ARRAY];
}Stack;

void InitStack(Stack* pstack) {
	pstack->top = -1;
}

bool IsEmpty(Stack* pstack) {
	return pstack->top == -1;
}

void Push(Stack* pstack) {
	++(pstack->top);
}

void Pop(Stack* pstack) {
	--(pstack->top);
}

bool IsFull(Stack* pstack) {
	return pstack->top == MAX_ARRAY - 1;	//MAX_ARRAY의 맨 끝은 NULL값이기 때문에 -1을 해서 비교해야한다.
}


int main() {
	Stack stack;
	InitStack(&stack);

	int many;
	char input[51] = { 0, };	//괄호를 넣을 배열
	int uncorrect;				//반복문 종료 후 배열안에 괄호가 남거나 꽉차서 더는 못넣을 때 1씩 증가
	scanf("%d", &many);

	for (int i = 0; i < many; i++) {
		InitStack(&stack);		//새로운 문자열 시작할때마다 top값 초기화
		uncorrect = 0;			//새로운 문자열 시작할때마다 초기화
		scanf("%s", input);
		for (int j = 0; j < strlen(input); j++) {

			if (input[j] == '(') {	//열린 괄호 만났을 때 스택에 push, 스택이 가득찼으면 오류변수 1증가
				if (!IsFull(&stack))
					Push(&stack);
				else
					uncorrect++;
			}
			else if (input[j] == ')') {	//닫힌 괄호 만났을 때 스택에서 pop, 스택이 비어있다면 오류변수 1증가
				if (!IsEmpty(&stack))
					Pop(&stack);
				else {
					uncorrect++;
				}
			}
		}
		if (IsEmpty(&stack) && uncorrect == 0)	//문자열의 반복문을 다 돌린 후에 스택이 비어있으면서 오류변수가 0일때는 VPS다
			printf("YES\n");
		else
			printf("NO\n");
	}
}
