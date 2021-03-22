  
from django.db import models

# Create your models here.

class Account(models.Model):
	account_name = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.account_name


class Opportunitie(models.Model):
        opportunity_title = models.CharField(max_length=200, null=True)
        associated_account = models.ForeignKey(Account, null=True, on_delete= models.SET_NULL)
        amount = models.DecimalField(max_digits=8, decimal_places=2)
        discovery = models.CharField(max_length=200, null=True)
        proposal_shared = models.CharField(max_length=200, null=True)
        negotiations = models.CharField(max_length=200, null=True)

        def __str__(self):
            return self.opportunity_title

