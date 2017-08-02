from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=200)

	def __init__(self, arg):
		super(Company, self).__init__()
		self.arg = arg


class Brewery(models.Model):
	"""docstring for Brewery"""

	def __init__(self, arg):
		super(Brewery, self).__init__()
		self.arg = arg
		

class Customer(models.Model):
	"""docstring for Customer"""
	name = models.CharField(max_length=200)
	card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
	status = models.IntegerField(default=0)
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=200)
    birthday = models.DateTimeField('birth date')
	
	def __init__(self, arg):
		super(Customer, self).__init__()
		self.arg = arg

		
class Card(models.Model):
	"""docstring for Card"""
	name = models.CharField(max_length=200)
	hashcode = models.CharField(max_length=200)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
	status = models.IntegerField(default=0)
	cost_total = models.IntegerField(default=0)
	
	def __init__(self, arg):
		super(Card, self).__init__()
		self.arg = arg

class BeerType(object):
	"""docstring for BeerType"""
	name = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

	def __init__(self, arg):
		super(BeerType, self).__init__()
		self.arg = arg
		

class Beer(models.Model):
	"""docstring for Beer"""
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	harmonization = models.CharField(max_length=200)
	details = models.CharField(max_length=200)
	brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
	ibu = models.IntegerField(default=0)
	abv = models.IntegerField(default=0)
	price_liter = models.IntegerField(default=0)

	def __init__(self, arg):
		super(Beer, self).__init__()
		self.arg = arg

class Consumption(models.Model):
	"""docstring for Consumption"""
	card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
	beer_id = models.ForeignKey(Beer, on_delete=models.CASCADE)
	beer_qty = models.IntegerField(default=0)
    time = models.DateTimeField('birth date')

	def __init__(self, arg):
		super(Consumption, self).__init__()
		self.arg = arg
