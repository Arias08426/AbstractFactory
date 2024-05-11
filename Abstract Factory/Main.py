def main():
    MazdaFactory = MazdaFactory()
    ChevroletFactory = ChevroletFactory()
    RenaultFactory = RenaultFactory()

    Car= [
        MazdaFactory.create_Hashback(),
        MazdaFactory.create_Sedan(),
        MazdaFactory.create_Suv(),
        ChevroletFactory.create_Hashback(),
        ChevroletFactory.create_Sedan(),
        ChevroletFactory.create_Suv(),
        RenaultFactory.create_Hashback()
        RenaultFactory.create_Sedan()
        RenaultFactory.create_Suv()
    ]

    for Car in Car:
        Car.SellCar()

if __name__ == "__main__":
    main()