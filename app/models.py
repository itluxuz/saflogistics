from django.db import models



class Order(models.Model):
    title = models.CharField(max_length=150)
    product_id = models.CharField(max_length=150)
        


    def __str__(self):
        return str(self.title)


class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=128, blank=True, null=True)
    date_status = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.order.title}: {self.status}"