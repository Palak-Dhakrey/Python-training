hasattr() and getattr() in Python-
Both hasattr() and getattr() are used to work with attributes (variables, functions, or methods) of objects dynamically.
-The hasattr(object, name) function checks if an object (like a module, class, or instance) has a specific attribute.
-The getattr(object, name[, default]) function retrieves an attribute from an object.
If the attribute does not exist, it returns a default value (if provided) or raises an AttributeError
-USE OF GREET().
To get a custom message when calling from another module.
To test if a module is properly imported.
To provide helper functions that don’t execute automatically.

-Exploring sys.modules and Reloading Modules in Python
Python caches imported modules in sys.modules to avoid reloading them unnecessarily and improve performance.

Concept	                              Behavior
sys.modules['mymodule']:	Shows the cached reference of mymodule.
importlib.reload(mymodule):	Reloads mymodule without restarting Python.
del sys.modules['mymodule']:Removes mymodule from cache, forcing re-import.
