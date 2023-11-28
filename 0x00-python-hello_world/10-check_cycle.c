#include "lists.h"
/**
 * check_cycle - function that checks if a list has a cycle
 * @list: linked list
 * Return: 1 if there is cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *rapid, *steady;

	if (!list || !list->next)
		return (0);
	rapid = list;
	steady = list;

	while (steady != NULL && rapid != NULL && rapid->next != NULL)
	{
		steady = steady->next;
		rapid = rapid->next->next;
		if (steady == rapid)
		{
			return (1);
		}
	}
	return (0);
}
