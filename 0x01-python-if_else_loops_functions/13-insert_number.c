#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert a number
 * @head: a linked list
 * @number: number to be inserted
 * Return: pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (curr && curr->n < number)
		{
			temp = curr;
			curr = curr->next;
		}

		temp->next = new;
		new->next = curr;
	}
	return (new);
}
