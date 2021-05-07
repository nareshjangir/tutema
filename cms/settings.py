from django.db import models
from django.utils.translation import gettext_lazy as _


class Kakshayein(models.TextChoices):
    NINTH = 'Class - IX', _('9th')
    TENTH = 'Class - X', _('10th')
