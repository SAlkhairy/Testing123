from django.conf.urls import url
from accounts import views


urlpatterns = [
    url(r'^registration/', views.registration, name='registration'),
    url(r'(?P<user_id>)/timeline/', views.timeline, name='timeline'),
    url(r'^search_result/', views.search_result, name='search_result'),
    url(r'^user_settings/', views.user_settings, name='user_settings'),
    url(r'(?P<user_id>)/user_media/', views.user_media, name='user_media'),
    url(r'(?P<user_id>)/following/', views.following, name='following'),
    url(r'(?P<user_id>)/followers/', views.followers, name='followers'),
    url(r'(?P<user_id>)/user_page/', views.user_page, name='user_page'),

    url(r'(?P<user_id>)/add_post/', views.add_post, name='add_post'),
    url(r'(?P<user_id>)/edit_post/', views.edit_post, name='edit_post'),
    url(r'(?P<user_id>)/delete_post/', views.delete_post, name='delete_post')
]
