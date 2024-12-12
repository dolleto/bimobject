from django.db import models


class Winemaker(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class WineBottle(models.Model):
    STYLE_CHOICES = [
        ("dry", "Dry"),
        ("sweet", "Sweet"),
    ]

    winemaker = models.ForeignKey(Winemaker, related_name="wines", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    size = models.CharField(max_length=50)
    count_in_winecellar = models.PositiveIntegerField()
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    taste = models.TextField(help_text="Comma separated, e.g., plum, tobacco")
    description = models.TextField()
    food_pairing = models.TextField()
    link = models.URLField(blank=True, null=True)
    # TODO: Support image field
    # image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"
