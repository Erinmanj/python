from django.db import models



class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)

    class Meta:
        db_table = 'speciality'

    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)  
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='doctor')  
    phone_no = models.BigIntegerField()  

    class Meta:
        db_table = 'doctor'  
     
    def __str__(self):
        return self.name


class DetailsofPatient(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255,null=True)
    middlename = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=255,null=True)
    dob = models.DateField()  
    age = models.PositiveIntegerField()
    maritalst = models.CharField(max_length=255,null=True)
    maidenname = models.CharField(max_length=255,null=True)
    flatno = models.BigIntegerField(null=True)
    country = models.CharField(max_length=255,null=True)
    ct = models.CharField(max_length=255,null=True)
    otherlocality = models.CharField(max_length=255, null=True)
    pin = models.BigIntegerField(null=True)
    state = models.CharField(max_length=255, null=True)
    locality = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255)  
    tele = models.BigIntegerField(null=True)
    mobile = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'DetailsofPatient'






class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescription')
    patient  = models.ForeignKey(DetailsofPatient, on_delete=models.CASCADE, related_name= 'prescription', null=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='prescription', null=True)
    date = models.DateField(null=True)
    image = models.TextField(max_length=50, null=True, blank=True)


    class Meta:
        db_table = 'prescription'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=200,null=True)
    date = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment')
    patient = models.ForeignKey(DetailsofPatient, on_delete=models.CASCADE, related_name='appointment')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name= 'appointment')
    

    class Meta:
        db_table = 'appointment'

    def __str__(self):
        return "Appointment {self.id} on {self.date} from {self.start_time} to {self.end_time}"

class Bill(models.Model):
    id = models.AutoField(primary_key=True)  
    number = models.CharField(max_length=255)  
    date = models.DateField()  
    image = models.TextField(max_length=50, null=True, blank=True)
 

    class Meta:
        db_table = 'bill'


class Reciept(models.Model):
    id = models.AutoField(primary_key=True)  
    number = models.CharField(max_length=255)  
    date = models.DateField()  
    image = models.TextField(max_length=50, null=True, blank=True)
 

    class Meta:
        db_table = 'reciept'


class Report(models.Model):
    id = models.AutoField(primary_key=True)  
    number = models.CharField(max_length=255)  
    name=models.CharField(max_length=255)
    date = models.DateField()  
    image = models.TextField(max_length=50, null=True, blank=True)

 

    class Meta:
        db_table = 'report'


