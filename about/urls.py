from django.urls import path

urlpatterns = [
    path('about/', about_views.about_me, name='about'),
]