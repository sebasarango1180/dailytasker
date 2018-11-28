function getTasks(){

    $.ajax({
        type: 'GET',
        url: "/tasks/list",
        dataType: 'jsonp',
        success: function(jsonData) {
          //alert(jsonData);

          list = $('<ul></ul>');
          task_list = jsonData.list;

          task_list.forEach(element => {
              if (element.status == 'to do'){
                tag = txt = '<div class="chip">' + element.status + '</div>';
              }
              else if (element.status == 'in process'){
                tag = '<div class="chip">' + element.status + '</div>';
              }
              else if (element.status == 'done'){
                tag = '<div class="chip">' + element.status + '</div>';
              }

              txt = '<li class="collection-item">' + element.description + '</li>'
              task = $(txt).appendChild(tag);
              $('#list').appendChild(task);
              task.setAttribute('id', str(element.id));
          });
        },
        error: function() {
          alert('Error loading');
        }
      });
    
}