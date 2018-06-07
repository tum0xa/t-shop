import random

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Customer(User):
    """
    Customer
    """
    act_code = models.CharField(_('act_code'), default='_', max_length=255)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
    pass

    def generate_activation_code(self):
        code = ''
        for pos in range(0,25):
            code += chr(random.randint(48,122))
        self.act_code = code
