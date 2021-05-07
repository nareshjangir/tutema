from django.db import models
from django.utils.translation import gettext_lazy as _


class QuestionType(models.TextChoices):
    NOUN_TYPE = 'Single noun answer', _('Answer in single word(noun)')
    SET_OF_NOUNS = 'More than one noun answer', _('Answer in multiple word(noun)')
    TIME_UNIT = 'Time unit answer', _('Answer in time units')
    YES_NO = 'Yes No type answer', _('Answer either yes or no')
    ONE_WORD_FILL_BLANK = 'Fill 1 word in the blank', _('Fill single word in the blank')
    SET_WORD_FILL_BLANK = 'Fill set of words in the blank', _('Fill set of words in the blank')
    TRUE_FALSE = 'True False type answer', _('Answer either True or False')
