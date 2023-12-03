#include "lists.h"
/**
 * is_palindrome - checks for a singly-linked list is a palindrome
 * @head: pointer to address of first node on the list
 * Return: 1 if list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int list_length = 0;

	if (!*head)
		return (1);

	temp = *head;
	while (temp)
	{
		list_length++;
		temp = temp->next;
	}
	if (list_length % 2 != 0)
		return (0);

	return (1);
}
