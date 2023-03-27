from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You need to complete an email field')
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_confirmed = True
        user.save(using=self._db)
