#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function to check if a there is a loop in a linked list
 * @list: pointer to the structure
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *single_pace, *double_pace;

	single_pace = list;
	double_pace = list;

	while (single_pace && double_pace && double_pace->next)
	{
		single_pace = single_pace->next;
		double_pace = double_pace->next->next;

		if (single_pace == double_pace)
		{
			printf("There is a cycle.");
			return (1);
		}
	}
	return (0);
}
