from django.urls import path


urlpatterns = [
    path('', index_views.index, name='home')
]