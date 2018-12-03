function putStatus(id){

  if (id.split("-")[0]== 'To_Do'){
    id = 'To Do-' + id.split("-")[1];
  }

  $.ajax({
    type: 'PUT',
    url: "tasks/",
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify({"task_id": id.split("-")[1], "status": id.split("-")[0]}),
    success: function(result) {
      
      if (status == 'Doing'){
        $('#anchor-' + result.id).attr("class", "left-align btn dropdown-trigger lime lighten-2");
      }

      else if (status == 'Done'){
        $('#anchor-' + result.id).attr("class", "left-align btn dropdown-trigger green lighten-2");
      }

      else {
        $('#anchor-' + result.id).attr("class", "left-align btn dropdown-trigger red lighten-2");
      }
  },
    error: function(jqxhr, status, exception) {
      console.log("task_id: " + id.split("-")[1].replace("_", " ") + "status: " + id.split("-")[0]);
      alert("task_id: " + id.split("-")[1].replace("_", " ") + "status: " + id.split("-")[0]);
      alert(exception);
    } 
  });
}

function getTasks(jQuery){

    $.ajax({
        type: 'GET',
        url: "tasks/",
        dataType: 'json',
        contentType: 'application/json',
        //data: JSON.stringify({}),
        success: function(result) {
          //alert(jsonData);

          list = $('<ul class="collapsible"></ul>');

          taskList = result.list;

          taskList.forEach(function(element){

              statusList = '<ul id="listStatus" class="dropdown-content left-align">\
              <li><a href="" id="To_Do-' + element.id + '" onclick="putStatus(this.id)">To Do</a></li>\
              <li><a href="" id="Doing-' + element.id + '"onclick="putStatus(this.id)">Doing</a></li>\
              <li><a href="" id="Done-' + element.id + '"onclick="putStatus(this.id)">Done</a></li></ul>';

              if (element.status == 'Doing'){
                inputStatus = $('<a id="anchor-' + element.id + '" class="left-align btn dropdown-trigger lime lighten-2" href="" data-target="listStatus"></a>').append(element.status + '<i class="material-icons">arrow_drop_down</i>');  
              }

              else if (element.status == 'Done'){
                inputStatus = $('<a id="anchor-' + element.id + '" class="left-align btn dropdown-trigger green lighten-2" href="" data-target="listStatus"></a>').append(element.status + '<i class="material-icons">arrow_drop_down</i>');  
              }

              else {
                inputStatus = $('<a id="anchor-' + element.id + '" class="left-align btn dropdown-trigger red lighten-2" href="" data-target="listStatus"></a>').append(element.status + '<i class="material-icons">arrow_drop_down</i>');  
              }
              
              txt = $('<li></li>').append('<div class="collapsible-header"><i class="material-icons">filter_drama</i>' + element.description + ' '
              + '</div>\
              <div class="collapsible-body">\
                <span><h5>Created: </h5>' + element.creation_date.split(" ")[0] + '</span>\
                <span><h5>Due Date: </h5>' + element.due_date.split(" ")[0] + '</span></div>');

              $('#list').append($(list).append(txt));
              txt.attr("id", 'collapsible-' + element.id);

              $('#statusCol').append(statusList);
              $('#statusCol').append(inputStatus);
              inputStatus.attr("id", 'dropdown-' + element.id);

              $('.collapsible').collapsible();
              $('.dropdown-trigger').dropdown();
            });
        },
        error: function(jqxhr, status, exception) {
          alert(exception)
        }
      });
}

$(document).ready(getTasks);
//$(window).on("reload", updateMaterializers);