var tblFuncionario;
function getData() {

    tblFuncionario = $('#data').DataTable({
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
            {"data": "fun_id"},
            {"data": "fun_rut"},
            {"data": "fun_nombre"},
            {"data": "fun_apellido_paterno"},
            {"data": "fun_apellido_materno"},
            {"data": "f_car.car_nombre"},
            {"data": "fun_id"},
        ],
        columnDefs: [
            {
                targets: [6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-primary btn-xs"><i class="fa-solid fa-pen-to-square"></i></a> ';
                    buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger btn-xs"><i class="fa-solid fa-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {

    modal_title = $('.modal-title');
    
    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un Funcionario');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#MyModalFuncionario').modal('show');
    });

    $('#data tbody')
        .on('click', 'a[rel="edit"]', function () {
            modal_title.find('span').html('Editar un Funcionario');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblFuncionario.cell($(this).closest('td, li')).index();
            var data = tblFuncionario.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="fun_id"]').val(data.fun_id);
            $('input[name="fun_rut"]').val(data.fun_rut);
            $('input[name="fun_nombre"]').val(data.fun_nombre);
            $('input[name="fun_apellido_paterno"]').val(data.fun_apellido_paterno);
            $('input[name="fun_apellido_materno"]').val(data.fun_apellido_materno);
            $('select[name="f_car"]').val(data.f_car);
            $('#MyModalFuncionario').modal('show');
        })
        .on('click', 'a[rel="delete"]', function () {
            var tr = tblFuncionario.cell($(this).closest('td, li')).index();
            var data = tblFuncionario.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('fun_id', data.fun_id);
        submit_whit_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de eliminar el siguiente registro?', parameters, function () {
            tblFuncionario.ajax.reload();
        });
        });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);

        submit_whit_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de guardar el siguiente registro?', parameters, function () {
            $('#MyModalFuncionario').modal('hide');
            tblFuncionario.ajax.reload();
        });
    }); 
});