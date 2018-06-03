
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
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  return emailReg.test( $email );
}

$(".modal").on('click','#btn_register', function(){
    if (validateEmail($('#email').val()))
        {
    modal_dialog = $(".modal-dialog").html();
    $.ajax(
            {
            type: "POST",
            url: "/user/register",
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
