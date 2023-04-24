from django.urls import path

from web.views import main_view

app_name = 'web'

urlpatterns = [
    path('', main_view)
]