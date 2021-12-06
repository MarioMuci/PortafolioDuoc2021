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
            {"data": "id"},
            {"data": "rut"},
            {"data": "first_name"},
            {"data": "apellido_paterno"},
            {"data": "apellido_materno"},
            {"data": "username"},
            {"data": "email"},
            {"data": "date_joined"},
            {"data": "groups"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.groups, function (key, value) {
                        html += '<span class="badge bg-success">' + value.name + '</span> ';
                    });
                    return html;
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/EditarUsuario/' + row.id + '/" class="btn btn-primary btn-xs"><i class="fa-solid fa-pen-to-square"></i></a>';
                    buttons += '<a href="/user/EliminarUsuario/' + row.id + '/" class="btn btn-danger btn-xs"><i class="fa-solid fa-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});