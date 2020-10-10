from django.urls import path
from django.views.generic import TemplateView

from sort_app.views import AppleAllFieldDataTableView, ApplePermsFieldDataTableView, \
    AppleSomeFieldDataTableView

app_name = 'sort_app'
urlpatterns = [
    # 全列ソート可能
    path('all-columns', TemplateView.as_view(template_name='sort_app/all-columns.html'),
         name='all'),
    path('all-columns/data/', AppleAllFieldDataTableView.as_view()),

    # 一部列のみソート可能
    path('some-columns', TemplateView.as_view(template_name='sort_app/some-columns.html'),
         name='some'),
    path('some-columns/data/', AppleSomeFieldDataTableView.as_view()),

    # 権限により列が可変
    path('perms-columns', TemplateView.as_view(template_name='sort_app/perms-columns.html'),
         name='perms'),
    path('perms-columns/data/', ApplePermsFieldDataTableView.as_view()),
]
