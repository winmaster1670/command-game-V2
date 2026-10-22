def check_house_upgrade(looking, stat):
    if looking == "house":
        if stat == "cost":
            return 150
        if stat == "where":
            return "carpenter"

    if looking == "porch":
        if stat == "cost":
            return 65
        if stat == "where":
            return "carpenter"

    if looking == "floor_boards":
        if stat == "cost":
            return 40
        if stat == "where":
            return "carpenter"

    if looking == "second_floor":
        if stat == "cost":
            return 100
        if stat == "where":
            return "carpenter"
