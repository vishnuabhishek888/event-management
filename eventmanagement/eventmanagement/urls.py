from django.contrib import admin
from django.urls import path
from event import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.SignupPage, name='signup'),
    path('login/', event_views.LoginPage, name='login'),
    path('home/', event_views.HomePage, name='home'),
    path('logout/', event_views.LogoutPage, name='logout'),
    path('event/create/', event_views.event_create, name='event_create'),
    path('event/list/', event_views.event_list, name='event_list'),
    path('event/<int:event_id>/rsvp/', event_views.rsvp_create, name='rsvp_create'),
]
