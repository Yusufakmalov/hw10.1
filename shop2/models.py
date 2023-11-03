from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='shop2')
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shop2'


class FormModel(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return str(self.pk)



    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'


