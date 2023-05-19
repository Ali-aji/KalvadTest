## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Ali-aji/KalvadTest.git
$ cd KalvadTest
```

Makr sure you have python and pip installed

```sh
$ python --version
$ pip --version

```

Install pipenv if not installed

```sh
$ pip install pipenv
```

Then install the dependencies:

```sh
$ pipenv install
```

Once `pipenv` has finished downloading the dependencies:

you need to run the migration
```sh
$ python manage.py migrate
```

then create a superuser
```sh
$ python manage.py createsuperuser
```

And navigate to `http://127.0.0.1:8000/admin/`. to logIn to the app.

after that you can navigate to `http://127.0.0.1:8000/`. to create your Cart.


