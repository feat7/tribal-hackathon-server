from django.db import models

# Create your models here.
class Department(models.Model):
    YES = 'YES'
    NO = 'NO'

    name = models.CharField(max_length=200)
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
        return  self.name   

    def __unicode__(self):
        return self.name

class Scheme(models.Model):
    YES = 'YES'
    NO = 'NO'

    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        default=0,
        related_name='Scheme'
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    used_amount = models.FloatField()
    allocated_amount = models.FloatField()
    likes = models.IntegerField(default=0)
    dis_likes = models.IntegerField(default=0)
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
        return  self.name   

    def __unicode__(self):
        return self.name

class Place(models.Model):
    YES = 'YES'
    NO = 'NO'

    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20)
    upper_node=models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    population=models.ForeignKey(
        'Population',
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

    def __str__(self):
        return  self.name+ " - "+ self.type 

    def __unicode__(self):
        return  self.name+ " - "+ self.type 

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

    scheme = models.ForeignKey(
        'Scheme',
        on_delete=models.CASCADE
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
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

    def __str__(self):
        return  self.scheme.name+ " - "+self.place.name   

    def __unicode__(self):
        return  self.scheme.name+ " - "+self.place.name

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
        return  self.name   

    def __unicode__(self):
        return self.name
