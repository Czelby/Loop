from Base import base_home_window, base_chest_window


def base_exe():
    run = 0
    while run == 0:
        dec = base_home_window()
        if dec == 1:
            run = 1
            base_chest_window()


base_exe()
