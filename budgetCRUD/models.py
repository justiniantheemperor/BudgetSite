from django.db import models

# Create your models here.

class Spending_Category(models.Model):
    category_id = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=20)

    class Meta:
        db_table = 'grade_level'

    def __str__(self) :
        return (self.description)

