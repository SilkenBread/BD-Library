$(document).ready(function (){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'list_libro'
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
              { data: function(row) { return row.fields.titulo; } },
              { data: function(row) { return row.fields.anio_publicacion; } },
              { data: function(row) { return row.fields.numero_pagina; } },
              { data: function(row) { return row.fields.codigo_area; } },
              { data: function(row) { return row.fields.codigo_editorial; } },
              { data: function(row) { return row.fields.codigo_editorial; } },
            ],
            columnDefs:[
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = `<a href="/app/libro/update/${row.pk}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                       <a href="/app/libro/delete/${row.pk}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                        return buttons;
                    }
                },
            ]
        });
    })
})
