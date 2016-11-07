from django.conf.urls import url
from accounts import views


urlpatterns = [

    url(r'^registration/', views.registration, name='registration'),
    url(r'^search_result/', views.search_result, name='search_result'),
    url(r'^settings/', views.edit_common_profile, name='edit_common_profile'),
    url(r'(?P<user_id>)/user_media/', views.user_media, name='user_media'),
    url(r'(?P<user_id>)/following/', views.following_list, name='following'),
    #url(r'(?P<user_id>)/followers/', views.followers, name='followers'),
    url(r'(?P<user_id>)/', views.timeline, name='timeline'),

    url(r'^add_post/', views.add_post, name='add_post'),
    url(r'^edit_post/(?P<post_id>\d+)', views.edit_post, name='edit_post'),
    url(r'^delete_post/(?P<post_id>\d+)', views.delete_post, name='delete_post'),
    url(r'^view_post/(?P<post_id>\d+)', views.view_post, name='view_post'),
]