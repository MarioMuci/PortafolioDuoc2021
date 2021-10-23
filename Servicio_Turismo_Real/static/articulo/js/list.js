$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "art_dep_id"},
            {"data": "art_dep_nombre"},
            {"data": "art_dep_estado"},
            {"data": "art_dep_precio"},
            {"data": "f_cat_art.cat_art_nombre"},
            {"data": "art_dep_id"},
        ],
        columnDefs: [
             {
                targets: [3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$'+(data);
                }
            },
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Turismo_Real/EditarArticulo/' + row.art_dep_id + '/" class="btn btn-primary btn-xs"><i class="fa-solid fa-pen-to-square"></i></a>';
                    buttons += '<a href="/Turismo_Real/EliminarArticulo/' + row.art_dep_id + '/" class="btn btn-danger btn-xs"><i class="fa-solid fa-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});