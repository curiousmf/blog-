from django.urls import path
from blogger.views import *
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('', start_page, name='start'),
    path('register/', RegisterViewPage.as_view(), name='registration'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('<slug:slug>/update/', EditBlogView.as_view(), name='update'),
    path('<slug:slug>/delete/', DeleteBlogView.as_view(), name='delete'),
    path('change/', change_password, name='change'),
    path('reset/', PasswordResetView.as_view(), name='reset')
]