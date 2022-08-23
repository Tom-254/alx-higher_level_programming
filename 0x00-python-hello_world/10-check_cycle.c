#include "lists.h"

/**
 * check_cycle - checks to see if a list is in an endless loop or cycle
 * uses Floyd's circle finding algorithm
 * @list: the list to check
 * Return: 0 if no cycle is detected, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}