#include <stdio.h>
#include <string.h>
#include "lists.h"

char *_strRev(char *str)
{
    int len, i;
    char ch;

    len = strlen(str);
    for (i = 0; i < len / 2; i++)
    {
        ch = str[i];
        str[i] = str[len - 1 - i];
        str[len - 1 - i] = ch;
    }
    return (str);
}

int is_palindrome(listint_t **head)
{
    listint_t *temp = head;
    int count, i = 0, j = 0;

    while (temp != 0)
    {
        count++;
        temp = temp->next;
    }
    char str[count * sizeof(*int)] = "";
    while (temp->next != NULL)
    {
        str[i] = temp->n;
        i++;
    }
    str[i] = '\0';
    char str1[count * sizeof(*int)] = _strRev(str);
    if (str == _strRev(str1))
        return 1;
    else
        return 0;
}
