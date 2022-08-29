#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer of the heade of list
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		current->next = prev;
		prev = current;
		next = current->next;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it's not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;

	if (*head == NULL)
		return (1);
	/*Find Middle */
	while (fast_ptr->next && fast_ptr->next->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	/*reverse from middle*/
	slow_ptr = reverse_list(&slow_ptr);

	/*compare both */
	fast_ptr = *head;
	while (slow_ptr && fast_ptr)
	{
		if (slow_ptr->n != fast_ptr->n)
			return (0);
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next;
	}
	return (1);
}
