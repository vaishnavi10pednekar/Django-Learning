
from django.urls import path, include
from firstprojectt import views

urlpatterns = [
    path('', views.home, name="home"),
    path('task/', views.task, name="task"),
    path('task/del_task/<task_id>', views.del_task, name="del_task"),
    path('task/edit_task/<task_id>', views.edit_task, name="edit_task"),
    path('task/comp_task/<task_id>', views.comp_task, name="comp_task"),
     path('task/pend_task/<task_id>', views.pend_task, name="pend_task"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('del_con/<data_id>', views.del_con, name="del_con"),
    path('edit_con/<data_id>', views.edit_con, name="edit_con"),
    path('info/', views.info, name="info"),
    path('del_info/<data_id>', views.del_info, name="del_info"),
    path('edit_info/<data_id>', views.edit_info, name="edit_info"),

]
