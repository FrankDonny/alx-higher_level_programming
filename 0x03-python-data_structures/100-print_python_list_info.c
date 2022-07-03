#include "Python.h"

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t ob_size, a;
	PyObject *object;
	struct _typeobject *type;
	
	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		ob_size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", ob_size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (a = 0; a < ob_size; a++)
		{
			object = list->ob_item[a];
			type = object->ob_type;
			printf("Element %ld: %s\n", a, type->tp_name);
		}
	}
}
