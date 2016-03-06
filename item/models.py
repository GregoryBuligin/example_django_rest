# -*- coding: utf-8 -*-
from django.db import models
from category.models import Category
import datetime

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Наименование товара")
    item_price = models.PositiveIntegerField(verbose_name="Цена")
    item_description = models.TextField(blank=True, null=True)
    item_receipt_date = models.DateTimeField(default=datetime.datetime.now, verbose_name="Время поступления")
    item_capture = models.ImageField(upload_to="item/%Y/%m/%d", blank=True, null=True)
    item_category = models.ForeignKey(Category, null=True, related_name='items')

    def __str__(self):
        return "{} -> {}".format(self.item_name, self.item_receipt_date)

    def save(self, *args, **kwargs):
        try:
            this_record = Item.objects.get(id=self.id)
            if this_record.item_capture != self.item_capture:
                this_record.item_capture.delete(seve=False)
        except:
            pass
        super(Item, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.item_capture.delete(save=False)
        super(Item, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['item_name', 'item_receipt_date']
        unique_together = ('item_name', 'item_description', 'item_receipt_date')
