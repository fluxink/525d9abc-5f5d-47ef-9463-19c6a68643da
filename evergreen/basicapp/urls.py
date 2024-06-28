from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_links, name='page_links'),
    path('<int:page_id>/', views.page_view, name='page_view'),
]
