from django.db import models

# User Role
class user(models.Model):
    userid = models.CharField(max_length=60)


    def __str__(self):
        return self.name

# User Info
class user(models.Model):
    id = models.UUIDField('UID', primary_key = True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    date_birth = models.CharField(max_length=60)
    sex = models.CharField(max_length=60)    
    primary_care_provider = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# User Measurements
class user(models.Model):
    userid = models.CharField(max_length=60)
    height = models.CharField(max_length=60)
    weight = models.CharField(max_length=60)
    blood_pressure = models.CharField(max_length=60)
    glucose = models.CharField(max_length=60)
    cholesterol = models.CharField(max_length=60)
    iron = models.CharField(max_length=60)
    pulse = models.CharField(max_length=60)
    blood_oxygen = models.CharField(max_length=60)


    def __str__(self):
        return self.name

# User History
class user(models.Model):
    userid = models.CharField(max_length=60)
    family_history = models.CharField(max_length=60)
    medical_history = models.CharField(max_length=60)
    medications = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# User Billing
class user(models.Model):
    userid = models.CharField(max_length=60)
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
        return self.name
