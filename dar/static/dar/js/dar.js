'use strict';

function listDisciplines(departament_id)
{
    console.log('oi');
    $.ajax({
        url: 'api/disciplines/?departament+id=' + departament_id,
        data: 'departament_id=' + departament_id,
        dataType: 'json',
        success: function(data) {
            console.log(data)
        }
    });
}

