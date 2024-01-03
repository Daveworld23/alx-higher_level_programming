#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: linked list to be checked
 * Return: 1 if there is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *doubled = list;
	listint_t *single = list;

	if (!list)
		return (0);
	while (single && doubled && doubled->next)
	{
		single = single->next;
		doubled = doubled->next->next;
		if (single == doubled)
			return (1);
	}
	return (0);
}
