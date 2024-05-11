class MazdaFactory(CarFactory):
    def create_hashback(self):
        return MazdaHashback()

    def create_sedan(self):
        return MazdaSedan()

    def create_suv(self):
        return MazdaSuv()
