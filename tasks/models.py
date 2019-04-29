from django.db import models

class Task(models.Model):
    STATUS = (
        ('doing','Realizada'),
        ('done', 'Não Realizada'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=20, choices= STATUS,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
