#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer of the list
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *forward = NULL, *prev = NULL;

	while (*head)
	{
		forward = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = forward;

	}
	(*head) = prev;
	return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it's not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_pointer = *head;

	if (*head == NULL)
		return (1);
	/* Find middle */
	while (fast_pointer->next && fast_pointer->next->next)
	{
		slow_ptr = slow_ptr->next;
		fast_pointer = fast_pointer->next->next;
	}
	/*reverse second half*/
	slow_ptr = reverse_list(&slow_ptr);

	fast_pointer = *head;
	/*check if reversed half matches the first half*/
	while (slow_ptr && fast_pointer)
	{
		if (slow_ptr->n != fast_pointer->n)
			return (0);
		slow_ptr = slow_ptr->next;
		fast_pointer = fast_pointer->next;
	}
	return (1);
}
