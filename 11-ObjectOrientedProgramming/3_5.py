from thermometer import Temperature
def main():
    import random
    temp = round(random.uniform(34.0,42.0),2)

    my_therm = Temperature(temp)
    my_therm.turn_on()
    my_therm.messure()
    my_therm.turn_off()
    my_therm.messure()

if __name__ == "__main__":
    main()
