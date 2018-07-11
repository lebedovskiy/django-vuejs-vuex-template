# Vue.js & Django project template
> A Vue.js project, based on [webpack vuejs-template](https://github.com/vuejs-templates/webpack)

All is pre-ready for start coding - this template include simple blog-app with Django & Django REST framework on backend
and Vue.js & Vuex & Vue-router on frontend. Also I add Pug (Jade) - language of html template.

Summary, it include: 
1. Simple Django project (business_card) with app (posts).
2. Model Post with Serializer and all settings for Django REST Framework and Django CORS headers.
3. (it will be changed!) Basic Hello World Vue.js App from [webpack vuejs-template.](https://github.com/vuejs-templates/webpack)

## Build Setup

``` bash

# clone this repo
git clone https://github.com/lebedovskiy/django-vuejs-vuex-template.git
cd django-vuejs-vuex-template

# creat virtualenv for django
virtualenv .

# install dependencies
npm install
pip install -r requirements.txt

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
Also you can check documentation of [Django REST Framework](https://www.django-rest-framework.org/#quickstart)
