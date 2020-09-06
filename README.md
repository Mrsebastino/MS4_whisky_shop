# Uisge Beatha
The live website can be view here 
[Uisge Beatha](https://git.heroku.com/whisky-shop-uisge-beatha.git)


## UX
### User
 * As a user i want to be able to access the site on any device.

 * As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.
 * As a user, I want to view products details (e.g. image, price, description, rating, provenance), so that I can book/buy some of them. 
 * As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
 * As a user, I want to view and modify my order in the shopping bag before completing it, so that I can make last changes easily before proceeding to payment.
 * As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
 * As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
 * As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.
 * As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.
 * As a user, I want to easily login anytime, so that I can get access to my saved profile.
 * As a user, I want to reset my password if I forgot it.
 * As a user, I want to be able to change my password, to keep my profile secure.

 ### Owner
 * As a user, I want to have convenient and secure admin interface avalable only for website admin, so that I can add, edit and remove products/services.


 
### UI
---

### Wireframes

All drawing for the website can be found  here
[wireframes](https://github.com/Mrsebastino/MS4_whisky_shop/tree/master/static/wireframes/), they includes mobile and desktop.

### Technologies Used
#### Languages
* [HTML5](https://www.w3schools.com/html/default.asp)
* [CSS3](https://www.w3schools.com/css/default.asp)
* [Javascript](https://www.w3schools.com/js/default.asp)
* [Python](https://www.w3schools.com/python/default.asp)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/)
#### Libraries and Framework
* [Django](https://docs.djangoproject.com/en/3.1/)
* [Bootstrap](https://getbootstrap.com/)
* [FontAwesome](https://fontawesome.com/)
* [Favicon](https://favicon.io/)
* [Google Fonts](https://fonts.google.com/)
* [JQuery](https://api.jquery.com/)
* [Gunicorn](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/gunicorn/)
* [Psycopg2](https://pypi.org/project/psycopg2/)
* [Stripe](https://stripe.com/gb)
* [Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)
### Tools
* [Gitpod](https://www.gitpod.io/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Heroku](https://heroku.com/)
* [AWS S3 Bucket](https://aws.amazon.com/)
* [Boto3](https://boto3.amazonaws.com/)
### Bugs encountered
While making change to my `checkout Models` one migration got corrupted. I had a look and my mentor had a look, and the problem was with `Django`. My Mentor suggested to just create a new DB it would be quicker than keep looking for the bug.

When migrating files to `postgres` and error showed up.
`django.db.utils.ProgrammingError: cannot cast type integer to date
LINE 1: ...R COLUMN "release_date" TYPE date USING "release_date"::date`
I first rename the field, migrate to `sqlite3`, and then migrate to `postgres` again, still an error. I checked with tutor support and the problems was with some of the existing migration, deleting them fixed the bug.
