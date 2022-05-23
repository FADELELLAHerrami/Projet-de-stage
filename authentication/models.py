from django.db import models
from django.contrib.auth.models import AbstractUser,Group

class User(AbstractUser):
	CREATOR='CREATOR'
	SUBSCRIBER='SUBSCRIBER'

	ROLE_CHOICES=(
		(CREATOR,'Créateur'),
		(SUBSCRIBER,'Abonné'),
	)
	profile_photo=models.ImageField()
	role=models.CharField(max_length=30,choices=ROLE_CHOICES)
	follows=models.ManyToManyField(
		'self',
		limit_choices_to={'role':CREATOR},
		symmetrical=False,
		verbose_name='suit',
	)

	def save(self,*args,**kargs):
		super().save(*args,**kargs)
		if self.role==self.CREATOR:
			group=Group.objects.get(name='creators')
			group.user_set.add(self)
		elif self.role==self.SUBSCRIBER:
			group=Group.objects.get(name='subscribers')
			group.user_set.add(self)
	