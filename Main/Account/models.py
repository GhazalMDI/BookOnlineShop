from django.db import models

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from Account.manager import UserManager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=35, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_lable):
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def is_staff(self):
        return self.is_admin

    @property
    def full_name(self):
        if self.first_name:
            return f'{self.first_name} عزیز '
        if self.last_name:
            return f'{self.last_name} عزیز '
        if self.last_name and self.first_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return 'کاربر عزیز'