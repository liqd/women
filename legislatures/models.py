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
    seats = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (self.name + ' - ' + str(self.year))


class ParliamentaryGroup(models.Model):
    CDU = 'CDU'
    SPD = 'SPD'
    FDP = 'FDP'
    GRUEN = 'GRU'
    LINKE = 'LIN'
    AFD = 'AFD'
    GROUP_CHOICES = (
        (CDU, 'CDU/CSU'),
        (SPD, 'SPD'),
        (FDP, 'FDP'),
        (GRUEN, 'B\'90/die Grünen, früher: Grüne'),
        (LINKE, 'Linke, früher: PDS'),
        (AFD, 'AfD')
    )

    legislature = models.ForeignKey('Legislature', on_delete=models.CASCADE)
    group = models.CharField(
        max_length=3,
        choices=GROUP_CHOICES
    )
    colour_code = models.CharField(max_length=8)
    percentage_women = models.DecimalField(decimal_places=2, max_digits=4)
    number_women = models.IntegerField(blank=True, null=True)
    percentage_group = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    number_group = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (self.legislature.name + ' - ' + str(self.legislature.year) + ' - ' + self.get_group_display())
