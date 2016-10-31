from django.conf.urls import url
from accounts import views


urlpatterns = [
    url(r'^registration/', views.registration, name='registration'),
    url(r'(?P<user_id>\d+)/timeline/', views.timeline, name='timeline'),
    url(r'^search_result/', views.search_result, name='search_result'),
    url(r'^user_settings/', views.user_settings, name='user_settings'),
    url(r'(?P<user_id>\d+)/user_media/', views.user_media, name='user_media'),
    url(r'(?P<user_id>\d+)/following/', views.following, name='following'),
    url(r'(?P<user_id>\d+)/followers/', views.followers, name='followers'),
    url(r'(?P<user_id>\d+)/user_page/', views.user_page, name='user_page'),

]
