# django DIY blog
A basic blog to complete MDN django tutorials assessment

![Django CI](https://github.com/Harison-Mwangi/django-diy-blog/workflows/Django%20CI/badge.svg)

## Instructions

> 1. Create and activate a **virtual environment** using [```venv```](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [```virtualenvwrapper```](https://virtualenvwrapper.readthedocs.io/en/latest/)
> 2. Install the dependencies using ```pip install -r requirements.txt```
> 3.  Make and run migrations using ```python manage.py makemigrations``` and ```python manage.py migrate``` respectively.
> 4. Use ```python manage.py runserver``` to run the development server.

### Note
> - Use ```coverage run manage.py test``` or ```python manage.py test``` to run the tests
>- Use ```coverage report``` to see [_coverage.py_](https://coverage.readthedocs.io/en/latest/)'s test results in the command line
> - Use ```coverage html``` to generate HTML for _coverage.py_'s  test results. Go to ```<the repository root>/htmlcov/index.html``` to see the results.