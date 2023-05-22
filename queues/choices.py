from django.db import models


class QueueStatusChoices(models.TextChoices):
    New = 'Кезектер тізімінде'
    ProcessInProgress = 'Қызмет көрсетілуде'
    End = 'Қызмет аяқталды'


class QueueTypeChoices(models.TextChoices):
    Grant = 'Грант'
    Budget = 'Ақылы'
    Other = 'Басқа'

