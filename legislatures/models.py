from django.db import models

class Legislature(models.Model):
    WEIMAR = 'WE'
    NS_ZEIT = 'NS'
    VOLKSKAMMER = 'VK'
    BUNDESTAG = 'BT'
    POLITICAL_SYSTEM_CHOICES = (
        (WEIMAR, 'Weimarer Republik'),
        (NS_ZEIT, 'Zeit des Nationalsozialismus'),
        (VOLKSKAMMER, 'Volkskammer der DDR'),
        (BUNDESTAG, 'Deutscher Bundestag'),
    )

    name = models.CharField(max_length=200)
    start_data = models.DateField(blank=True, null=True)
    end_data = models.DateField(blank=True, null=True)
    year = models.IntegerField()
    percentage = models.DecimalField(decimal_places=2, max_digits=4)
    system = models.CharField(
        max_length=2,
        choices=POLITICAL_SYSTEM_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.name
