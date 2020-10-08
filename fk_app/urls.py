from django.urls import path
from django.views.generic import TemplateView

from fk_app.views import CultivarsDataTableView

app_name = 'fk_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='fk_app/index.html')),
    path('data/', CultivarsDataTableView.as_view()),
]
