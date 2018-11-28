

function checkCredentials(){
    $.post("localhost:5000/auth/login", { json_string:JSON.stringify({user: $('#user').val(), password:$('#password').val()}) })}