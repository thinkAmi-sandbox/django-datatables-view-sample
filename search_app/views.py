from django.db.models import Q
from django_datatables_view.base_datatable_view import BaseDatatableView

from search_app.models import Apple


class AppleSearchDataTableView(BaseDatatableView):
    model = Apple

    columns = [
        'id',
        'name',
        'color__name',
        'born_in_nagano',
    ]

    def render_column(self, row, col):
        if col == 'color__name':
            return row.color.name

        if col == 'born_in_nagano':
            # Booleanな項目の場合な場合、返し方によりJSでの型が異なるので注意
            # 暗黙的に返す -> JSではstring型
            # 明示的に返す -> JSではboolean型
            return row.born_in_nagano

        return super().render_column(row, col)

    def get_filter_method(self):
        """ 今回は結果をわかりやすくするために、部分一致(大文字小文字区別なし)にする
            デフォルトは、FILTER_ISTARTSWITH
        """
        return self.FILTER_ICONTAINS

    def filter_queryset(self, qs):
        """ Booleanフィールドの値はうまくSearchできない
            そのため、オーバーライドして一部を書き換える
        """
        columns = self._columns
        if not self.pre_camel_case_notation:
            # get global search value
            search = self._querydict.get('search[value]', None)
            q = Q()
            filter_method = self.get_filter_method()
            for col_no, col in enumerate(self.columns_data):
                # col['data'] - https://datatables.net/reference/option/columns.data
                data_field = col['data']
                try:
                    data_field = int(data_field)
                except ValueError:
                    pass
                if isinstance(data_field, int):
                    column = columns[data_field]  # by index so we need columns definition in self._columns
                else:
                    column = data_field
                column = column.replace('.', '__')
                # apply global search to all searchable columns
                if search and col['searchable']:
                    q |= Q(**{'{0}__{1}'.format(column, filter_method): search})

                # column specific filter
                if col['search.value']:
                    # BooleanField対応のため、if col_no を追加し、指定した列だけ処理を変える
                    if col_no == 3:
                        if col['search.value'] == 'true':
                            qs = qs.filter(**{f'{column}': True})
                    else:
                        qs = qs.filter(**{
                            '{0}__{1}'.format(column, filter_method): col['search.value']})
            qs = qs.filter(q)
        return qs
