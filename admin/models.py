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
            choices=(
                (YES, 'YES'),
                (NO, 'NO'),
            ),
            default=NO
        )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_add=True)


    def __str__(self):
          return     

    def __unicode__(self):
        return 
