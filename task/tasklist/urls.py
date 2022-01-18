from django.urls import path
from . import views
app_name = 'tasklist'

urlpatterns = [

	path('', views.TaskList.as_view(), name='task_list'),
	path('profile', views.profile, name='profile'),
	path('about', views.about, name='about'),
	path('new', views.TaskCreate.as_view(), name='task_form'),
	path('edit/<int:pk>', views.TaskUpdate.as_view(), name='task_update_form'),
	path('delete/<int:pk>', views.TaskDelete.as_view(), name='task_confirm_delete'),
	path('signup/', views.register_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]
	
