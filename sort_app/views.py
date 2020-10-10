from django.utils import timezone
from django_datatables_view.base_datatable_view import BaseDatatableView

from sort_app.models import Apple


class AppleAllFieldDataTableView(BaseDatatableView):
    model = Apple

    columns = [
        'id',
        'name',
        'color__name',
        'breeding',
        'season',
        'born_in_nagano',
    ]

    def render_column(self, row, col):
        if col == 'color__name':
            return row.color.name

        if col == 'season':
            if row.season == timezone.now().month:
                return True
            return False

        if col == 'born_in_nagano':
            # Booleanな項目の場合な場合、返し方によりJSでの型が異なるので注意
            # 暗黙的に返す -> JSではstring型
            # 明示的に返す -> JSではboolean型
            return row.born_in_nagano

        return super().render_column(row, col)


class AppleSomeFieldDataTableView(BaseDatatableView):
    model = Apple

    columns = [
        'id',
        'name',
        'color__name',
        'breeding',
        'season',
        'born_in_nagano',
    ]

    order_columns = [
        'id',
        'name',
        'color__name',
        'breeding',
        'season',
        '',  # born_in_nagano部分はソート不可にする
    ]

    def render_column(self, row, col):
        if col == 'color__name':
            return row.color.name

        if col == 'season':
            if row.season == timezone.now().month:
                return True
            return False

        if col == 'born_in_nagano':
            return row.born_in_nagano

        return super().render_column(row, col)


class ApplePermsFieldDataTableView(BaseDatatableView):
    model = Apple

    def get_columns(self):
        results = [
            'id',
            'name',
            'color__name',
        ]

        if self.request.user.is_authenticated:
            results.append('breeding')

        results.extend([
            'season',
            'born_in_nagano',
        ])

        return results

    def render_column(self, row, col):
        if col == 'color__name':
            return row.color.name

        if col == 'season':
            if row.season == timezone.now().month:
                return True
            return False

        if col == 'born_in_nagano':
            return row.born_in_nagano

        return super().render_column(row, col)
