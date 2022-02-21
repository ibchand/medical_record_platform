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

# # User Measurements
# class user(models.Model):
#     userid = models.CharField(max_length=60)
#     height = models.CharField(max_length=60)
#     weight = models.CharField(max_length=60)
#     blood_pressure = models.CharField(max_length=60)
#     glucose = models.CharField(max_length=60)
#     cholesterol = models.CharField(max_length=60)
#     iron = models.CharField(max_length=60)
#     pulse = models.CharField(max_length=60)
#     blood_oxygen = models.CharField(max_length=60)


#     def __str__(self):
#         return self.name

# # User History
# class user(models.Model):
#     userid = models.CharField(max_length=60)
#     family_history = models.CharField(max_length=60)
#     medical_history = models.CharField(max_length=60)
#     medications = models.CharField(max_length=60)

#     def __str__(self):
#         return self.name

# # User Billing
# class user(models.Model):
#     userid = models.CharField(max_length=60)
#     billing_address = models.CharField(max_length=60)
#     insurance_address = models.CharField(max_length=60)
#     member_id = models.CharField(max_length=60)
#     group_num = models.CharField(max_length=60)
#     insurance_plan_name = models.CharField(max_length=60)
#     insurance_plan_type = models.CharField(max_length=60)
#     holder_name = models.CharField(max_length=60)
#     holder_relation = models.CharField(max_length=60)
#     credit_card_num = models.CharField(max_length=60)

#     def __str__(self):
#         return self.name
