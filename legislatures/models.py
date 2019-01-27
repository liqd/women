from django.db import models

class Legislature(models.Model):
    name = models.CharField(max_length=200)
    start_data = models.DateField(blank=True, null=True)
    end_data = models.DateField(blank=True, null=True)
    year = models.IntegerField()
    percentage = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name
