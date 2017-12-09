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
        default=0
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

        name = models.CharField(max_length=200)
        total_population = models.BigIntegerField()
        tribal_population = models.BigIntegerField()
        percent_tribal_population = models.IntegerField()
        
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
