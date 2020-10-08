$('#demo').DataTable({
  'autoWidth': false,
  'serverSide': true,
  'processing': true,
  'responsive': true,
  'ajax': {
    'url': '/fk-app/data/',
    'type': 'GET',
  },
  columnDefs: [
    {targets: 0, data: 'id'},
    {targets: 1, data: 'species__family__name'},
    {targets: 2, data: 'species__name'},
    {targets: 3, data: 'name'},
  ]
});
