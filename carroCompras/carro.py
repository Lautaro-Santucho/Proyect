class carro:
    def __init__(self, request):
        self.request= request
        self.session= request.session
        carro= self.session.get("carro")
        if not carro:
            carro= self.session["carro"]= {}
        else:
            self.carro=carro

    def agergarProducto(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]= {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":producto.precio,
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for keys, values in self.carro.items():
                if keys == str(producto.id):
                    values["cantidad"]= values["cantidad"]+1
                    break
        self.guardarCambios()
            
    def guardarCambios(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def restarProducto(self, producto):
        for keys, values in self.carro.items():
                if keys == str(producto.id):
                    values["cantidad"]= values["cantidad"]-1
                    if values["cantidad"]<1:
                        self.eliminar()
                    break
        self.guardarCambios()

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro["producto.id"]
        self.guardarCambios()

    def limpiar(self):
        self.session["carro"]= {}

    
