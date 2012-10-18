from django.db import models

class Mes(models.Model):
    mes = models.CharField(max_length=10)
    
    # ...
    def __unicode__(self):
        return self.mes

class Marca(models.Model):
    marca = models.CharField(max_length=100)
    
    # ...
    def __unicode__(self):
        return self.marca

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    # ...
    def __unicode__(self):
        return self.categoria

class Local(models.Model):
    local = models.CharField(max_length=100)
    
    # ...
    def __unicode__(self):
        return self.local

class Color(models.Model):
    color = models.CharField(max_length=100)
    
    # ...
    def __unicode__(self):
        return self.color

class Talle(models.Model):
    talle = models.CharField(max_length=100)
    
    # ...
    def __unicode__(self):
        return self.talle
    
class Componente(models.Model):
    componente = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.componente

class Producto(models.Model):
    codigo = models.CharField(max_length=500)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    descripcion = models.CharField(max_length=500)
    composiciones = models.ManyToManyField(Componente, through='Composicion')
    
    def __unicode__(self):
        return self.codigo

class Composicion(models.Model):
    producto = models.ForeignKey(Producto)
    componente = models.ForeignKey(Componente)
    porcentaje = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.producto) + " + " + unicode(self.componente) + " + " + unicode(self.porcentaje)
    
class Articulo(models.Model):
    producto = models.ForeignKey(Producto)
    talle = models.ForeignKey(Talle)
    local = models.ForeignKey(Local)
    color = models.ForeignKey(Color)
    stock = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.producto) + " + " + unicode(self.talle) + " + " + unicode(self.local) + " + " + unicode(self.color)  + " -> " + unicode(self.stock) 
    
    
class Precio(models.Model):
    producto = models.ForeignKey(Producto)
    talle = models.ForeignKey(Talle)
    precio = models.CharField(max_length=100)
    
    def __unicode__(self):
        return unicode(self.producto) + " + " + unicode(self.talle)  + " -> " + self.precio 
    
    