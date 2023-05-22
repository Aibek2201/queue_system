from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices


class Queue(models.Model):
    id = models.AutoField(primary_key=True)
    queue_number = models.CharField(max_length=10, unique=True, blank=True)
    status = models.CharField(
        choices=choices.QueueStatusChoices.choices,
        default=choices.QueueStatusChoices.New,
        blank=True,
        null=False,
        max_length=20,
    )
    user = models.CharField(max_length=20, null=True, blank=True)
    queue_type = models.CharField(
        choices=choices.QueueTypeChoices.choices,
        default=choices.QueueTypeChoices.Other,
        blank=True,
        null=False,
        max_length=20,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Queue')
        verbose_name_plural = _('Queues')

    def save(self, *args, **kwargs):
        if not self.queue_number:
            last_queue = Queue.objects.filter(queue_type=self.queue_type).order_by('-created_at').first()
            if last_queue:
                last_number = last_queue.queue_number.split('-')[-1]
                next_number = str(int(last_number) + 1)
                self.queue_number = f'{self.queue_type[0]}-{next_number}'
            else:
                self.queue_number = f'{self.queue_type[0]}-101'
        super().save(*args, **kwargs)

