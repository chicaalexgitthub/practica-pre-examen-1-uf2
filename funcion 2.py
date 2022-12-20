def new_tfn():
    try:
        tfn = input("Introduce the new tfn: ")
        if not tfn.isdigit():
            raise ValueError("The tfn must be all digits.")
        elif not len(tfn) == 9:
            raise ValueError("The tfn must be 9 digits long.")
        return tfn
    except ValueError as error:
        print(error)
        input("Press enter to continue.")
        new_tfn()


new_tfn()