$('#demo').DataTable({
  autoWidth: false,
  serverSide: true,
  processing: true,
  responsive: true,
  ajax: {
    url: '/concat-col-app/data/',
    type: 'GET',
  },
  columnDefs: [
    {targets: 0, data: 'id'},
    {targets: 1, data: 'title'},
    {targets: 2, data: 'breeding'},
  ]
});
