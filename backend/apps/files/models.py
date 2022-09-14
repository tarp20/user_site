from django.db import models

from core.models import BaseModel


class File(BaseModel):
    title = models.CharField(max_length=100, default='No Title')
    file = models.FileField(upload_to='files')

    def __str__(self) -> str:
        return self.title

