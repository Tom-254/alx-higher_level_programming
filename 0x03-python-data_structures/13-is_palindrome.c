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
 * compare_lists - compares the values of two lists
 * @head1: pointer to head1 list
 * @head2: pointer to head2 list
 * Return: 0 for not equal and 1 for equal
 */

int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it's not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *second_half, *fast_ptr = *head, *slow_ptr = *head,
	*prev_of_slow_ptr = *head, *middle_node = NULL;
	int equals;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			middle_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse_list(&second_half);
		equals  = compare_lists(*head, second_half);

		if (middle_node != NULL)
		{
			prev_of_slow_ptr->next = middle_node;
			middle_node->next = second_half;
		}
		else
		{
			prev_of_slow_ptr->next = second_half;
		}
	}
	return (equals);
}
