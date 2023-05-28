#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int word_count, group_word = 0, wrong = 0;
	char word[101];
	scanf("%d", &word_count);

	for (int i = 0; i < word_count; i++) {
		scanf("%s", &word);
		for (int k = 0; k < strlen(word); k++) {
			for (int j = k + 1; j < strlen(word); j++) {
				if (word[k] == word[j]) {	//문자 같은 경우
					if (word[j] != word[j - 1]) {	//해당 문자와 이전 문자 비교
						wrong++;	//다르다면 그룹단어가 아님
						break;
					}
				}
			}
		}
		if (wrong >= 1) {
			wrong = 0;
		}
		else {
			group_word++;
		}
	}
	printf("%d\n", group_word);
}
