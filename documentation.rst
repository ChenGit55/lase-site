=============
Documentation
=============
--------------
in development
--------------

Introduction
============

This is a personal project to put into practice and improve my knowledge, a simple website developed using the Django framework.

It provides information and a student registration, I did it for a friend who has a "soccer school"

Project Structure
=================

The project follows the standard Django directory structure, with the following main components:

* lase-site: Django project root directory
* src: main app that contains the manage.py file
* students: app that manages students
* programs: app that organizes all programs
* payments: app responsible for payments (in development)
* accounts: app that manages website users
* media: contains all media uploaded by users
* staticp: contains all static files of website
* templates: contains all html pages/templates of website

Required System
===============

* Python 3.8 or above
* Django 3.2 or above

Packages
---------
+ Django Bootstrap
+ Django Widget Tweaks
+ Python Decouple
+ Stripe
+ Pillow

Main Functionalities
====================

Individual pages for programs and special sections
User registration to log in
Student registration

Rotas e URLs
============

The following are the main project routes and URLs:

- `/`: Main page
- `accounts/login/`: Login page
- `accounts/sign-up/`: User registration page
- `students/enroll/`: Student registration page
- `students/`: Student list page
