from django.contrib.auth import get_user_model
from django.db import models
#
# from ..users.models import CustomUser
#
User = get_user_model()


class DownloadFiles(models.Model):
    file_name = models.CharField(
        max_length=200,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author_download',
        verbose_name='Автор закачки'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self):
        return self.file_name
