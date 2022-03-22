from django.db import models
import uuid

# User
class User(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#uuidfield
    user_id = models.UUIDField(
        'user_id',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#datefield
    date_birth = models.DateField(auto_now=False, auto_now_add=False)

    SEX_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    )
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)

    primary_care_provider = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# User Role
class Role(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('NURSE', 'Nurse'),
        ('DOCTOR', 'Doctor'),
        ('ADMIN', 'Admin'),
        ('FAMILY', 'Family'),
        ('OTHER', 'Other')
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    status = models.BooleanField()
    time_status = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.role

# User Measurements
class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    blood_pressure = models.CharField(max_length=60)
    glucose = models.FloatField()
    cholesterol = models.FloatField()
    iron = models.FloatField()
    pulse = models.FloatField()
    blood_oxygen = models.FloatField()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.role

# User History
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    family_history = models.CharField(max_length=300)
    medical_history = models.CharField(max_length=300)
    medications = models.CharField(max_length=300)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.role

# User Billing
class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=60)
    insurance_address = models.CharField(max_length=60)
    member_id = models.CharField(max_length=60)
    group_num = models.CharField(max_length=60)
    insurance_plan_name = models.CharField(max_length=60)
    insurance_plan_type = models.CharField(max_length=60)
    holder_name = models.CharField(max_length=60)
    holder_relation = models.CharField(max_length=60)
    credit_card_num = models.CharField(max_length=60)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.role