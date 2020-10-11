from django.db.models import Value
from django.db.models.functions import Concat
from django_datatables_view.base_datatable_view import BaseDatatableView

from concat_col_app.models import Apple


class AppleConcatDataTableView(BaseDatatableView):
    model = Apple

    columns = [
        'id',
        'title',
        'breeding',
    ]

    def get_initial_queryset(self):
        # title列を追加
        return super().get_initial_queryset().annotate(
            title=Concat(Value('['), 'color__name', Value('] '), 'name')
        )
