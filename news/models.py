from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Follow(models.Model):
    from_user = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name="following")
    to_user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="followers")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.from_user} => {self.to_user}"
