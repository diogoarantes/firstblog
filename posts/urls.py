from django.urls import path
from .views import post_list
from .views import post_create
from .views import post_delete_list, post_delete
from .views import post_edit_list, post_edit

urlpatterns = [
    path('list', post_list, name='post_list'),
    path('posts/create',post_create,name='post_create'),
    path('delete_list/',post_delete_list,name='post_delete_list'),
	path('delete/<int:id>',post_delete,name='post_delete'),
	path('edit_list/',post_edit_list,name='post_edit_list'),
	path('edit/<int:id>',post_edit,name='post_edit'),
]