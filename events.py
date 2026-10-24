def check_event_stats(looking, stat):

    #FORREST ===========================

    if looking == "bow_string":
        if stat == "item":
            return "bow_string"
        if stat == "desc":
            return " you walk around the forrest and get increasingly bored, you start playing with some strands of grass you found until you realise you've made a bow_string, sweet! \n [blue]1 bow_string added to inventory"

    if looking == "apple":
        if stat == "item":
            return "apple"
        if stat == "desc":
            return " while exploring you find an apple on the ground, sweet! \n [blue]1 apple added to inventory[/blue]"

    if looking == "boar":
        if stat == "item":
            return None
        if stat == "desc":
            return " you were peacfully enjoying the scenery when you hear brushes rustling you draw your weapon then you realise it's just a dumb boar"

    if looking == "birch_wood":
        if stat == "item":
            return "birch_wood"
        if stat == "desc":
            return "while exploring you find a cool looking stick, maybe you could use this to craft something, sweet! \n [blue]1 birch_wood added to inventory[/blue]"

    #SMALL_TOWN=========================

    if looking == "placeholder":
        pass