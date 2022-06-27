#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int check__cycle(listint_t *list)
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
			printf("There is a cycle.")
			return (1);
		}
	}
	return (0);
}
