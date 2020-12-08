#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has
 *  a cycle in it
 * @list: head of singly linked list
 *
 * Return: 0 no cycle, 1 if is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *verif;

	if (!list)
		return (0);

	while (list)
	{
		verif = list;
		list = list->next;
		if (verif <= list)
			return (1);
	}
	return (0);
}
