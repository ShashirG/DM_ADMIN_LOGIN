
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.TextField(max_length=255, blank=False)
    last_name = models.TextField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    phone_number = models.IntegerField( blank=False)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    alternate_phonenumber = models.IntegerField( blank=True)
    addressline_one = models.CharField(max_length=100, blank=False)
    addressline_two = models.CharField(max_length=100, blank=True)
    country_or_city = models.TextField(max_length=100,default=True, blank=False)
    postalcode = models.CharField(max_length=100, blank=False)
    company_name = models.TextField(max_length=100, blank=True)
    company_type = models.TextField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=False)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_table"


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

class conn(models.Model):
    connection_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo_name =models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    key_param=JSONField()
    d_type=JSONField()

    class Meta:
        db_table = "conn"



class connection_detail(models.Model):
    tenant_id=models.ForeignKey(tenant_user, on_delete=models.CASCADE,null=True)
    connection_id = models.ForeignKey(conn, on_delete=models.CASCADE,related_name='connection_id')
    # connection_name = models.CharField(max_length=100)
    connection_detail = models.CharField(max_length=100)
    con_str=JSONField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    last_modified_by = models.CharField(max_length=100,null=True)
    last_modified_on = models.DateField(auto_now=True,null=True)
    created_on= models.DateField(auto_now=True,null=True)
    created_by= models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'connection_detail'




