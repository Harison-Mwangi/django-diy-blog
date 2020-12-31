# django DIY blog
A basic blog to complete MDN django tutorials assessment

![Django CI](https://github.com/Harison-Mwangi/django-diy-blog/workflows/Django%20CI/badge.svg?branch=dev)

## Instructions

> 1. Create and activate a **virtual environment** using [```pipenv```](https://pypi.org/project/pipenv/)
      by running ```$ pipenv shell```
> 2. Install the dependencies using ```$ pipenv install --dev```
> 3.  Run database migrations using ```$ python manage.py migrate```
> 4. Use ```$ python manage.py runserver``` to run the development server.

### Note
> - Use ```$ coverage run manage.py test``` or ```$ python manage.py test``` to run the tests
>- Use ```$coverage report``` to see [_coverage.py_](https://coverage.readthedocs.io/en/latest/)'s test results in the command line
> - Use ```$ coverage html``` to generate HTML for _coverage.py_'s  test results. Go to ```<repository root>/htmlcov/index.html``` to see the results.