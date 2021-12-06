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
            {"data": "dep_id"},
            {"data": "dep_nombre"},
            {"data": "dep_ubicacion"},
            {"data": "dep_capacidad"},
            {"data": "dep_acondicionado"},
            {"data": "dep_canon_renta"},
            {"data": "dep_estado"},
            {"data": "dep_costo_mes"},
            {"data": "dep_tipologia"},
            {"data": "dep_piso"},
            {"data": "dep_imagen_portada"},
            {"data": "f_zona.zona_id"},
            {"data": "dep_id"},
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 100px; height: 50px;">';

                }
            },
            {
                targets: [-6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$'+(data);
                }
            },
            {
                targets: [-8],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$'+(data);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Turismo_Real/EditarDepartamento/' + row.dep_id + '/" class="btn btn-primary btn-xs"><i class="fa-solid fa-pen-to-square"></i></a>';
                    buttons += '<a href="/Turismo_Real/EliminarDepartamento/' + row.dep_id + '/" class="btn btn-danger btn-xs"><i class="fa-solid fa-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
