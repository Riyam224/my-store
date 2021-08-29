# PROJECT TITLE : Store for trendy outfits

#### Video Demo: 

[ VIDEO DEMO ](https://www.youtube.com/watch?v=ni7CmpY0rCQ)

#### Description:

Full stack project with payment integration and also the ability of the user to do shopping as Registered user and also as a Guest user 



#### Setup Instructions 

**install python3.9 version  to make sure everythinh works**



[Download Python 3.9.5](https://www.python.org/downloads/)



**Setup and activate  your Virtual Environment for Django for windows** 



```bash
pip install virtualenv
```

**Start virtualenv**
In your windows command prompt, head to your project location: 

```bash
cd my_project
```

Once inside the project folder run: 

```bash
virtualenv env
```

**Activate virtualenv**
On Windows, virtualenv (venv) creates a batch file called 


```bash
virtualenv env
```

To activate virtualenv on Windows


```bash
env\Scripts\activate
```



**Install Required Python Modules**



```bash
pip install -r requirements.txt
```


**Installing the project**

```bash
open terminal and type
```

TODO GITHUB URL 

**or simply download using the url below**

THE GITGUB URL 


#### To migrate the database open terminal in project directory and type

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Static files collection
open terminal and type


```bash
python manage.py collectstatic
```




#### Creating Superuser

To create superuser open terminal and type

```bash
python manage.py createsuperuser
```

### To run the program in local server use the following command

Then go to [http://127.0.0.1:8000](http://127.0.0.1:8000)in your browser



### Project snapshot


**Home Page (Store page )**

![store](https://user-images.githubusercontent.com/36796463/120848399-993a5500-c529-11eb-9d53-b4461df76704.png)



**product details**
![product details](https://user-images.githubusercontent.com/71698431/120935443-6a7bd480-c70b-11eb-8192-2109f24f4285.PNG)


**Cart Page**

![cart](https://user-images.githubusercontent.com/71698431/120851857-15f91d80-c582-11eb-8b98-9c1a4bb3df45.png)







**Checkout  Page for Registered user**

![checkout](https://user-images.githubusercontent.com/36796463/120848065-2c26bf80-c529-11eb-98ad-cf5cf72d80eb.png)


**Checkout Page for Guest user**

![checkout](https://user-images.githubusercontent.com/71698431/120851343-5a37ee00-c581-11eb-9e59-b759202c79b6.jpg)



**Login Page**

![login](https://user-images.githubusercontent.com/71698431/120852479-ec8cc180-c582-11eb-8e9a-ef1b30297f3f.png)



**Profile Page**

![profile](https://user-images.githubusercontent.com/36796463/120847913-fd104e00-c528-11eb-9a29-3f56b061d99b.png)


**Edit Profile Page**



![edit profile](https://user-images.githubusercontent.com/71698431/120852944-9cfac580-c583-11eb-8456-5c9b8f8f8ce8.png)




## code details 

**project coding files**


![coding files ](https://user-images.githubusercontent.com/71698431/120937658-5b028880-c717-11eb-9668-9f0cb956ddb6.jpg)


**online django admin page details with all the models that registered in the  apps admin pages**

![django admin page](https://user-images.githubusercontent.com/71698431/120937854-905ba600-c718-11eb-9b5a-2165608ff13a.jpg)

## some of ecommerce project important files 

**ecommerce settings.py**

 A Django settings file contains all the configuration of your Django installation.



![settings.py](https://user-images.githubusercontent.com/71698431/120938077-ccdbd180-c719-11eb-804a-7d8c943318e3.jpg)


![settings.py](https://user-images.githubusercontent.com/71698431/120938277-9488c300-c71a-11eb-962e-66d47309a642.jpg)




**project main urls.py**

this is the main urls file for all the apps in the project 
so it contains the urls for **store app**   , and  **accounts app** urls.

* path('accounts/', include('django.contrib.auth.urls'))

this url for DJANGO site authentication urls (the login , logout , password management)

*  path('accounts/', include('accounts.urls')),

for other authentication pages 

*  path('' , include('store.urls')),

for the STORE app 


![urls](https://user-images.githubusercontent.com/71698431/120939154-4629f300-c71f-11eb-89c1-74b642e91f5b.jpg)




## Store App files


**models.py**

A model is the single, definitive source of information about my  data. It contains the essential fields and behaviors of the data iam storing. Generally, each model maps to a single database table.

and in this app , need tables for  (Customer, Product , Order,  OrderItem  , ShippingAddress)

Customer table with its columns

![model1 store](https://user-images.githubusercontent.com/71698431/120939550-36131300-c721-11eb-8702-b7bf74b2613c.PNG)

Product table with its columns

![model2 store](https://user-images.githubusercontent.com/71698431/120939562-46c38900-c721-11eb-95f3-a24a5e421cfd.PNG)

Order table with its columns

![model3store](https://user-images.githubusercontent.com/71698431/120939571-4fb45a80-c721-11eb-8e9c-f9693abf75a7.PNG)


OrderItem table with its columns

![model4store](https://user-images.githubusercontent.com/71698431/120939578-56db6880-c721-11eb-86e6-30c1a7867464.PNG)

ShippingAddress table with its columns

![model5store](https://user-images.githubusercontent.com/71698431/120939585-5fcc3a00-c721-11eb-8314-283617843560.PNG)


**admin.py**

to register store models and show it on the admin panal page of django 


![admin store](https://user-images.githubusercontent.com/71698431/120939802-7030e480-c722-11eb-923d-97055d1b078e.PNG)





**views.py**

A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response



so views  ===  logic of the app 
and here need views for :
* store ( home page) 
* product_detail 
* cart
* checkout  
* updateItem 
* process_order 



and here the code pages for all the views above 

* store view 


![store view in store app](https://user-images.githubusercontent.com/71698431/120940012-a1f67b00-c723-11eb-9e55-5c2652a4063a.PNG)


* product details  view 

![product details store](https://user-images.githubusercontent.com/71698431/120940058-dcf8ae80-c723-11eb-98e8-33f625b4f832.PNG)


* cart view

![cart store](https://user-images.githubusercontent.com/71698431/120940078-044f7b80-c724-11eb-873a-0a6c4e6ad5ad.PNG)


* checkout view 


![checkout store](https://user-images.githubusercontent.com/71698431/120940096-15988800-c724-11eb-8cd1-800f82917752.PNG)


* orderItem view 

![orderitem view](https://user-images.githubusercontent.com/71698431/120940109-38c33780-c724-11eb-8c1c-28bec0147997.PNG)


* process_order view 

![process order view](https://user-images.githubusercontent.com/71698431/120940128-5395ac00-c724-11eb-8389-ca523b8f29a3.PNG)




**urls.py**

this file contains pages needed urls in store app like :

* store
* product_details
* cart
* checkout 
* update_item
* process_order



![urls store](https://user-images.githubusercontent.com/71698431/120940240-f51cfd80-c724-11eb-860f-36c20ea8a472.PNG)





**vtils.py**

file for dont repeat the code in the views 

![utils store](https://user-images.githubusercontent.com/71698431/120940515-51345180-c726-11eb-97e9-32c1a2402e36.PNG)



## Static folder 

contains  the css , js , fonts and images files that needed in the whole project .



![statics](https://user-images.githubusercontent.com/71698431/120940671-1a127000-c727-11eb-936e-c7e03f8160b8.PNG)


## Templates  folder 

A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.

The syntax of the Django template language involves four constructs.


so in my project  .. there are templates for  store app , accounts app and 
also main.html page template that all pages inherited from .


![templates and main page](https://user-images.githubusercontent.com/71698431/120940931-7c1fa500-c728-11eb-926f-6b62415cdb9c.PNG)





## Accounts App 

this app for  user authentication pages  so it contains 
the details of login , logout , signup ,  and password management  ....
and also for profile (social login) 

**models.py**

contains classes that i need to add in database to manage 
accounts pages and profile page 


![197237888_509051993853110_6515079656697607303_n (3)](https://user-images.githubusercontent.com/71698431/121067774-24d70e80-c7d4-11eb-8f7c-7a06fe22fda0.jpg)


**admin.py**


![accounts admin](https://user-images.githubusercontent.com/71698431/121067992-623b9c00-c7d4-11eb-95fd-936bea4eda92.PNG)



**forms.py**

forms for signup  , user and profile 

![forms](https://user-images.githubusercontent.com/71698431/121071837-22c37e80-c7d9-11eb-987e-e01821ba1296.jpg)


**views.py**

signup view and also prodile , edit_profile view 

* signup view


![196789760_856593631882643_8719692968304207799_n](https://user-images.githubusercontent.com/71698431/121072379-cdd43800-c7d9-11eb-92cf-42bb669af01c.jpg)


* profile and edit_profile views 


![198281673_515959056273611_7605581834866677196_n](https://user-images.githubusercontent.com/71698431/121072438-e3496200-c7d9-11eb-865b-2e784bea108e.jpg)


**urls.py**

for signup page , also prodile , edit_profile 


![urls accounts](https://user-images.githubusercontent.com/71698431/121072481-f1977e00-c7d9-11eb-93c4-77256ae89e77.PNG)




## paypal integratation  

to integrate paypal into the website to allow the user to checkout either with the default paypal checkout option or with the debit credit card that also provided with paypal . 


to add paypal buttons to the checkout page  go to this link 


[paypal buttons link](https://developer.paypal.com/docs/archive/checkout/how-to/customize-button/#supported-locales)

here working with client side integration 
so using sandbox accounts to send and recieve the payments

[sandbox accounts ](https://developer.paypal.com/developer/accounts/)



![paypal1](https://user-images.githubusercontent.com/71698431/121079750-370c7900-c7e3-11eb-8a0d-80234945eeab.PNG)


![paypal explain2](https://user-images.githubusercontent.com/71698431/121079826-53a8b100-c7e3-11eb-8822-54ffc796d16c.PNG)



![sandbox accounts](https://user-images.githubusercontent.com/71698431/121079922-73d87000-c7e3-11eb-91d9-8c15bdf6edbb.PNG)


paypal in checkout page 


![checkout paypal](https://user-images.githubusercontent.com/71698431/121079984-8488e600-c7e3-11eb-8352-efe11169aed2.PNG)


![complete payments](https://user-images.githubusercontent.com/71698431/121080256-e3e6f600-c7e3-11eb-9f98-a0e590ce068a.PNG)



## Packages 


**django-filter**

```bash

pip install django-filter

```

**django-crispy-forms**


```bash

pip install django-crispy-forms

```








# Author

Riyam Hazim
Email: cs50riyam211@gmail.com



                                            ========Thank You !!!=========