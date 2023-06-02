$(document).ready(function (){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'list_area_conocimiento'
        },
    }).done(function(data){
        let data_table = $('#tableData').DataTable({
            autoWidth: false,
            destroy: true,
            scrollX: true,
            deferRender: true,
            sAjaxDataProp: "",
            data: JSON.parse(data.data),
            columns: [
              { data: 'pk' },
              { data: function(row) { return row.fields.nombre_area; } },
              { data: function(row) { return row.fields.desc_area; } },
              { data: function(row) { return row.fields.cod_area_contenida; } },
              { 
                targets: -1,  // Última columna
                data: null,
                defaultContent: "<button id='btn_delete' type='button' class='btn btn-danger btn-sm delete-button'><i class='fas fa-trash'></i></button>"
              },
            ]
        });

        $('#tableData').on('click', '.delete-button', function() {
            var row = $(this).closest('tr');
            var rowData = data_table.row(row).data();
            Swal.fire({
                title: '¿Estás seguro?',
                text: 'Se eliminará el área permanentemente',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, confirmar'
            }).then((result) => {
                if (result.isConfirmed) {
                    console.log(rowData.pk)
                    deleteRow(rowData.pk)
                }
            })
        });
    })
})

function deleteRow (idRow){
    $.ajax({
        url: window.location.pathname,
        method: 'POST',
        data: {
            'action': 'delete_area_conocimiento',
            'parameters': idRow
        },
    }).done(function(data){
        if (data.type == 'success') {
            Swal.fire({
                title: 'Correcto!',
                text: data.msg,
                icon: 'success'
            })
            setTimeout(function () {
                location.href = window.location.pathname
            }, 1500);
        }else {
            Swal.fire({
                title: 'Error!',
                text: data.msg,
                icon: 'error'
            })
        }
    })
}
