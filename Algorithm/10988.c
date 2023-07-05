#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char word[100];
	scanf("%s", &word);
	int wrong = 0;
	for (int i = 0; i <= strlen(word)/2; i++) {
		if (word[i] != word[strlen(word) - i - 1]) {
			wrong++;
		}
	}
	if (wrong > 0) printf("%d", 0);
	else printf("%d", 1);
	return 0;
}
