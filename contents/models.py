from django.db import models


class Product(models.Model):

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=256)
    description = models.BooleanField(null=True, default=False, verbose_name='Está ativo')
    is_active = models.BooleanField(null=True, default=False, verbose_name='Está ativo')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Image(models.Model):

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
    )
    original = models.ImageField(
        upload_to='productsImages/original',
        null=True,
        blank=True
    )
    medium = models.ImageField(
        upload_to='productsImages/medium',
        null=True,
        blank=True
    )
    small = models.ImageField(
        upload_to='productsImages/small',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)


class Order(models.Model):

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    product = models.ManyToManyField(Product, verbose_name='produtos')
    amount = models.IntegerField()
    date_time = models.DateTimeField()
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

