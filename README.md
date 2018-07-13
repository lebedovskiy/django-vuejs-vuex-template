# Vue.js & Django project template
> A Vue.js + Django project, based on [webpack vuejs-template](https://github.com/vuejs-templates/webpack)

All is pre-ready for start coding - this template include simple blog-app with Django & Django REST framework on backend
and Vue.js & Vuex & Vue-router on frontend. Also I add Pug (Jade) - language of html template and Stylus support for styles.

Summary, it include: 
1. Simple Django project (business_card) with app (posts).
2. Model Post with Serializer and all settings for Django REST Framework and Django CORS headers.
3. [Webpack vuejs-template](https://github.com/vuejs-templates/webpack) with Pug/Jade, SCSS, Axios, Vuex and vue-router.
4. Views for post list from axios (from REST Framework).

**For usage you must comment string ***router.register(r'posts', views.PostViewSet)*** in /posts/urls.py.
This string call django exception when you try ***python manage.py makemigrations***** 

## Build Setup

``` bash

# clone this repo
git clone https://github.com/lebedovskiy/django-vuejs-vuex-template.git
cd django-vuejs-vuex-template

# creat virtualenv for django
virtualenv venv
cd /venv/scripts

# for Windows, better from cmd.exe
activate.bat

# for Linux
./activate

# entry to project directory
cd ..
cd ..

# install dependencies
npm install
pip install -r requirements.txt

```

Be sure that you comment string **router.register(r'posts', views.PostViewSet)** in **/posts/urls.py**!

``` bash
# make migrations and database
python manage.py makemigrations
python manage.py migrate

# also you can add superuser
python manage.py createsuperuser
```

Now you can run develop or production mode: 

``` bash
# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [webpack vuejs-template](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
Also you can check documentation of [Django](https://docs.djangoproject.com/en/2.0/) and [Django REST Framework](https://www.django-rest-framework.org/#quickstart)
