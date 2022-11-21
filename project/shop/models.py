from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()

    def display_price(self) -> float:
        return self.price/100

    def display_title(self) -> str:
        return f"Item name - {self.name}"

    def __str__(self):
        return self.display_title()
