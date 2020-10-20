from django.urls import path
from django.views.generic import TemplateView

from args_app.views import AppleArgsDataTableView

app_name = 'args_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='args_app/index.html')),
    path('data/', AppleArgsDataTableView.as_view()),
]
