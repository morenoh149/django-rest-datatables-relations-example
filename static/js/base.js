$(document).ready(function() {
  var table = $('#experts').DataTable({
    "serverSide": true,
    "ajax": "/api/experts/?format=datatables",
    "columns": [
      {"data": "id"},
      {"data": "name"},
      {"data": "objectives"}
    ]
  });
});