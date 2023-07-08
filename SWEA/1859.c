#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 1000001

int arr[MAX] = { 0, };

int main() {
	int test_case;
	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++) {
		int day;
		int result = 0;
		scanf("%d", &day);
		for (int j = 0; j < day; j++) {
			scanf("%d", &arr[j]);
		}
		int tmp = arr[day - 1];
		for (int k = day - 1; k >= 0; k--) {
			if (tmp > arr[k]) {
				result += tmp - arr[k];
			}
			else {
				tmp = arr[k];
			}
		}
		printf("#%d %d\n",i+1, result);
	}
	return 0;
}
