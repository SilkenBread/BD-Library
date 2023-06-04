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
              { data: function(row) { return row.fields.cod_area_contenida; } },
            ],
            columnDefs:[
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = `<a href="/app/area_conocimiento/update/${row.pk}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                       <a href="/app/area_conocimiento/delete/${row.pk}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                        return buttons;
                    }
                },
            ]
        });
    })
})
