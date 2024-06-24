from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShipmentHistory(models.Model):
    bill_to_account = models.CharField(max_length=50)
    contents = models.CharField(max_length=255)
    destination_airport_code = models.CharField(max_length=10)
    facility_id = models.CharField(max_length=10)
    licence_plate_no = models.CharField(max_length=50)
    outbound_mail_sort_code = models.CharField(max_length=10)
    plt = models.BooleanField()
    product_abbreviation = models.CharField(max_length=10)
    receiver_address_1 = models.CharField(max_length=255, blank=True, null=True)
    receiver_address_2 = models.CharField(max_length=255, blank=True, null=True)
    receiver_address_3 = models.CharField(max_length=255, blank=True, null=True)
    reciever_attention = models.CharField(max_length=50, blank=True, null=True)
    receiver_business_name = models.CharField(max_length=255, blank=True, null=True)
    receiver_city = models.CharField(max_length=50, null=True)
    reciever_company_name = models.CharField(max_length=255, null=True)
    receiver_country = models.CharField(max_length=50, null=True)
    reciever_country_code = models.CharField(max_length=10, null=True)
    receiver_name = models.CharField(max_length=50, null=True)
    receiver_phone = models.CharField(max_length=50, blank=True, null=True)
    receiver_postcode_zip = models.CharField(max_length=20, blank=True, null=True)
    reciever_telephone = models.CharField(max_length=50, blank=True, null=True)
    shipment_date = models.DateField()
    shipment_declared_value = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_id = models.CharField(max_length=50)
    shipment_pieces = models.IntegerField()
    shipment_reference = models.CharField(max_length=50)
    shipment_weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipper_account_number = models.CharField(max_length=50)
    shipper_address_1 = models.CharField(max_length=255)
    shipper_address_2 = models.CharField(max_length=255)
    shipper_address_3 = models.CharField(max_length=255)
    shipper_airport_code = models.CharField(max_length=10)
    shipper_city = models.CharField(max_length=50)
    shipper_company_name = models.CharField(max_length=255)
    shipper_country = models.CharField(max_length=50)
    shipper_name = models.CharField(max_length=50)
    shipper_phone = models.CharField(max_length=50)
    shipper_postcode_zip = models.CharField(max_length=20)
    weight_rounded = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bill_to_account} - {self.contents}"
