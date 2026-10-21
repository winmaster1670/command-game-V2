def check_item_stats(looking, stat):
    
    #FOOD==================================
    if looking == "apple":
        if stat == "health":
            return 3
        if stat == "hunger":
            return 3
        if stat == "effect":
            return None
        if stat == "effect time":
            return None
        if stat == "food":
            return True
        if stat == "crafting":
            return False
        if stat == "equip":
            return False
        if stat == "desc":
            return " this is an apple, you can eat it, just make sure to check for worms \n it heals you for 3 health"
            
    if looking == "bread":
        if stat == "health":
            return 4
        if stat == "hunger":
            return 4
        if stat == "effect":
            return None
        if stat == "effect time":
            return None
        if stat == "food":
            return True
        if stat == "crafting":
            return False
        if stat == "equip":
            return False
        if stat == "desc":
            return " its a piece of bread, you can eat it, not much to say its bread \n it heals you for 4 health"
            
    if looking == "ale":
        if stat == "health":
            return None
        if stat == "effect":
            return "drunk"
        if stat == "effect time":
            return 5
        if stat == "food":
            return True
        if stat == "crafting":
            return False
        if stat == "equip":
            return False
        if stat == "desc":
            return " its ale you can drink it, side effects include: confedence, dancing skills and getting kicked out of places \n it applies the 'drunk' effect increacing damage but lowering accuracy"
            
            
    #WEAPONS====================
    if looking == "sword":
        if stat == "damage":
            return 4
        if stat == "accuracy":
            return 7
        if stat == "cost":
            return 22
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "weapon"
        if stat == "desc":
            return " this is a sword, its better then punching stuff \n its accuracy is 7 and its damage is 4"
            
    if looking == "axe":
        if stat == "damage":
            return  6
        if stat == "accuracy":
            return 5
        if stat == "cost":
            return 19
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "weapon"
        if stat == "desc":
            return " this is an axe, the weapon of a barbarian, or you maybe \n its accuracy is 5 and its damage is  6"
            
    if looking == "dagger":
        if stat == "damage":
            return  3
        if stat == "accuracy":
            return 8
        if stat == "cost":
            return 17
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "weapon"
        if stat == "desc":
            return " this is a dagger, allan please add details \n its accuracy is 8 and its damage is 3"
            
    if looking == "fist":
        if stat == "damage":
            return 3
        if stat == "accuracy":
            return 6
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "weapon"
        if stat == "desc":
            return "this is your fist, please dont eat it \n its accuracy is 6 and its damage is 3"
            
    
    #CRAFTING==============
    if looking == "slime":
        if stat == "cost":
            return 17
        if stat == "food":
            return False
        if stat == "crafting":
            return True
        if stat == "equip":
            return False
        if stat == "desc":
            return "this is slime, its slimy and sticky who wouldve guessed \n it is a teir 1 adhesive use in crafting"

    
    
    
    #CHARMS=================
    if looking == "bandana":
        if stat == "cost":
            return None
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "charm"
        if stat == "charm effect":
            return list("disguise bandit", "add", 2)
        if stat == "desc":
            return " this is a bandana, its seen many bank robberies but it'll never talk \n it is a charm that will give disguise you as a bandit [red]THIS DOES NOTHING YET[/red]"
            
    if looking == "rabbits_foot":
        if stat == "cost":
            return 16
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "charm"
        if stat == "charm effect":
            return list("luck", "add", 3)
        if stat == "desc":
            return " its a rabbits foot, ITS SO FLUFFY \n it is used as a speacial item in crafting"
        
    
    
    #OTHER==============

    if looking == "backpack":
        if stat == "cost":
            return 25
        if stat == "food":
            return False
        if stat == "crafting":
            return False
        if stat == "equip":
            return "charm"
        if stat == "charm effect":
            return "max inventory +10"
        if stat == "desc":
            return " its a backpack, who knows whats in it? actually you do \n its a charm that will increace you max inventory by 10"