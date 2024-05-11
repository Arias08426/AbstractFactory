class ChevroletFactory(CarFactory):
    def create_hashback(self):
        return ChevroletHashback()

    def create_sedan(self):
        return ChevroletSedan()

    def create_suv(self):
        return ChevroletSuv()