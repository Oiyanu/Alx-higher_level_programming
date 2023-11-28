#ifndef _LISTS_H
#define _LISTS_H

#include <stdio.h>

/**
 * struct listint_s - a singly linked list
 * @n: int
 * @next: next node to point
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif
