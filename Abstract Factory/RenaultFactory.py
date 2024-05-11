class RenaultFactory(CarFactory):
    def create_hashback(self):
        return RenaultHashback()

    def create_sedan(self):
        return RenaultSedan()

    def create_suv(self):
        return RenaultSuv()