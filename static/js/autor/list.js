$(document).ready(function (){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'list_autores'
        },
    }).done(function(data){
        console.log(data)
        let data_table = $('#tableData').DataTable({
            autoWidth: false,
            destroy: true,
            scrollX: true,
            deferRender: true,
            sAjaxDataProp: "",
            data: JSON.parse(data.data),
            columns: [
              { data: 'pk' },
              { data: function(row) { return row.fields.primer_nombre; } },
              { data: function(row) { return row.fields.segundo_nombre; } },
              { data: function(row) { return row.fields.primer_apellido; } },
              { data: function(row) { return row.fields.segundo_apellido; } },
              { data: function(row) { return row.fields.segundo_apellido; } },
            ],
            columnDefs:[
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = `<a href="/app/autores/update/${row.pk}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                       <a href="/app/autores/delete/${row.pk}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                        return buttons;
                    }
                },
            ]
        });
    })
})
