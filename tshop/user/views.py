from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from .models import Customer


# TODO: Add comments
def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    message = _('Emtpy message!')
    error = False
    if request.method == 'POST':
        try:
            user = Customer.objects.get(email=email)
        except Exception:
            try:
                user = Customer(username=email, email=email, password=password, is_active=False)
                user.generate_activation_code()

            except Exception:
                error = True
                message = _('Cannot create account! Call to technical support.')
            else:
                if user:
                    subject = _('Activation code')
                    from_email = 'timofey.samodurov@mail.ru'
                    to = email
                    html_content = render_to_string('user/mail_activation_code.html', {'shop': 'http://localhost:8000',
                                                                                       'act_code': user.act_code})
                    text_content = strip_tags(html_content)

                    try:
                        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                    except Exception:
                        message = _('Cannot send activation link. Call to technical support!')
                        error = True
                    else:
                        error = False
                        message = _('Activation link has been sent to ') + str(email) + '!'
                        user.save()
        else:
            error = True
            message = _('User already exist! Try another email.')

    else:
        error = True
        message = _('Something wrong!')

    return render(request, template_name='user/registration_alert.html',
                  context={'error': error, 'alert_message': message})


# TODO: Redirect to the main page with activation message
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
            return HttpResponse("Activation is successfully!")
