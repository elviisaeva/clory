from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'all-stores'),
    path('zara/', views.zara, name = 'zara'),
    path('zara/zara_women/', views.zara_women, name = 'zara_women'),
    path('zara/zara_women/zara_all/', views.zara_all, name = 'zara_all'),
    path('zara/zara_women/zara_dress/', views.zara_dress, name = 'zara_dress'),
    path('zara/zara_women/zara_dress/assembly_dress/', views.assembly_dress, name = 'assembly_dress'),
    path('zara/zara_women/zara_tshirt/', views.zara_tshirt, name = 'zara_tshirt'),
    path('zara/zara_women/zara_trouser/', views.zara_trouser, name = 'zara_trouser'),

]
