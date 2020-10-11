from django.urls import path
from django.views.generic import TemplateView

from concat_col_app.views import AppleConcatDataTableView

app_name = 'concat_col_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='concat_col_app/index.html')),
    path('data/', AppleConcatDataTableView.as_view()),
]
