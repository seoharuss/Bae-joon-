#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int k, n;
	long long first = 1, last = 0, mid, max_len = 0;	//랜선의 길이를 더했을 때 정수형 범위 넘어갈 수 있음
	scanf("%d %d", &k, &n);

	int* len = (int*)malloc(sizeof(int) * k);
	for (int i = 0; i < k; i++) {	//랜선 길이 중 가장 큰 것 추출
		scanf("%d", &len[i]);
		if (len[i] > last)
			last = len[i];
	}
	while (first <= last) {	
		int count = 0;
		mid = (first + last) / 2;

		for (int j = 0; j < k; j++) {	//가지고 있는 랜선을 잘라 자른 개수 만큼 count에 저장
			count += len[j] / mid;
		}
		if (count >= n) {		//정해진 개수보다 더 많이 자르거나 같은 경우
			if (max_len < mid)	//최대 자를 수 있는 길이 수정
				max_len = mid;	
			first = mid + 1;	
		}
		else
			last = mid - 1;		//정해진 개수보다 조금 자른 경우
	}
	printf("%lld\n", max_len);
	free(len);
	return 0;
}
