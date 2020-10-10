$('#all-columns').DataTable({
  autoWidth: false,
  serverSide: true,
  processing: true,
  responsive: true,
  pageLength: 25,  // サンプルデータ量が多いため、デフォルト値を変えておく
  ajax: {
    'url': '/sort-app/all-columns/data/',
    'type': 'GET',
  },
  columnDefs: [
    {targets: 0, data: 'id'},
    {targets: 1, data: 'name'},
    {targets: 2, data: 'color__name'},
    {targets: 3, data: 'breeding'},
    {
      targets: 4,
      data: 'season',
      render: data => {
        const checked = data ? 'checked="checked"' : '';
        return `<input type="checkbox" ${checked} />`;
      }
    },
    {
      targets: 5,
      data: 'born_in_nagano',
      render: data => {
        const checked = data ? 'checked="checked"' : '';
        return `<input type="checkbox" ${checked} />`;
      }
    },
  ],
  order: [
    [3, 'asc'],
    [5, 'desc'],
    // ソートキーが重複した場合にもソートが常に一定となるよう、idをソートキーに加えておく
    [0, 'asc'],
  ],
});


$('#some-columns').DataTable({
  'autoWidth': false,
  'serverSide': true,
  'processing': true,
  'responsive': true,
  'pageLength': 25,  // サンプルデータ量が多いため、デフォルト値を変えておく
  'ajax': {
    'url': '/sort-app/some-columns/data/',
    'type': 'GET',
  },
  columnDefs: [
    {targets: 0, data: 'id'},
    {targets: 1, data: 'name'},
    {targets: 2, data: 'color__name'},
    {targets: 3, data: 'breeding'},
    {
      targets: 4,
      data: 'season',
      render: data => {
        const checked = data ? 'checked="checked"' : '';
        return `<input type="checkbox" ${checked} />`;
      }
    },
    {
      targets: 5,
      data: 'born_in_nagano',
      searchable: false,
      orderable: false,  // ソート不可
      render: data => {
        const checked = data ? 'checked="checked"' : '';
        return `<input type="checkbox" ${checked} />`;
      }
    },
  ],
  order: [
    // ソート不可な列を追加するとエラーになるので注意
    [3, 'asc'],
    // ソートキーが重複した場合にもソートが常に一定となるよう、idをソートキーに加えておく
    [0, 'asc'],
  ]
});


$('#perms-columns').DataTable({
  autoWidth: false,
  serverSide: true,
  processing: true,
  responsive: true,
  pageLength: 25,  // サンプルデータ量が多いため、デフォルト値を変えておく
  ajax: {
    'url': '/sort-app/perms-columns/data/',
    'type': 'GET',
  },

  // columnDefs: () => { /* .. */ } のような定義では動作しないので注意
  columnDefs: getColumnDefs(),

  order: getOrder(),
});


function getColumnDefs() {
  const results = [];
  let colIndex = 0;
  results.push({targets: colIndex++, data: 'id'});
  results.push({targets: colIndex++, data: 'name'});
  results.push({targets: colIndex++, data: 'color__name'});

  if ($('#username').length) {
    results.push({targets: colIndex++, data: 'breeding'});
  }
  results.push({
    targets: colIndex++, data: 'season',
    render: data => {
      const checked = data ? 'checked="checked"' : '';
      return `<input type="checkbox" ${checked} />`;
    }
  });
  results.push({
    targets: colIndex++, data: 'born_in_nagano',
    render: data =>{
      const checked = data ? 'checked="checked"' : '';
      return `<input type="checkbox" ${checked} />`;
    }
  });

  return results;
}


function getOrder() {
  const results = [];
  let bornIndex = 4;  // 非表示時の "born_in_nagano" 位置

  if ($('#username').length) {
    results.push([3, 'asc']);
    bornIndex++;  // 列が増えるため、"born_in_nagano" 位置を修正
  }
  results.push([bornIndex, 'desc']);

  // ソートキーが重複した場合にもソートが常に一定となるよう、idをソートキーに加えておく
  results.push([0, 'asc']);

  return results;
}
