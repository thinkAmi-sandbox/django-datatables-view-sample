$(document).ready(function() {
  const app = new SearchApp();
  app.addEventHandler();
  app.loadDataTable();
});


class SearchApp {
  constructor() {
    // DataTableインスタンスを保持しておきたいため、クラスとして定義
    this.instance = null;
  }

  addEventHandler() {
    $('#filter').on('click', () => {
      // columnsの引数には、columnDefsで定義した列indexをセット
      this.instance.columns(1).search($('#filterName').val());
      this.instance.columns(3).search($('#filterIsBornInNagano').prop('checked'));
      this.instance.draw();
    })
  }

  loadDataTable() {
    this.instance = $('#demo').DataTable({
      autoWidth: false,
      serverSide: true,
      processing: true,
      responsive: true,
      ajax: {
        url: '/search-app/data/',
        type: 'GET',
      },
      columnDefs: [
        {targets: 0, data: 'id'},
        {targets: 1, data: 'name'},
        {targets: 2, data: 'color__name'},
        {
          targets: 3,
          data: 'born_in_nagano',
          render: data => {
            const checked = data ? 'checked="checked"' : '';
            return `<input type="checkbox" ${checked} />`;
          }
        },
      ]
    });
  }
}



