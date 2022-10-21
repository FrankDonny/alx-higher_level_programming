#include <stddef.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	char str[sizeof(listint_t) + 1];
	char str1[sizeof(listint_t) + 1];
	int i, j;
	
	temp = *head;
	while (temp->next != NULL)
	{
		str[i] = temp->n;
		i++;
	}
	str[i] = 0;
	
	for (j = 0; j == sizeof(str) - 1; j--)
	{
		str1[j] = str[j];
	}
	str1[sizeof(str)] = 0;
	
	if (str == str1)
		return 1;
	else
		return 0;
}
