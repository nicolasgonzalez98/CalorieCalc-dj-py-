from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addFoodUserItem/', views.addFoodUserItem, name='addFoodItem'),
    path('foodItem/', views.food_item, name='food_item'),
    path('createFoodItem/', views.createFoodItem, name='createFoodItem')
]