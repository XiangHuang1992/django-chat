# django-chat
使用django、rabbitmq、vue编写的一个聊天程序

# Requirements

## python
* django 2.0
* djoser
* django-notifs
* pika
* uWSGI

## JavaScript
* vue.js
* vue-cli
* vue-router

# Installation

```shell
django-chat-RssXa0NX ❯ pipenv install django
django-chat-RssXa0NX ❯ django-admin startproject chatire .
django-chat-RssXa0NX ❯ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
django-chat-RssXa0NX ❯ pipenv install djangorestframework
django-chat-RssXa0NX ❯ pipenv install djoser
```