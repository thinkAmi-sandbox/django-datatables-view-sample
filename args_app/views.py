from django_datatables_view.base_datatable_view import BaseDatatableView

from concat_col_app.models import Apple


class AppleArgsDataTableView(BaseDatatableView):
    model = Apple

    columns = [
        'id',
        'title',
        'color__name',
    ]

    def render_column(self, row, column):
        if column == 'color__name':
            return row.color.name

        return super().render_column(row, column)

    def filter_queryset(self, qs):
        qs = super().filter_queryset(qs)

        # 追加されたクエリパラメータによる絞り込み
        limitation = self._querydict.get('limitation')
        if limitation == 'yellow':
            qs = qs.filter(color__name='黄')

        return qs
