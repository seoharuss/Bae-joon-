#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int age;
	char name[101];
}Person;

int main() {
	int numberOfMember;
	scanf("%d", &numberOfMember);
  //동적할당으로 원하는 수만큼만 할당
	Person *person = (Person*)malloc(sizeof(Person) * numberOfMember);
  //포인터 변수가 NULL을 가리키는 오류가 발생할 수 있으므로 NULL을 가리키는지 먼저 확인해야함.
	if (person != NULL) {
		for (int i = 0; i < numberOfMember; i++) {
			scanf("%d %s", &person[i].age, &person[i].name);
		}
		for (int i = 1; i < 201; i++) {
			for (int j = 0; j < numberOfMember; j++) {
				if (i == person[j].age) {
					printf("%d %s\n", person[j].age, person[j].name);
				}
			}
		}
	}
	free(person);
}

