#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * get_nodeint_at_index -  returns the nth node of a listint_t linked list
 * @head: head pointer of singly linked list
 * @index: index to find in list
 *
 * Return: nth node of a listint_t linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int count = 0;

	if (head == 0)
		return (0);

	while (count < index)
	{
		if (head == 0)
			return (0);
		head = head->next;
		count++;
	}
	return (head);
}

/**
 *is_palindrome - 
 *
 *
 *
 *
 */

int is_palindrome(listint_t **head)
{
        listint_t *tmp, *head_t, *index, *other;
	unsigned int count_t = 0, count_h = 0;
	head_t = *head;
        tmp = *head;
	
        if (!head)
        {
                return (1);
        }

	while (tmp)
	{
		tmp = tmp->next;
		count_t++;
	}
        tmp = *head;

	while(count_t != count_h)
	{
		index = get_nodeint_at_index(tmp, count_t - 1);
		other = get_nodeint_at_index(head_t, count_h);
		if (index->n != other->n)
		{
			return (0);
		}
		count_t -= 1;
		count_h += 1;
	}
        return (1);
}



