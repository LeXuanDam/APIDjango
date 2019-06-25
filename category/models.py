from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

class Category(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s %s" % (self.name)
