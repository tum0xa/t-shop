
/* Functions for registration modal window */

var csrf_token = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
});

function validateEmail($email) {
  var emailReg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailReg.test( $email );
}

function validatePassword($password) {
  var passwordReg = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,20}$/;
  return passwordReg.test( $password );
}
/* Send to the server a new user's email */
$(".modal").on('click','#btn_register', function(){
    if (validateEmail($('#email').val()) && validatePassword($('#password').val()))
        {
    modal_dialog = $(".modal-dialog").html();
    $.ajax(
            {
            method: "POST",
            url: "/user/register",
            data: {
            "email": $("#email").val(),
            "password": $("#password").val(),
            },
            success: function(result){
                    $(".modal-body").html(result);
                    $(".btn-secondary").html("OK");
                    $(".btn-primary").hide();
                    }});
    return false;
    }});

$(".modal").on('click','.btn-secondary', function(){
    $("#register").modal('hide');

    $(".modal-dialog").html(modal_dialog);
    return false;

});
