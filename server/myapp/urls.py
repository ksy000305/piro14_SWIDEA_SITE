from django.contrib import admin
from django.urls import path

from myapp.views import idea_list, idea_create, idea_detail, idea_update, devtool_create, devtool_list, devtool_detail, devtool_update, idea_delete, devtool_delete
from django.conf import settings
from django.conf.urls.static import static

app_name='myapp'

urlpatterns = [
    path('', idea_list, name='idea_list'),
    path('idea/create/', idea_create, name='idea_create'),
    path('idea/<int:pk>/', idea_detail, name='idea_detail'),
    path('idea/<int:pk>/update/', idea_update, name='idea_update'),
    path('idea/<int:pk>/delete/', idea_delete, name='idea_delete'),


    path('devtool/create/', devtool_create, name='devtool_create'),
    path('devtool/', devtool_list, name='devtool_list'),
    path('devtool/<int:pk>/', devtool_detail, name='devtool_detail'),
    path('devtool/<int:pk>/update/', devtool_update, name='devtool_update'),
    path('devtool/<int:pk>/delete/', devtool_delete, name='devtool_delete'),

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)