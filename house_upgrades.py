def check_house_upgrade(looking, stat):
    if looking == "house":
        if stat == "cost":
            return 150

    if looking == "porch":
        if stat == "cost":
            return 65

    if looking == "floor_boards":
        if stat == "cost":
            return 40

    if looking == "second_floor":
        if stat == "cost":
            return 100

    if looking == "stone_walls":
        if stat == "cost":
            return 75