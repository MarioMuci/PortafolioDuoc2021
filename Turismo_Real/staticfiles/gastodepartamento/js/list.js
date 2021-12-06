var tblDetaDepa;

function format(d) {
    console.log(d);
    var html = '<table class="table table-bordered">';
    html += '<thead class="thead-light">';
    html += '<tr><th scope="col">Departamento</th>';
    html += '<th scope="col">Costo Mensual</th>';
    html += '<th scope="col">Cantidad</th>';
    html += '<th scope="col">Subtotal</th>';
    html += '</thead>';
    html += '<tbody>';
    $.each(d.det, function (key, value) {
        html+='<tr>'
        html+='<td>'+value.dep.dep_nombre+'</td>'
        html+='<td>'+value.cos_mensual+'</td>'
        html+='<td>'+value.cos_cant+'</td>'
        html+='<td>'+value.cos_subtotal+'</td>'
        html+='</tr>';
    });
    html += '</tbody>';
    return html;
}

$(function () {
    tblDetaDepa = $('#data').DataTable({
        scrollX: true,
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
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "des_cos_fecha_ingreso"},
            {"data": "pf_fun.fun_nombre"},
            {"data": "des_cos_dep_dia"},
            {"data": "des_cos_dep_semanal"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [3, 4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$' + (data);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Turismo_Real/EliminarDepartamento/' + row.id + '/" class="btn btn-danger btn-xs"><i class="fa-solid fa-trash"></i></a>';
                    buttons += '<a href="/Turismo_Real/EditarDetalleCostoDepartamento/' + row.id + '/" class="btn btn-warning btn-xs"><i class="fa-solid fa-edit"></i></a>';
                    buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

   $('#data tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblDetaDepa.cell($(this).closest('td, li')).index();
            var data = tblDetaDepa.row(tr.row).data();
            console.log(data);

            $('#tblCos').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_depto',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "dep.dep_nombre"},
                    {"data": "cos_mensual"},
                    {"data": "cos_cant"},
                    {"data": "cos_subtotal"},
                ],
                columnDefs: [
                    {
                        targets: [1, 3],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return '$' + (data);
                        }
                    },
                    {
                        targets: [2],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelcos').modal('show');
        })
        .on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = tblDetaDepa.row(tr);
            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                tr.addClass('shown');
            }
        });
});
