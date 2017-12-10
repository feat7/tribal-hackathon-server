from django.db import models

# Create your models here.
class Scheme(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    used_amount = models.FloatField()
    allocated_amount = models.FloatField()
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Place(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)

    population = models.ForeignKey(
        'Population',
        on_delete=models.CASCADE,
        default=0
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20)
    upper_node=models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    		return self.name + " "+ self.type

class Population(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)
    total_population = models.BigIntegerField()
    tribal_population = models.BigIntegerField()
    tribal_population_percent = models.IntegerField()
    
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Allocation(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)
    scheme = models.ForeignKey(
        'Scheme',
        on_delete=models.CASCADE
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE
    )
    description = models.TextField()
    allocated_amount = models.BigIntegerField()
    used_amount = models.BigIntegerField()
    
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Complaint(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    allocation = models.ForeignKey(
        'Allocation',
        on_delete=models.CASCADE
    )
    
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Announcement(models.Model):
    YES = 'YES'
    NO = 'NO'
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()    
    
    status = models.CharField(
        max_length=20,
        choices=(
            (YES, 'YES'),
            (NO, 'NO'),
        ),
        default=NO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return     

    def __unicode__(self):
        return 
