def check_house_upgrade(looking, stat):
    if looking == "house":
        if stat == "cost":
            return 150
        if stat == "where":
            return "carpenter"
        if stat == "need":
            return None

    if looking == "porch":
        if stat == "cost":
            return 65
        if stat == "where":
            return "carpenter"
        if stat == "need":
            return "house"

    if looking == "floor_boards":
        if stat == "cost":
            return 40
        if stat == "where":
            return "carpenter"
        if stat == "need":
            return "house"

    if looking == "second_floor":
        if stat == "cost":
            return 100
        if stat == "where":
            return "carpenter"
        if stat == "need":  #DOUBLE MODE BITCHES
            return "double" #DOUBLE MODE BITCHES
        if stat == "need1":
            return "floor_boards"
        if stat == "need2":
            return "porch"

