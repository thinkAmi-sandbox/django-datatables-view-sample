from django.urls import path
from django.views.generic import TemplateView

from search_app.views import AppleSearchDataTableView

app_name = 'search_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='search_app/index.html'),
         name='all'),
    path('data/', AppleSearchDataTableView.as_view()),
]
