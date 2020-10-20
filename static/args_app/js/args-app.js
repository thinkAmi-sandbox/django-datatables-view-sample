$('#demo').DataTable({
  autoWidth: false,
  serverSide: true,
  processing: true,
  responsive: true,
  ajax: {
    url: '/args-app/data/',
    type: 'GET',
    // 追加で渡すクエリパラメータを指定
    data: getLimitation(),
  },
  columnDefs: [
    {targets: 0, data: 'id'},
    {targets: 1, data: 'name'},
    {targets: 2, data: 'color__name'},
  ]
});


function getLimitation() {
  const limitation = $('#limitation');
  return limitation.length ? {limitation: limitation.val()} : {};
}
