from django.db import models
from django.db.models import Sum
from django.utils.timezone import now

class RevenueManager(models.Manager):
    def daily_revenue(self):
        return self.filter(date=now().date()).aggregate(Sum('revenue_amount'))['revenue_amount__sum'] or 0

    def monthly_revenue(self):
        return self.filter(date__month=now().month, date__year=now().year).aggregate(Sum('revenue_amount'))['revenue_amount__sum'] or 0

    def yearly_revenue(self):
        return self.filter(date__year=now().year).aggregate(Sum('revenue_amount'))['revenue_amount__sum'] or 0

class Revenue(models.Model):
    date = models.DateField()
    revenue_amount = models.DecimalField(max_digits=10, decimal_places=2)
    objects = RevenueManager()

    def __str__(self):
        return f"Revenue on {self.date}"
