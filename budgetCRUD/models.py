from django.db import models

# Create your models here.

# this is a test message
class user(models.Model):
    user_id = models.CharField(max_length=2, unique = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return(self.first_name + " " + self.last_name)

class transaction(models.Model):
    transaction_id = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    category_id = models.ForeignKey(user,max_length=30,
                                verbose_name="User",
                                on_delete=models.DO_NOTHING, )
    description = models.CharField(max_length=30)
    user_id = models.ForeignKey(user,max_length=30,
                                verbose_name="User",
                                on_delete=models.DO_NOTHING, )
 
class budget(models.Model):
    budget_number = models.CharField(max_length=30)
    housing_goal = models.CharField(max_length=30)
    trasportaion_goal = models.CharField(max_length=30)
    food_goal = models.CharField(max_length=30)
    utilities_goal = models.CharField(max_length=30)
    insurance_goal = models.CharField(max_length=30)
    savings_goal = models.CharField(max_length=30)
    investing_goal = models.CharField(max_length=30)
    recreation_goal = models.CharField(max_length=30)
    user_id = models.ForeignKey(user,max_length=30,
                                verbose_name="User",
                                on_delete=models.DO_NOTHING, )

    
