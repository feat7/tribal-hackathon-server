from django.db import models

# Create your models here.
class Scheme(models.Model):
    YES = 'YES'
    NO = 'NO'

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

    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20)
    upper_node=models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        default=0,
        blank=True,
        null=True
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

class Population(models.Model):
    YES = 'YES'
    NO = 'NO'

    place_id = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
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

    scheme_id = models.ForeignKey(
        'Scheme',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    place_id = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    population_id = models.ForeignKey(
        'Population',
        on_delete=models.CASCADE,
        blank=True,
        null=True
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

    name = models.CharField(max_length=50)
    description = models.TextField()
    allocation_id = models.ForeignKey(
        'Allocation',
        on_delete=models.CASCADE,
        blank=True,
        null=True
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
