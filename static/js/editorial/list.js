$(document).ready(function (){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'list_editorial'
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
              { data: function(row) { return row.fields.nombre_editorial; } },
              { data: function(row) { return row.fields.pagina_web; } },
              { data: function(row) { return row.fields.pais_origen; } },
              { data: function(row) { return row.fields.pais_origen; } },
            ],
            columnDefs:[
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = `<a href="/app/editorial/update/${row.pk}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                        <a href="/app/editorial/delete/${row.pk}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                        return buttons;
                    }
                },
            ]
        });
    })
})