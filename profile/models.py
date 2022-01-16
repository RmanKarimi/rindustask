from django.db import models
import uuid
from utils.utils import validate_iban
from django.contrib.auth import get_user_model

# getting User Model
User_model = get_user_model()

class DataModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    # objects = DataModelManager()

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.pk)


class UserDataModel(DataModel):
    """Abstract for user model"""
    user = models.ForeignKey(
        User_model,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name='User'
    )

    class Meta:
        abstract = True


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Profile(UUIDPrimaryKeyMixin, UserDataModel):
    first_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Last Name')
    IBAN = models.CharField(max_length=26, null=True, blank=True, validators=[validate_iban],
                            verbose_name='IBAN Number')

    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
