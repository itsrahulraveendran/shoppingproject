from django.urls import path
# from views import SearchResult
from . import views

app_name='searchapp'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]
