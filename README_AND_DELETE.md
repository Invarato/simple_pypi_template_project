# Steps to create your own module and upload to PyPI (NOT INCLUDE THIS FILE IN THE PROJECT, REMOVE THIS)

## Steps to build project and upload to https://pypi.org/
 1. **Rename** `simple_pypi_template_project` and `simple_pypi_template` folders to your project name 
 (instead blank space use underscore `_`). It is a good idea add "project" word to end of main folder 
 (example: `my_project_name_project`) and code folder use only the name 
 (example:`my_project_name_project/my_project_name`). Example of minimal project structure suggested:
     ```
        my_project_name_project
        |__ my_project_name
        |   |__ __init__.py
        |   |__ my_modules.py
        |__ tests
        |__ LICENSE
        |__ README.md
        |__ setup.py
     ```
 
 2. **Create your Python modules** (your code). To build the project, you need to ensure remove comments and other 
 files you do not want to add in the build to upload.
 
 3. **Check `__init__.py`** if you want to extract one level the package.
    Example, if you hava a blank `__init__.py` third developers need import a method in your package with:
     ```python
        from simple_pypi_template.simple_pypi_template import func_of_my_module
     ```
    If you want the easy import way:
    ```python
       from simple_pypi_template import func_of_my_module
    ```
    You need to add in `__init__.py` this line:
    ```python
    from simple_pypi_template.simple_pypi_template import *
    ```
 
 4. **Create your tests** in `tests` folder. In this template structure you can find an example with `doctest` 
 in `doctest_simple_pypi_template.py` file and `unittest` in `test_simple_pypi_template.py` file; chose the appropriate test
  for your project.
 
 5. **Full fill `setup.py`** data:
    * Change `name` to your project name (instead blank space or underscore use hyphen `-`)
    * Change `version`. PyPI always need a higher version in each update. 
    If this is your first version you can leave: `1.0.0`
    * Fill `author`: your name (or company)
    * Fill `author_email`: your email
    * Fill `description`: your description
    * Fill `url`: your website with the documentation or git project or PyPI page
    * Check `classifiers` and change Lincense and Language if it is necessary.
    * Check `python_requires` and put the minimum Python version.
 
 6. **Choose a license** and put it in `LICENSE` file. You can check https://choosealicense.com/, 
 https://choosealicense.com/licenses/ , https://opensource.org/licenses. In this project template you have 
 a `MIT License`; if this is enough for you, then you only need add your name (or company) in this.
 
 7. **Fill the `README.md`**. In this project template you have a `README.md` template. You can define documentation 
 here then you can delete `doc` folder (and skip 8 point), but it is more professional generate your documentation 
 (see step 8). Useful resources to create a good `README.md`:
    * **Markdown guide** with code examples: https://www.markdownguide.org/getting-started/ (quick examples in  
    https://guides.github.com/features/mastering-markdown/
    * Add **emojis** (select one, copy and paste in `README.md`; only are available a set of emojis in Markdown 
    and appearance depend on system): https://github.com/ikatyang/emoji-cheat-sheet or https://getemoji.com/
        * Example: 😄 😺 💻
    * Add **badges/shields**: https://shields.io/ (examples in https://github.com/Naereen/badges). 
       * Example Static: 
    [![Author](https://img.shields.io/badge/Author-Ramon%20Invarato-green.svg)](https://github.com/Invarato)
       * Example Dynamic: 
    [![PyPI](https://img.shields.io/pypi/v/simple-pypi-template)](https://pypi.org/project/simple-pypi-template/)
    * Create a console **video example**: https://asciinema.org/
        * Example: [![asciicast](https://asciinema.org/a/14.png)](https://asciinema.org/a/14)

 8. Optionally you can **generate your documentation** website with (and save it in `doc` folder):
    * **pydoc** (Python includes this by default), example in project folder:
    ```
        python -m pydoc -w simple_pypi_template
    ```
    * **pycco**: https://pycco-docs.github.io/pycco/
    * **sphinx**: https://www.sphinx-doc.org/en/master/
    * **epydoc**: http://epydoc.sourceforge.net/
    * **readthedocs**: https://readthedocs.org/
    * **doxygen**: https://www.doxygen.nl/manual/docblocks.html
    * **mkdocs**: https://www.mkdocs.org/

 9. If you want to publish your code, then you can **commit and push** your project to git (for example Github)

 10. If you do not have **installed `Twine`**, this is the moment (skip this step if you have already installed):
     ```
        python -m pip install --user --upgrade twine
     ```

 11. **Build your project** with (go to `setup.py` in project dir):
     ```
        python simple_pypi_template_project/setup.py sdist bdist_wheel
     ```

 12. Here you have two options, **upload and test** your application in https://test.pypi.org/ 
 **or upload as a release version** in https://pypi.org/ (this is a summary of 
 https://packaging.python.org/tutorials/packaging-projects/):
* **TEST (PRE-PRODUCTION):**
    1. Get your `API token`, if you do not have one you need:
        1. Create an account or login in https://test.pypi.org/
        2. Create a new `test API token` in https://test.pypi.org/manage/account/
    2. Upload your package:
        ```
            python -m twine upload --repository testpypi dist/*
        ```
        1. When ask you for the user, then write: `__token__`
        2. When ask you for the password, then write: `<<< Your test API token >>>`
    3. Test your package installing with (where `simple-pypi-template` is your project name write 
    in `setup.py` in `name`):
        ```
            pip install -i https://test.pypi.org/simple/ simple-pypi-template
        ```
        4. You can see the last version of your project in (change last part of url with your project name): 
        https://test.pypi.org/project/sorted-in-disk/simple-pypi-template/
    5. Try to import it in other Python scrypt and use it. Example:
        ```python
           from simple_pypi_template import func_of_my_module
        ```    
* **RELEASE (PRODUCTION):**
    1. Get your `API token`, if you do not have one you need:
        1. Create an account or login in https://pypi.org/
        2. Create a new `API token` (this is different to `test API token`) in https://pypi.org/manage/account/
    2. Upload your package:
        ```
            python -m twine upload dist/**
        ```
        1. When ask you for the user, then write: `__token__`
        2. When ask you for the password, then write: `<<< Your API token >>>`
    3. Check your package installing with (where `simple-pypi-template` is your project name write 
    in `setup.py` in `name`):
        ```
            pip install simple-pypi-template
        ```
    4. You can see the last version of your project in (change last part of url with your project name): 
    https://pypi.org/project/simple-pypi-template/
    5. Try to import it in other Python scrypt and use it. Example:
        ```python
           from simple_pypi_template import func_of_my_module
        ```
