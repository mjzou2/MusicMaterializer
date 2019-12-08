from django.urls import path

from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	# path('add', views.add, name='add'),
        path('', views.home, name='home'),
	path('upload', views.upload, name='upload'),
        path('files/<int:pk>', views.delete_file, name='delete_file'),
        path('files', views.file_list, name='file_list'),
        path('help', views.help, name='help'),
	# path('files/upload', views.upload_file, name='upload_file')
]
