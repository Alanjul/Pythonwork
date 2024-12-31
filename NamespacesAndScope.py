"""Every scope determines where you can use the identifier in the program
Scopes are determined by namespaces, which associate identifiers with
objects
THREE PRIMARY namespces
local, global, built in namespaces
Local namespaces are defined in the methods
Associates local identifies(parameters or variables ) with objects
They are in scope from the time of creation until the end of the method
Global namespaces on module by module basis
Associates global module identifier(s) with objects
Created when python loads the module
Global attributes __name__ contains the name module attribute
assigned with __main__ if python script is run.
Builtin namespaces are created at the time of execution
class namespaces is associated with classes
"""
globalNamespaces = "Global z"
def print_variable():
    y = "Local namespace"
    print(globalNamespaces)
    print(y)
print_variable()