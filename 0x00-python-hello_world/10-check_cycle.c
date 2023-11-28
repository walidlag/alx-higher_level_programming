#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * Return: If it is cyclical, the value is 1; otherwise, it is 0
 * check_cycle - Verifies whether the list is cyclical
 * @list: Pointer to the list for verification
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}	
