from django.db import models


class Winemaker(models.Model):
    """
    Stores a single wine maker entry.
    A wine producer does not need to have a relation with a wine bottle.
    """

    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class WineBottle(models.Model):
    """
    Stores a single wine bottle entry, related to :model: winemaker.Winemaker.
    Notes:
        - A wine bottle can only belong to one wine maker.
        - Only some properties set to be required: name, year, size, count_in_winecellar, style.
    """

    STYLE_CHOICES = [  # Basic choices for wine style
        ("dry", "Dry"),
        ("sweet", "Sweet"),
    ]

    winemaker = models.ForeignKey(Winemaker, related_name="wines", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    size = models.CharField(max_length=50)
    count_in_winecellar = models.PositiveIntegerField()
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    taste = models.TextField(help_text="Comma separated, e.g., plum, tobacco", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    food_pairing = models.TextField(help_text="Comma separated, e.g. red meat, cheese", blank=True, null=True)
    link = models.URLField(
        help_text="Unique URL for each wine bottle (could be a link to the wine maker's website)", blank=True, null=True
    )

    # TODO: Support image field
    # image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"
