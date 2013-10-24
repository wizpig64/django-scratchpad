Scratchpad
----------

Scratchpad is a very simple blog app I wrote in 5 hours or so to get back into the groove of programming with Django. Nothing fancy like comments or file uploading are that planned at the moment. You can see it in action at http://blog.wizpig64.com/

Used [Django 1.5](https://www.djangoproject.com/), [django-bootstrap3](https://github.com/dyve/django-bootstrap3), [django-endless-pagination](https://github.com/frankban/django-endless-pagination), and [django-markdown-deux](https://github.com/trentm/django-markdown-deux). 

If you plan on deploying this for some reason, remember to:

- `python manage.py collectstatic` - the static folder is included in the repo but git will ignore its contents.
- Remove the sample DB and `python manage.py syncdb` to create your own.
- More details are given specifically for Heroku users at the end of settings.py.
