from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, first_name=None, last_name=None, national_code=None,email=None):
        if phone_number:
            user = self.model(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                national_code=national_code,
                email=email
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, phone_number, password=None, first_name=None, last_name=None, national_code=None,email=None):
        user = self.create_user(phone_number, password, first_name, last_name, national_code,email)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
