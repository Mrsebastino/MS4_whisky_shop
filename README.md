# Uisge Beatha
Whisky is a big business in Scotland, it attract tourism and export all over the world. Almost everybody that visit Scotland leaves with a bottle of Whisky. 
And there is no signs of slowing down, with meals being prepared with Whisky matching instead of wine, being one example.
Whisky can be expensive, specially then older one, and it take times to make Whisky. Some distillery offer a pre-release service, where you can buy Whisky now, while it is still ageing in cask, making it more affordable for the consumers and brining income quicker to the distillery.

The web page goals is to:
* Sell and Promote Scottish Whisky
* Make it quick and easy for customer to buy from the shop
* To offer Whisky that are only available here
* To offer Whisky that are still ageing with a pre-release service

The live website can be view here 
[Uisge Beatha](https://whisky-shop-uisge-beatha.onrender.com/)

## UX
### All Users
 * As a user i want to be able to access the site on any device.

 * As a user, I want to easily navigate the website, so that I can quickly find what I'm looking for.
 * As a user, I want to view products details (e.g. image, price, description, rating, provenance), so that I can buy some of them. 
 * As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
 * As a user, I want to buy Whisky that are not widely available.
 * As a user, I want to view and modify my order in the shopping bag before completing it, so that I can make last changes easily before proceeding to payment.
 * As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
 * As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
 * As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successful.

 ### New users
 * As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.

 ### Users with Profile
 * As a user, I want to easily login anytime, so that I can get access to my saved profile.
 * As a user, I want to reset my password if I forgot it.
 * As a user, I want to be able to change my password, to keep my profile secure.
 * As a user, i want to be able to view my order history.

 ### Owner
 * As a user, I want to have convenient and secure admin interface available only for website admin, so that I can add, edit and remove products/pre-release.
* As a owner, I want to received a copy of the confirmation email send to the user.

### Wireframes

All drawing for the website can be found  here
[wireframes](https://github.com/Mrsebastino/MS4_whisky_shop/tree/master/static/wireframes/), they includes mobile and desktop.

**Notice**. The wireframes were used as a guidances and although most of the design remain true to the original some changes have been applied.
### Features
#### All pages
* NavBar-mobile: The Navbar is  fixed at the top at all time, On mobile the link to the home page is located in the hamburger menu with the links to **all whiskies**, **regions** and **something specials**. Search bar, link to account and link to bag/checkout and a link to the Pre-release offers are on the right of the hamburger menu.
* NavBar-desktop: The desktop has the same features with the logo on top left to allow user to return to the home page. **all whiskies**, **regions** and **something specials** are dropdown menu. 
#### My account-dropdown
* if your are login will will see My Profile or sign out. 
* My profile take you to a page where you can view your order history and edit your details
* sign out take you to a page where you are asked to sign out
* If you are not signed in you will be offered to log in or register.
* If you are sign in and you are a register user, will view the **Product Management** link, this will take you to a page where you can add a new product to the shop.
#### Footer
* The footer is not present on all whisky's page. The reason behind this is that the products page would, in normal shop, be very long, so i didn't saw the need to have a footer a the bottom. On other pages that don't have as much content the users can see the footer without scrolling endlessly.
#### Home page
* Enter our cellar button.
* Footer with logo return to home page(or reload) on the left and social media links on the right.
#### All Whiskies
* A sort bar is located on the right to allow users to search by **price**, **age**, **rating** or **name**. On mobile it located in the center.
* The whiskies are displayed in random order, by clicking on an image we are taking to the product detail page, where we can increase or decrease the quantity, add to our bag or go back to the cellar. 
* Add to bag will trigger a confirmation in the top right corner with a link to the checkout.
* Authorized users can edit or delete products on the all products page or product detail page.
* A back to the top arrow is located on the button right.
#### Shopping Bag
* The shopping bag page give the users a last chance to edit their bag.
* It offers the choice to increase or completely remove a product fromm the bag.
* It offers the chance to bo back to the cellar or to proceed to the checkout.
#### Checkout 
* The checkout page ask the users to add theirs personal details, delivery details and card details.
* On the right the users can view the content of their bag and the total, this is the last chance they have to go back and adjust their bag, a link is provided just beside **complete order** button.
* clicking **complete order** will trigger a success message in top right corner with the order number, and will trigger an email confirmation being send to the user and the shop owner. The full details of the order is displayed on the left.
* A link is offer to go back and view specials whiskies.
### Future Features
* Add the functionality of login with social media link.
* Add the locations of distillery on interactive map.
* Being a student projects all the legals, refunds, cookie and delivery policy need to be research and implemented if this is going to be use as a real business.
### Technologies Used
#### Languages
* [HTML5](https://www.w3schools.com/html/default.asp)
* [CSS3](https://www.w3schools.com/css/default.asp)
* [Javascript](https://www.w3schools.com/js/default.asp)
* [Python3](https://www.w3schools.com/python/default.asp)
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
### Databases
* [Sqlite3](https://www.sqlite.org/index.html) Used with Django
* [PostgreSQL](https://www.postgresql.org/) Used with Heroku
### Testing
* While i was developing the project i was manually testing as i go and checking on Google Chrome Developer Tools after each changes.
* I tested the app on Chrome and Firefox on Laptop and 32inch HD Tv Screen, on the large screen we need to reduce the view to 75%.
* I tested the app on Galaxy S9, S8, A40 and Ipad 6 in all cases the app was responsive and display content as expected.
* The app was built with mobile first approach.
* I used testing provided from Django, i tested forms, views and models. I did not intent to achieve 100% testing in **coverage**.
### Testing functionality
#### NavBar and Footer
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Logo  | click | on homepage reload, on other pages link you back to home page | passed 
| My account  |  click     | open dropdown menu, with link to login or register      | passed
| My Profile | click | take you a a page where you can view your order history and your personal and delivery details | passed
| logout | click | take you to the sign out page, and ask for confirmation | passed
| login | click | take you a form where you enter username and password | passed
| register | click | take you a register form where you are asked to enter your details | passed
| Product Management | click | For register users only. Take you to a page where you can add a new product without having to go into the admin | passed
| Basket icon | click      | if empty reload the page       | passed
| basket icon | click      | if there is something in your bag, redirect you to shopping bag page | passed 
| Navbar      | click  |  all three links open dropdown menu and redirect you to the expected page | passed
| promo-banner | click and hover | take you to all whisky available in pre-release | passed
| logo in footer | click and hover | on homepage reload, on other pages link you back to home page | passed
| social link | click and hover | take you to their pages in a new tab | passed
#### Homepage
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Enter our cellar | click | Take you to the page with all the whiskies | passed
#### All Whiskies
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| sorting bar  | click  |  open a dropdown menu to sort search by various categories in ascending or descending order | passed
| Image   | click | take you to the product details page | passed
| Edit/ Delete | click | If you are a registered user only. Take you to the edit page where you can edit all fields. Delete will delete the product | passed
| back to top arrow | click | take you to the top of the page | passed
#### Product details page
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| image  | click | open then image in a new tab | passed
| quantity-form | click/text | select by using the plus and minus button or by typing in the amount of whisky you want. You can't enter less than 1 or more than 99 | passed
| Edit/ Delete | click | If you are a registered user only. Take you to the edit page where you can edit all fields. Delete will delete the product | passed
| back to the cellar | click | take you back to the all whisky page | passed 
| add to bag | click | open a window with a secure checkout link | passed 
| secure checkout link | click | take you to then shopping bag page | passed
#### Shopping Bag
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| quantity-forms | click/text | to adjust the quantity or removed all products from the bag | passed
| back to the cellar | click | take you back to the all whisky page | passed
| secure checkout | click | take you to the checkout form page | passed
#### Checkout Form
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| form fields | text | The fields will be populated if you are a returning users. Except the card fields | passed
| save profile | checkbox | save all details to the profile for first time  users | passed
| adjust bag | click | take you the shopping bag page for one last chance to change your bag content | passed
| card field |text |  Enter the test card number 4242 4242 4242 4242 and any future expiring data, and any CSV. An error message wil; be trigger if you enter the wrong card details | passed
| complete order | click | take you the checkout success page, it trigger a loading gif, and an email being send to both the user and then shop owner | passed
#### Checkout success
| Test        |  action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
|check specials | click | take you to page that display all whiskies from the ** something specials ** link | passed




### Code Validation
* All HTML passed the validation using W3C Markup Validation
* All CSS files passed the validation using W3C CSS validation service. Jigsaw
* All Python code passed the validation PEP8 online checker.
#### Defensive design
* Warning messages are used when user enter wrong password, email. If the email is already taken and if the passwords check don't matched.

#### Bugs encountered
* While making change to my `checkout Models` one migration got corrupted. I had a look and my mentor had a look, and the problem was with `Django`. My Mentor suggested to just create a new DB it would be quicker than keep looking for the bug. 

* When migrating files to `postgres` and error showed up.
`django.db.utils.ProgrammingError: cannot cast type integer to date
LINE 1: ...R COLUMN "release_date" TYPE date USING "release_date"::date`
I first rename the field, migrate to `sqlite3`, and then migrate to `postgres` again, still an error. I checked with tutor support and the problems was with some of the existing migration, deleting them fixed the bug. And i was then able to deploy to Heroku.

* On the shopping bag page, the plus and minus button to adjust the bag, sometimes appear over the NavBar when we scroll the page up, it is an intermittent problem, as sometimes the page function as expected, i looked online, couldn't find anything helpful, the bug is esthetic, it doesn't affect the functionality of the page. I will look in into it when i have more time.

* I have encountered a problem with **AWS** when deploying to **Heroku**, my project, made a lot more `Pull request` and `Get request` than expected, i checked with the tutor but since it's a third party they couldn't give that much advice. I was advice to get a new **AWS**  `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which i did, but that didn't fixed the issue. I contacted **AWS**, and made a request to be allowed more  `Pull and Get request` , but was only allowed a very small amount. I have made cost calculation, since i will have to cover the cost and it doesn't look to be expensive. I have done  some research and it's seems to be a divided area. Some peoples think it is cause by the static files being in the `S3 Bucket`, but other disagree, one thing i am sure of, is i didn't leak my secret key in my repository. I have ask clarification to **AWS**, i am waiting for an answer.
### Deployment
The project is stored on **Github** and hosted on **Heroku**
#### Local Deployment
 To run this project, the following tools have to be installed:
* An IDE of your choice (I used [Gitpod](https://www.gitpod.io/) for creating this project)
* [Git](https://git-scm.com/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Python3](https://www.w3schools.com/python/default.asp) With Mac it come pre installed.

You will also need to create account with:
* [Stripe](https://stripe.com/gb)
* [AWS](https://aws.amazon.com/) for the [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html)
* An email account of your choice. I used [gmail](https://mail.google.com/)
### Directions
1. You can clone this repository directly into you editor by pasting the following command into the terminal: https://github.com/Mrsebastino/MS4_whisky_shop 
2. Or you can save a copy of this directory by clicking the green button " Clone or download" then "Download Zip" and after that extract the Zip file to your folder, change the directory to the directory file location you just created.
3. For this project i stored all  Stripe secret key in both Heroku setting and Gitpod setting. That way i could still use them for development and production. 

In `settings.py` you can set your variables like in the example below
```
import os

SECRET_KEY = os.environ.get(your secret key)
DEBUG = 'DEVELOPMENT' in os.environ
STRIPE_PUBLIC_KEY = os.getenv(your secret key
STRIPE_SECRET_KEY = os.getenv(your secret key)
STRIPE_WH_SECRET = os.getenv(your secret key)
```
For more info on how to set up the Stripe keys visit [Stripe key](https://stripe.com/docs/keys).

3. Install all requirements from the `requirements.txt` file putting this command into your terminal:
```
pip3 install -r requirements.txt
```
4. In the terminal in your IDE migrate the models to crete a database using the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Load the data fixture (Categories, Specials, Products) in that order using the following command in the terminal
```
python3 manage.py loaddata <fixture name>
```
6. Create a superuser, it will alow you to have access to the admin panel.
you need a username, an email, a password. Note the password won't display in the terminal but will be registered.
```
python3 manage.py createsuperuser
```
7. You can now run the the application using the following command in the terminal:
```
python3 manage.py runserver
```
8. To access the admin panel add `/admin` in the url and enter the details for the superuser you created.

#### Heroku Deployment
In order for Heroku to work properly, the local deployment steps are required.
You will also need to have installed  `gunicorn`, `dj-database-url` and `psycopg`. All of those are already in the project requirements.txt, but for future project they are essentials for Heroku to function properly. 

1. Create a `requirements.txt ` file, which will contains the list of dependencies, using the following command in the terminal:
```
pip3 freeze > requirements.txt
```
2. Create a `Procfile` and inside it type:
```
web: gunicorn whisky_shop.wsgi:application
```
3. On [Heroku](https://heroku.com/) website you can now create your **new app**, assign a unique name(try to use a name as close as possible to the project name for consistency), choose the region the closest to you and click **Create app**.
4. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heroku Postgres**, select **Hobby Dev — Free** and click **Provision*** button to add it to your project. (This is where  `dj-database-url` and `Psycopg` are required.)
5. In the Heroku **settings** click on `Reveal Config Vars` and set the following variables.

| KEY                       | VALUE              
|-----------------          | ------------------ 
| AWS_ACCESS_KEY_ID         | your AWS access key here      
| AWS_SECRET_ACCESS_KEY     | your AWS secret key here  
| DATABASE_URL              | your Postgres DB url here
| EMAIL_HOST_PASSWORD       | you email password(generated by gmail)
| EMAIL_HOST_USER           | your email address
| SECRET_KEY                | your secret key
| STRIPE_PUBLIC_KEY         | your stripe public key here
| STRIPE_SECRET_KEY         | your stripe secretkey here
| STRIPE_WH_SECRET          | your stripe WH secret here
| USE_AWS                   | True

6. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in `settings.py`.
You can temporary comment out the current database settings code and just paste the following in `settings.py`:
```
DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")  
    }
```
This is just a temporary set up that allows to make all the migrations required for our data in our DB to be transfer to Heroku **POstgres**. You shouldn't commit and push at this stage for security reason.

7. Here you can now follow the exact steps, 4, 5 and 6 as explain in local deployment.

8. You can remove the POstgres URL form you settings and uncomment the default DATABASE code form your settings.

9. Add your heroku app url to **ALLOWED_HOST** in the settings file and also include local host.
```
ALLOWED_HOSTS = ['your heroku app name here', 'localhost']
```
10. You can now connect Heroku to Github to automatically deploy each time you push to Github.
In Heroku **Dashboards** select 
* Deploy -> Deployment method -> Github
* link your Github repo name to Heroku
* Click **Enable automatic Deployment**
* Now you you run `git push` in the terminal, it will push to Github and Heroku.
11. After your app has been successfully deployed you can view you project by clicking on **open app**
### Credits

#### Contents
* For this project i have used the Boutique ado tutorial as a reference throughout the development of the project, part of it have been modified to fit this project purpose, some part have been left untouched. (stripe and webhook, AWS, forms, bag and checkout)
* The 3D effect on the logo is inspired from **Coding Master** on Telegram 
* I have used Stack Overflow, Slack and the tutor during the development of the project.
* I also used [Django](https://docs.djangoproject.com/en/3.1/) documentation throughout the project.
#### Media 
* All Photos were taken from Google.
* The description of the Whiskys was taken from [kaggle](https://www.kaggle.com/koki25ando/22000-scotch-whisky-reviews) whisky reviews.
* Then logo name **Uisge Beatha** is Gaelic for Whisky which translate as **Water of life**
### Acknowledgements
* My mentor Brian Macharia for his help.
* The team at student support, Tim, Micheal, Miklos, Stephen, Haley, Cormac, Kevin.