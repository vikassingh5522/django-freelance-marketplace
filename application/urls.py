from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),
    path('happiness/', views.happiness, name='happiness'),
    path('contact/',views.contact,name='contact'), 
    path('login/',views.login_user,name='login'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('enquiry_details/', views.enquiry_details, name='enquiry_details'),
    path('delete/<int:id>/', views.delete_record, name ='delete_record'),
    path('edit/<int:id>/', views.edit_record, name ='edit_record'),
    path('update/<int:id>/', views.update_record, name ='update_record'),
    path('reports/', views.reports, name ='reports'),
    path('logout/', views.logout_user, name ='logout'),
    path('student_data', views.student_data.as_view(), name ='student_data'),
]