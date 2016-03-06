# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=50, db_index=True)
    category_discription = models.TextField(blank=True)
    category_capture = models.ImageField(upload_to="category/")

    def __str__(self):
        return "{}".format(self.category_title)

    def save(self, *args, **kwargs):
        try:
            this_record = Category.objects.get(id=self.id)
            if this_record.category_capture != self.category_capture:
                this_record.category_capture.delete(seve=False)
        except:
            pass
        super(Category, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.category_capture.delete(save=False)
        super(Category, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category_title']
        unique_together = ('category_title', 'category_discription', 'category_capture')
