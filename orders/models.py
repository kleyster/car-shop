from django.db import models


class ProductApplications(models.Model):

    phone_number = models.CharField(max_length=14)
    # email = models.EmailField()
    full_name = models.CharField(max_length=150)
    comment = models.TextField()
    city = models.CharField(max_length=50)
    product = models.ForeignKey("products.Products", related_name="applications", on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey("_auth.Company", related_name="applications", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
