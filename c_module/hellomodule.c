/**
Short example of combining C with Python
T. Walstra, aug. 2018
*/

#include <Python.h>

static PyObject *my_callback  = NULL;

static PyObject* say_hello(PyObject* self, PyObject* args) {
   const char* name;
   int         a;
   int         b;
   int         sum;
   PyObject*   arglist;
   PyObject*   result;
   
   // parse the arguments
   if (!PyArg_ParseTuple(args, "s", &name)) {
      return NULL;
   }
   
   printf("Hello %s!\n", name);
  /* 
   // call the Python function
   a          = 1;
   b          = 2;
   arglist    = Py_BuildValue("(i,i)",a,b);
   result     = PyObject_CallObject(my_callback, arglist);
   Py_DECREF(arglist);
   if (result == NULL) {
      return NULL;
   }
   if (!PyInt_Check(result)) {
      return NULL;
   }
   sum = PyInt_AsLong(result);
   Py_DECREF(result);
   printf("sum %d\n", sum);
   */
   Py_RETURN_NONE;
}

static PyObject* my_set_callback(PyObject* self, PyObject *args) {
   PyObject* result = NULL;
   PyObject* temp;
   
   if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
      if (!PyCallable_Check(temp)) {
         PyErr_SetString(PyExc_TypeError, "parameter must be callable");
         return NULL;
      }
      Py_XINCREF(temp);           // Add a reference to new callback.
      Py_XDECREF(my_callback);    // Dispose of previous callback.
      my_callback = temp;         // Remember new callback.
      
      // Prepare to return "None".
      Py_INCREF(Py_None);
      result = Py_None;
   }
   return result;
}


//=========================== initialize module ===============================
/*
static PyMethodDef HelloMethods[] = {
   {"say_hello",        say_hello,          METH_VARARGS,  "Greet somebody."},
   {"my_set_callback",  my_set_callback,    METH_VARARGS,  "Set a callback."},
   {NULL,               NULL,               0,             NULL}
};
static PyMethodDef adxl362_methods[] = {
	{"init", py_init, METH_NOARGS,"init the ADX362"},
	{"readId", py_readId, METH_VARARGS, "read the device ID"},
	{"status", py_status, METH_VARARGS, "read the device status"},
	{"soft_reset", py_soft_reset, METH_VARARGS, "do a soft reset"},
	{"measure", py_measure, METH_VARARGS, "start the measure mode"},
	{"readX", py_readX, METH_VARARGS, "read X axis"},
	{"readY", py_readY, METH_VARARGS, "read X axis"},
	{"readZ", py_readZ, METH_VARARGS, "read Z axis"},
	{"read_axes", py_read_axes, METH_VARARGS, "read 3 axes"},
	{"set_g", py_set_g, METH_VARARGS,"set g parameter"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef adxl362_module_definition = {
    PyModuleDef_HEAD_INIT, "adxl362", "adx362 spi library", -1, adxl362_methods
};
*/

static PyMethodDef HelloMethods[] = {
   {"say_hello",        say_hello,          METH_VARARGS,  "Greet somebody."},
   {"my_set_callback",  my_set_callback,    METH_VARARGS,  "Set a callback."},
   {NULL,               NULL,               0,             NULL}
};

static struct PyModuleDef hello_module_definition = {
    PyModuleDef_HEAD_INIT, "hello", "hello library", -1, HelloMethods
};

PyMODINIT_FUNC PyInit_hello(void){
	Py_Initialize();
	return PyModule_Create(&hello_module_definition);
}


//PyMODINIT_FUNC PyInit_adxl362(void){
//	Py_Initialize();
//	return PyModule_Create(&adxl362_module_definition);
//}


