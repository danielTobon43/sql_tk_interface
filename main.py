from crud_gui.crud import InterCrud


def main():
    print("=========== Practica Guiada ===========")
    GUI = InterCrud('BBDD1')
    GUI.on_exit()


if __name__ == "__main__":
    main()
