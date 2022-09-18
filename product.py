class Product:

    def __init__(self, _title_, _price_, _location_, _link_) -> None:
        self.title = _title_
        self.price = _price_
        self.location = _location_
        self.link = _link_
        
        #Bunlar None çünkü bilgiler başta veya sonradan da hiç olmayabilir.
        self.category = None
        self.brand_name = None
        self.model_name = None
        