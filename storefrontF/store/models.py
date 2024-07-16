from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product_set reply all item that discount applyd to


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promotion = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)


class Adress(models.Model):
    # zip = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    PEYMENT_STATUS_PENDING = 'P'
    PEYMENT_STATUS_COMPLETE = 'C'
    PEYMENT_STATUS_FAILD = 'F'
    PEYMENT_STATUS = [
        (PEYMENT_STATUS_PENDING, "Pending"),
        (PEYMENT_STATUS_COMPLETE, "Complete"),
        (PEYMENT_STATUS_FAILD, "Failed")
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PEYMENT_STATUS, default=PEYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
