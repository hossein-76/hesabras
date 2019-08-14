from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class InComeCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'title:{self.title}'


class InCome(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='incomes')
    amount = models.FloatField()
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateField()
    category = models.ForeignKey(
        InComeCategory, on_delete=models.CASCADE, related_name='c_incomes')

    def __str__(self):
        return f'amount:{self.amount}, used in:{self.used_at}'


class OutComeCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'title:{self.title}'


class OutCome(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='outcomes')
    amount = models.FloatField()
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateField()
    category = models.ForeignKey(
        OutComeCategory, on_delete=models.CASCADE, related_name="c_outcomes")

    def __str__(self):
        return f'amount:{self.amount}, used in:{self.used_at}'
