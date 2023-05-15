#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct meet {
	int start;
	int finish;
}Meet;

//종료시간으로 정렬하고, 만약 종료시간이 같다면 시작시간으로 정렬한다.
int compare(const void* a, const void* b) {
	const Meet* num1, * num2;
	num1 = (const Meet*)a;
	num2 = (const Meet*)b;

	if (num1->finish != num2->finish) {
		if (num1->finish < num2->finish) return -1;
		else if (num1->finish == num2->finish) return 0;
		else return 1;
	}
	else {
		if (num1->start < num2->start) return -1;
		else if (num1->start == num2->start) return 0;
		else return 1;
	}
}

int main() {
	int meet_count;	//회의의 수
	//회의 시작, 종료 저장 배열
	int possible_meet = 0;	//가능한 회의 수
	int last = 0;
	scanf("%d", &meet_count);

	Meet* meeting = (Meet*)malloc(sizeof(Meet) * meet_count);
	//배열에 시작시간과 종료시간 입력
	for (int i = 0; i < meet_count; i++) {
		scanf("%d %d", &meeting[i].start, &meeting[i].finish);
	}
	qsort(meeting, meet_count, sizeof(Meet), compare);
	for (int i = 0; i < meet_count; i++) {
		if (meeting[i].start >= last) {
			possible_meet++;
			last = meeting[i].finish;
		}
	}
	printf("%d", possible_meet);
	free(meeting);
	return 0;
}
