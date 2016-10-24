from django.conf.urls import url
from accounts import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^user_page/', views.user_page, name='user_page'),
    url(r'^timeline/', views.timeline, name='timeline'),
    url(r'^search_result/', views.search_result, name='search_result'),
    url(r'^user_settings/', views.user_settings, name='user_settings'),
    url(r'^user_media/', views.user_media, name='user_media'),
    url(r'^following/', views.following, name='following'),
    url(r'^followers/', views.followers, name='followers'),

]
