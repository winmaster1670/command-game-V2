def check_house_upgrade(looking, stat):
    if looking == "house":
        if stat == "cost":
            return 150

    if looking == "porch":
        if stat == "cost":
            return 75

    if looking == "floor_boards":
        if stat == "cost":
            return 50
