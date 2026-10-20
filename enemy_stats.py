def check_enemy_stats(looking, stat):
    
    if looking == "slime":
        if stat == "health":
            return 5
        if stat == "damage":
            return 2
        if stat == "accuracy":
            return 4
        if stat == "xp":
            return 3
        if stat == "loot chance":
            return 2
        if stat == "loot":
            return "slime"

    if looking == "goblin":
        if stat == "health":
            return 3
        if stat == "damage":
            return 4
        if stat == "accuracy":
            return 4
        if stat == "xp":
            return 2
        if stat == "loot chance":
            return None
        if stat == "loot":
            return None
            
    if looking == "rabbit":
        if stat == "health":
            return 2
        if stat == "damage":
            return 1
        if stat == "accuracy":
            return 7
        if stat == "xp":
            return 1
        if stat == "loot chance":
            return 3
        if stat == "loot":
            return "rabbits_foot"
            
            
    if looking == "bandit":
        if stat == "health":
            return 4
        if stat == "damage":
            return 3
        if stat == "accuracy":
            return 5
        if stat == "xp":
            return 4
        if stat == "loot chance":
            return 1
        if stat == "loot":
            return "bandana"
            
    if looking == "drunkman":
        if stat == "health":
            return 2
        if stat == "damage":
            return 1
        if stat == "accuracy":
            return 3
        if stat == "xp":
            return 1
        if stat == "loot chance":
            return 3
        if stat == "loot":
            return "ale"
            
    if looking == "thief":
        if stat == "health":
            return 3
        if stat == "damage":
            return 3
        if stat == "accuracy":
            return 6
        if stat == "xp":
            return 4
        if stat == "loot chance":
            return 3
        if stat == "loot":
            return "dagger"
            
    if looking == "shopkeeper":
        if stat == "health":
            return 40
        if stat == "damage":
            return 7
        if stat == "accuracy":
            return 8
        if stat == "xp":
            return 30
        if stat == "loot chance":
            return 10
        if stat == "loot":
            return "shop key"