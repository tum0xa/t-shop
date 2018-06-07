from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Customer

#TODO Add comments
def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        try:
            user = Customer.objects.get(email=email)
        except Exception:

            try:
                user = Customer(username=email, email=email, password=password, is_active=False)
                user.generate_activation_code()

            except Exception:
                html = '<div class="alert alert-danger" role="alert"><i class="fa fa-check-circle-o"></i>Something wrong! </div>'
            else:
                if user:
                    html_message = '<div style="padding: .75rem 1.25rem; margin-bottom: 1rem; ' \
                           'border: 1px solid transparent; border-radius: .25rem;' \
                           'background-color: #dff0d8; border-color: #d0e9c6; color: #3c763d;">' \
                      '<strong>Well done!</strong> Your activation code: ' \
                      '<a href="http://localhost:8000/user/activate/?act_code='+user.act_code+'" ' \
                      'class="alert-link">'+user.act_code+'</a>.</div>'
                    try:
                        send_mail(subject="Activation", from_email='timofey.samodurov@mail.ru', recipient_list=(email,),
                          auth_password="Su0vSvorliaM1609!", message='message', html_message=html_message, auth_user='timofey.samodurov')
                    except Exception:
                        html = '<div class="alert alert-danger" role="alert"><i class="fa fa-check-circle-o"></i>Something wrong! </div>'
                    else:
                        html = '<div class="alert alert-success" role="alert"><i class="fa fa-check-circle-o"></i>The message with ' \
                       'registration data has been sent to ' + str(email) + '!</div>'
                        user.save()
        else:
            html = '<div class="alert alert-danger" role="alert"><i class="fa fa-check-circle-o"></i>User exist!</div>'
    else:
        html = '<div class="alert alert-danger" role="alert"><i class="fa fa-check-circle-o"></i>Something wrong! </div>'

    return HttpResponse(html)


def activate(request):
    code = request.GET.get('act_code')
    print(request.GET)
    print(code)
    try:
        user = Customer.objects.get(act_code=code)
    except:
        return HttpResponse("Activation code is invalid!")
    else:
        if user.is_active:
            return HttpResponse("Activation code is not actual!")
        else:
            user.is_active = True
            user.save()
            return HttpResponse("Activation is successufully!")
