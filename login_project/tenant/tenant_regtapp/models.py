
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.fields import JSONField
try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin


class tenant_user(AbstractBaseUser):

    email = models.EmailField(max_length=255 ,unique=True ,blank=False)
    phone_number = models.CharField(max_length=15 ,blank=False)
    password = models.CharField(max_length=255 ,blank=False)
    address= models.CharField(max_length=100 ,blank=False)
    country = models.CharField(max_length=100 ,blank=False)
    city = models.CharField(max_length=100 ,blank=False)
    postalcode = models.CharField(max_length=100 ,blank=False)
    company_name = models.CharField(max_length=100 ,blank=True)
    company_reg_no = models.CharField(max_length=100 ,blank=True)
    company_pan_no = models.CharField(max_length=100 ,blank=True)
    tenant_id = models.CharField(max_length=100)
    role =models.CharField(max_length=100 ,blank=False)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.tenant_id

    class Meta:
        db_table = "tenantregister"