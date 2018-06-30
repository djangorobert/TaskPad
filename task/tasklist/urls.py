from django.urls import path
from . import views
app_name = 'tasklist'

urlpatterns = [

	path('tasks', views.TaskList.as_view(), name='task_list'),
	path('new', views.TaskCreate.as_view(), name='task_form'),
	path('edit/<int:pk>', views.TaskUpdate.as_view(), name='task_update_form'),
	path('delete/<int:pk>', views.TaskDelete.as_view(), name='task_confirm_delete'),
	
]