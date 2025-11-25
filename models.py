from django.db import models

# ============================
#      CATEGORÍA ALMACÉN
# ============================
class CategoriaAlmacen(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField()
    temperatura_ideal = models.CharField(max_length=50)
    tipo_almacenamiento = models.CharField(max_length=50)
    es_peligroso = models.BooleanField()

    def __str__(self):
        return self.nombre_categoria


# ============================
#       PROVEEDOR ALMACÉN
# ============================
class ProveedorAlmacen(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    contacto_persona = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_proveedor


# ============================
#       EMPLEADO ALMACÉN
# ============================
class EmpleadoAlmacen(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratación = models.DateField()
    carga = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    licencia_manejo_montacargas = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ============================
#       PRODUCTO ALMACÉN
# ============================
class ProductoAlmacen(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigo_sku = models.CharField(max_length=50)
    stock_actual = models.IntegerField()
    ubicacion_almacen = models.CharField(max_length=100)
    
    # Relaciones
    id_categoria = models.ForeignKey(CategoriaAlmacen, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.CASCADE)

    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    volumen_m3 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ultimo_movimiento = models.DateTimeField()

    def __str__(self):
        return self.nombre_producto


# ============================
#       ENTRADA PRODUCTO
# ============================
class EntradaProducto(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    
    id_producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_entrada = models.IntegerField()
    fecha_entrada = models.DateTimeField()
    
    id_proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.CASCADE)
    num_factura_compra = models.CharField(max_length=50)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    id_empleado_recepcion = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    observaciones = models.TextField()

    def __str__(self):
        return f"Entrada {self.id_entrada}"


# ============================
#        SALIDA PRODUCTO
# ============================
class SalidaProducto(models.Model):
    id_salida = models.AutoField(primary_key=True)
    
    id_producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    cantidad_salida = models.IntegerField()
    fecha_salida = models.DateTimeField()

    destino = models.CharField(max_length=100)
    id_cliente_salida = models.IntegerField()
    num_pedido_salida = models.CharField(max_length=50)
    
    id_empleado_despacho = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    motivo_salida = models.TextField()

    def __str__(self):
        return f"Salida {self.id_salida}"


# ============================
#        INVENTARIO FÍSICO
# ============================
class InventarioFisico(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    fecha_inventario = models.DateField()

    id_producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE)
    stock_sistema = models.IntegerField()
    stock_fisico = models.IntegerField()
    diferencia = models.IntegerField()

    id_empleado_realizo = models.ForeignKey(EmpleadoAlmacen, on_delete=models.CASCADE)
    comentarios = models.TextField()
    ultima_actualizacion = models.DateTimeField()

    def __str__(self):
        return f"Inventario {self.id_inventario}"

