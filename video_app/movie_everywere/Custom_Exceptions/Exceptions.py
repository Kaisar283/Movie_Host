from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class GanreNotFound(APIException):
    status_code = 700
    default_detail = _('Incorrect type of genres.')
    default_code = 'Process search genre failed'
