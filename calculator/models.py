from django.db import models


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    #  create the foreign key for discount rule model here

    def __str__(self):
        return self.name

class DiscountRules(models.Model):

    RESIDENCIAL = 'Residencial'
    COMERCIAL = 'Comercial'
    INDUSTRIAL = 'Industrial'

    LESS_THAN_10_THOUSAND = 'Less than 10 thousand'
    BETWEEN_10_AND_20_THOUSAND = 'Between 10 thousand and 20 thousand'
    GREATER_THAN_20_THOUSAND = 'Greater than 20 thousand'

    CONSUMER_TYPE_CHOICES = [
        (RESIDENCIAL, 'Residencial'),
        (COMERCIAL, 'Comercial'),
        (INDUSTRIAL, 'Industrial'),
    ]

    CONSUMPTION_RANGE_CHOICES = [
        (LESS_THAN_10_THOUSAND, 'Less than 10 thousand'),
        (BETWEEN_10_AND_20_THOUSAND, 'Between 10 thousand and 20 thousand'),
        (GREATER_THAN_20_THOUSAND, 'Greater than 20 thousand'),
    ]

    COVER_VALUE_CHOICES = [
        (90, '90%'),
        (95, '95%'),
        (99, '99%'),
    ]

    consumer_type = models.CharField(
        max_length=30,
        choices=CONSUMER_TYPE_CHOICES,
        default=RESIDENCIAL
    )

    consumption_range = models.CharField(
        max_length=30,
        choices=CONSUMER_TYPE_CHOICES,
        default=LESS_THAN_10_THOUSAND
    )

    cover_value = models.IntegerField(choices=COVER_VALUE_CHOICES, default=90)

    discount_value = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0
    )


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
