from django.urls import path
from . import views

urlpatterns = [
  path('',views.post_list,name='post_list'),
]
# nameはviewの名前らしい
# localhostへアクセスしてくると、8000/前の部分をdjangoは無視して、自身のフォルダ内を8000/以下の部分で検索する。