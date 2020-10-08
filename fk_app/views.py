from django_datatables_view.base_datatable_view import BaseDatatableView

from fk_app.models import Cultivars


class CultivarsDataTableView(BaseDatatableView):
    model = Cultivars

    columns = [
        'id',
        'species__family__name',
        'species__name',
        'name',
    ]

    def render_column(self, row, col):
        if col == 'species__family__name':
            return row.species.family.name

        if col == 'species__name':
            return row.species.name

        return super().render_column(row, col)
