from django.db import models

# Create your models here.
class Marca(models.Model):
	marca=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='Marca'
		verbose_name_plural='Marcas'
	def __str__(self):
		return self.marca

class Modelo(models.Model):
	modelo=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='Modelo'
		verbose_name_plural='Modelos'
	def __str__(self):
		return self.modelo

class Tienda(models.Model):
	nombre=models.CharField(max_length=50, unique=True)
	marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
	modelo=models.ForeignKey(Modelo, on_delete=models.CASCADE)
	imagen=models.ImageField(upload_to='Producto')
	precio=models.FloatField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Tienda"
		verbose_name_plural = "Tiendas"

	def __str__(self):
		return self.nombre