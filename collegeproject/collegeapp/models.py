from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBasicDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    current_address = models.TextField(blank=True)
    permanant_address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.first_name)
    
class OTPDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_number = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
