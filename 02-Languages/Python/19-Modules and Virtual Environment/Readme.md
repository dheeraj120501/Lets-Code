# Modules

Modules are of 2 types built-in modules and external modules.
We can directly import a built in module as it is already installed.
External modules can be of further 2 types the one which we create local one or the one which someone else created(from the internet).
The local external modules can also be directly imported.
The internet external modules first need to be installed through pip.
PIP is like play store of python just like npm is playstore of js.
To install an external module we use pip install module_name.
Once installed the external modules can also be imported easily.
To import any module to your project we can use import module_name.
File name of our python file shouldn't match any module name, use unique names.

We can import a module in lots of ways

- standard import: `import os`
- importing a module with different name: `import math as m`
- importing specific things from a module: `from tkinter import messagebox`
- importing my custom module : `import functions as func`

# Working of import

When we import a module then it import all it's variable and functions as well as execute the entire py file/module.

When working with a custom module sometimes we don't want specific things to get imported we use `if __name__ == "__main__"`

- `__name__` is a special built-in variable that returns us the name of the module being used, if the module being used if the same module/py file then it return `__main__` otherwise(if used in other file as import) it's file name so anything under this if block will not be executed in case of import as it will return the py file name, generally we keep the executable code of a py file/module in this block if in case we have to import it in some other py file.

# Virtual Environment

A virtual environment is a tool or an aid provided to us by Python to keep the dependencies that we have utilized earlier in a few projects, constant.
Virtual Environment saves the current state of our compiler along with the state of their modules and libraries.
We can also install different packages and “dataframes” in our virtual environment.

To create a virtual environment we can also use:

- `py -m venv virtualenv_name` // to create a new virtual environment named virtualenv_name

Once created we need to activate it to start using that env for this just run the activate file in the env folder through shell.

- `.\virtualenv_name\Scripts\activate`
- `deactivate` // to deactivate the env

requirements.txt is just like package-lock.json that keeps the record of all the modules installed in that virtual environment.

- `pip freeze > requirement.txt` // do this in same dir. of vir. env.

pip install package_name == version // to install a package's specific version
pip install -r .\requirements.txt // to install all packages of requirement txt file
