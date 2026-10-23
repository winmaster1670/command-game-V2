import random
from rich import print
from enemy_stats import check_enemy_stats
from item_stats import check_item_stats
from house_upgrades import check_house_upgrade
from events import check_event_stats


# IDEAS
# dungoen (later)
# add factions / clans that you can join or agitate 
# a pluge has struck the lands summoned by an evil entetiy, kill him  (maybe?)
# add town center with a notice board for quests from various nps's with quest difficulties so you dont get quest that are too hard
# every 5 turn have a chance to add a quest to the quest board
# add crafting matierals, can be bought from shops 
# add a shop that stock will randomize every x amount of turns
# add item rarity for shop and maybe item drops like enemy or chest or dungoen loot
# knowalge tree , resipy unlocks , knowlage stat , blueprint finding /buying 
# add afexes from apotheosis and afex dust from grinding down afex items to put afexes of other items
# make it so you can sell stuff to the shop
# make it so you can find crafting matrerials while exploring like wood the the forrest (soon) <============================
# instead of having a defferent item for each combo of woon and metal and adhesive types make different tiers of each crafting material eg:slime is a tier 1 adhisive 
# metal tier will affect aromor / damage stat adhisive teir will affect durability and wood wont be used of armor and will affect accuracy




#=========================================================================
#============ REMEMBER pyinstaller -onefile --clean script.py ============
#=========================================================================


def show_instructions():
    print("[cyan]------ Welcome to my Command RPG ------[/cyan]")
    print(
        "common commands are: [yellow]'explore', 'goto', 'bag', 'stats', 'effects', 'attack', 'run', 'help'[/yellow] and [yellow]'quit'[/yellow]"
        "\n for a list of all comands type: [yellow]'help commands'[/yellow] for help on a spesific topic type: [yellow]'help (topic)'[/yellow]"
    )


def game_loop():
    # vars
    
    #player stats
    health = 10
    max_health = 10
    weapon = "fist"
    damage = check_item_stats(f"{weapon}", "damage")
    accuracy = check_item_stats(f"{weapon}", "accuracy")
    damage_type = check_item_stats(f"{weapon}", "damage type")
    add_damage = 0
    add_accuracy = 0
    
    gold = 10
    attacked = False
    explorable = True
    
    xp = 0
    xp_to_next = 10
    level = 1
    points = 0
    
    skills = []
    pickpocket_cooldown = 0
    rage_cooldown = 0
    rage_timer = 0
    avalable_skills = ["pickpocket", "rage"]
    
    eat_cooldown = 0
    
    #room stats
    current_room = "forrest"
    unlocked_areas = ["forrest"]
    unexplorable_areas = ["shop", "carpenter", "blacksmith", "house"]
    shops_found = False
    
    
    house_level = 0
    house_material = None
    house_upgrades_owned = []
    house_storage = {}
    gold_stored = 0
    house_storage_used = 0
    house_storage_max = 0
    house_upgrades1 = ["house"]
    house_upgrades2 = ["porch", "floor_boards"]
    house_upgrades3 = ["second_floor"]
    house_upgrades_unlocked = ["house"]
    
    #inventory and charm stats
    max_inventory = 5
    inventory_used = 3
    charm_effects = {}
    charms = {}
    charms_equiped = 0
    max_charms = 3
    inventory = {
        "apple": 3,
    }
    
    #other stats
    attack_turn = "player"
    times_explored_forrest = 0
    times_explored_small_town = 0
    playable = True
    effects = {}
    drunk_applied = False
    backpack_applied = False
    
    forrest_enemies = ("slime", "goblin", "rabbit")
    small_town_enemies = ("bandit", "drunkman", "thief")

    forrst_events = ("bow_string", "apple", "boar")
    
    temp_count = 0
    temp_count2 = 0
    temp_count3 = 0

    to_remove = None

    

    playing = True

    while playing:
        # Display current status
        print(
            f"\n Location: {current_room}, gold: {gold}, health: {health} / {max_health}, max inventory: {inventory_used} / {max_inventory}, current weapon: {weapon}"
        )

        # Get input
        command = input("> ").lower().strip().split()

        if not command:
            continue

        # Handle commands
        action = command[0]

        if action == "quit":
            print("Thanks for playing!")
            playing = False

        elif action == "help":
            try:
                what = command[1]
            except:
                what = None

            if what == None:
                print(
                    " Common commands are: 'explore', 'goto', 'bag', 'stats', 'effects', 'attack', 'run', 'help' and quit"
                    "\n for a list of all comands type: 'help commands' for help on a spesific topic type: 'help (topic)'"
                    "\n remember all command and items and everthing is in all lowercase"
                )
            elif what == "combat" or what == "attacking" or what == "attack" or what == "fight" or what == "fighting":
                print(
                      "when exploring you may be [red]attacked[/red] by a creature or person you can either [blue]attack them or run[/blue]"
                      "\n when attacking you roll a random number between 1 - 10 you must roll [blue]BELOW you accuacy stat[blue] so the higher you accuracy the higher the chances of hitting"
                      "\n if you hit you attack you will deal damage depening on your weapon and apply any debufs you weapon may inflict"
                      "\n but you are not hitting a punching bag the enemy will attack back, like you it too will roll a number between 1 - 10 and must roll below it's accuracy stat"
                      "\n if they hit you will take damage depending on the enemy and receive any debufs the enemy may inflict"
                      "\n you can find, buy or craft new weapons some of which may have afexes [yellow](type help afexes for more info)[/yellow] to increese you chances of survival"
                      )
                
            elif what == "explore" or what == "exploring":
                print(
                    " you can explore many areas in the game the first of which is the forrest the one you spawn in."
                    "\n while exploring you my find gold but bewhere you may be [red]attacked by enemies![/red]"
                    "\n the enemies you can be attacked by [blue]differ depending on the area[/blue]."
                    "\n sometimes once you explore one area enough you may [blue]find new areas to explore[/blue]"
                    "\n there are some ares you [blye]can not explore[/blue] however these include the shop the carpenter the blacksmith and your house"
                )

            elif what == "afex" or what == "afexes":
                print(
                    " afex are [blue]random modifiers[/blue] that can be applied on weapons and armor, there are 4 teirs of afexs from most common to rarest they are: [grey]common[/grey] [green]uncommon[/green] [pruple]rare[/purple] [red]mythical[/red]"
                    "\n the most common way to get afex items is [blue]random enemy drops[/blue] but you can also [blue]apply afexes to existing item at the afex-anvil[/blue] [yellow](type help anvil for more info)[/yellow]"
                    "\n this needs [blue]afex dust[/blue] from the item grinder [yellow](type help grinder for more info)[/yellow]"
                    "\n [yellow](type help afex-list for a list of all avalable afexes)[/yellow]"
                    "\n [red]THESE ARE NOT IN THE GAME YET[/red]"
                )

            elif what == "anvil" or what == "afex-anvil":
                print(
                    " there are [blue]2 types of anvil[/blue] both of which are in the basement of your house once you unlock them"
                    "\n the anvil which is used for [blue]crafting weapons, armor and items[/blue] and the afex-anvil used to [blue]apply afexes to items and armor[/blue]"
                    "\n to craft things on the anvil you will need [blue]crafting resorces[/blue] these can be aquired in a few ways the most consistant is to [blue]buy them from stores[/blue] in the town or [blue]grinding down items[/blue] at the item grinder [yellow](type help grinder for more info)[/yellow] but you can also find them [blue]randomly when exploring some areas[/blue] [yellow](type help exploring for more info)[/yellow]"
                    "\n to apply afexes of the afex anvil you will need [blue]afex dust[/blue] you can get this by grinding down afex items at the [blue]item grinder[/blue] [yellow](type help grinder for more info)[/yellow]"
                    "\n you will need the [blue]correct teir[/blue] of afex dust to apply that tier of afex and some afexes will take [blue]multiple afex dusts[/blue]"
                    "\n unlike many other house upgardes the anvil and afex-anvil are not bought from the carpenter you will have to buy the anvil and unfinished-afex-anvil from the blacksmith you will have to enchant the unfinished-afex-anvil with 5 [grey]common afex-dust[/grey] 3 [green]uncommon afex-dust[/green] and 1 [purple]rare afex-dust[/purple]"
                    "\n [red]NOT IN THE GAME YET[/red]"
                )

            elif what == "grinder":
                print(
                    " the item grinder or grinder for short is a way to turn [blue]items into crafting materials[/blue] and [blue]afex items into afex dust[/blue]"
                    "\n when grinding down items you will get [blue]1/3 of the materials[/blue] used to craft it"
                    "\n when grinding down afex items you will get [blue]none of the materials[/blue] use to craft it but you will get afex dust used to apply afexes to weapons and armor [yellow](type help afex-anvil for more info)[/yellow]"
                    "\n unlike many other house upgardes the grinder is not bought at the carpenter you will have to make it yourself at the anvil [yellow](type help anvil for more info)[/yellow]"
                    "\n [red]NOT IN THE GAME YET[/red]"
                )
            
            elif what == "forge":
                print(
                    " the forge is a crafting staton in the basment of you house once you unlock it but if you dont have it unlokced you can goto the blacksmith in town to forge thing for at [italic]competative[/italic] prices"
                    "\n it is used to turn ores into bars and bars into heated bars which are used on the anvil to craft weapons and armor [yellow](type help anvil for more info)[/yellow]"
                    "\n unlike many other house upgardes the forge in not bought at the carpenter you will have to buy it at the blacksmith"
                    "\n [red]THIS IS NOT IN THE GAME YET[/red]"
                )

            elif what == "commands":
                print(
                    " commands are what you type into the terminal / input box next to the > symbol."
                    "\n to execute commands hit enter."
                    "\n all avalable commands are as follows in no particular order:"
                    "\n [green]quit:[/green] (closes the game)"
                    "\n [green]help:[/green] (displayes help menu type another topic after it to get more info on that topic)"
                    "\n [green]bag:[/green] (shows what you have in you inventory you can type bag desc (item name) to see the description of an item)"
                    "\n [green]effects:[/green] (shows the status effects you are under)"
                    "\n [green]explore:[/green] (explores the current area)"
                    "\n [green]goto:[/green] (moves you to another area type where you want to go [yellow]eg: goto forrest[/yellow])"
                    "\n [green]attack:[/green] (attacks the enemy you are fighting, [blue]this command is only usable while in combat[/blue])"
                    "\n [green]run:[/green] (runs from the enemy you are fighting, [blue]this command is only usable in combat[/blue])"
                    "\n [green]eat:[/green] (eat / drink a food item type the item you want to eat [yellow]eg: eat apple[/yellow])"
                    "\n [green]skill:[/green] (uses an active ability you have unlocked type the skill you want to use [yellow]eg: skill rage[/yellow])"
                    "\n [green]skillshelp:[/green] (displays help about the unlockable skills [red]WILL BE REMOVED SOON[/red] )" #port skillshelp command into the help command
                    "\n [green]pointhelp:[/green] (displays help about what you can spend skill points on [red]WILL BE REMOVED SOON[/red])" #port pointhelp command into the help command
                    "\n [green]spendpoints:[/green] (allowes you to buy upgrades with your skill points type the upgarde you want to buy for skills you must add the word skill eg: spendpoints damage / spendpoints skill rage [red]SOON TO BE REWORKED[/red])" #rework spendpoints to accomadate unlockable skills and make a different command for skills and stats
                    "\n [green]equip:[/green] (changes your equipted weapon or charms you must type the type of item you're equiping eg: equip weapon sword / equip charm backpack)"
                    "\n [green]buy:[/green] (buys a item from the shop or a house upgrade from the carpenter)"
                    "\n [green]drop:[/green] (allows you to drop items, this in one of the few command you can use while you have a full inventory, [yellow]but[/yellow] once you drop an item you cannot pick it up it will be [red]permenently deleted[/red])"
                    "\n [green]house:[/green] (displays information about your house and house storage)"
                    "\n [green]deposit:[/green] (deposits items and gold into you house's storage it can only be used while in your house you must type what you are depositing then how much [yellow]eg: deposit item apple 2 / deposit gold 5[/yellow])"
                    "\n [green]retrieve:[/green] (retrieves items or gold from your house's storage it can only be used while in your hosue you must type what your are retrieving then how mcuh [yellow]eg: retrieve item apple 2 / retrieve gold 5[/yellow])"
                    "\n [green]stats:[/green] (displays all of your stats)"
                )

            else:
                print("im sorry but there is no help on that topic at the moment please ask the developer to add a help section for that topic")


        elif action == "bag":
            if len(command) == 1:
                print(f"you are using {inventory_used} inventory slots out of you max of {max_inventory}")
                print("if you would like to see the description for an item type: [yellow]'bag desc [item]'[/yellow]")
                print("the following items are in you inventory")
                print(f"{inventory}")
            elif len(command) == 3:
                what = command[2]
                if what in inventory:
                    i_desc = check_item_stats(f"{what}", "desc")
                    print(f"{i_desc}")
                else:
                    print(f"you do not have {what}")
            elif command[1] == "desc":
                print("what would you like a description on?")
            else:
                print("you must type: [yellow]'bag desc (item)'[/yellow] to see the description of an item")

        elif action == "effects":
            print("you currently have these effects for x amount of turns")
            print(f"{effects}")

        elif action == "explore":
            if playable == True:
                if attacked == False:
                    if explorable == False:
                        print("you can not explore here")
                    else:

                        if pickpocket_cooldown <= 0:
                            pickpocket_cooldown -= 1
                        if rage_timer <= 0:
                            rage_cooldown -= 1

                        event_chance = random.randint (1, 2) #2 = event, 1 = no event
                        if event_chance == 2:
                            caught = random.randint(1, 2) #1 = attacked, 2 not attacked
                        
                        if caught == 1:
                            attack_turn = "player"

                            if current_room == "forrest":
                                caught_by = random.choice()

                            elif current_room == "small_town" or current_room == "town_center":
                                caught_by = random.choice(small_town_enemies)

                            e_health = check_enemy_stats(f"{caught_by}", "health")
                            e_damage = check_enemy_stats(f"{caught_by}", "damage")
                            e_xp = check_enemy_stats(f"{caught_by}", "xp")
                            e_accuracy = check_enemy_stats(f"{caught_by}", "accuracy")
                            e_loot_chance = check_enemy_stats(f"{caught_by}", "loot chance")
                            e_loot = check_enemy_stats(f"{caught_by}", "loot")
                            print(f"[red]youve been attacked[/red] by a {caught_by}")
                            attacked = True


                        elif caught == 2:
                            if current_room == "forrest":
                                event = random.choice(forrst_events)
                            if current_room == "small_town":
                            #    event = random.choice(small_town_events) these dont exist yet
                                event = random.choice(forrest_events)

                            ev_item = check_event_stats(f"{event}", "item")
                            ev_desc = check_event_stats(f"{event}", "desc")

                            if e_item == None:
                                pass
                            else:
                                if e_item in inventory:
                                    inventory[f"{ev_item}"] += 1
                                else:
                                    inventory[f"{ev_item}"] = 1
                            
                            print(f"{ev_desc}")

                        elif event_chance == 1:
                            if current_room == "forrest":
                                times_explored_forrest += 1
                                gold_found = random.randint(1, 4)
                                
                            if current_room == "small_town" or current_room == "town_center":
                                times_explored_small_town += 1
                                gold_found = random.randint(2, 5)
                                
                            gold += gold_found
                            print(f"you found {gold_found} gold, you now have {gold} gold")

                            if times_explored_forrest >= 10:
                                if attacked == False:
                                    if "small_town" not in unlocked_areas:
                                        unlocked_areas += ["small_town"]
                                        print("[magenta]while exploring you find a small_town![/magenta]")
                                        print("you can go to the small town by typing [yellow]'goto small_town'[/yellow]")
                                        print(f"you can now travel you these areas: {unlocked_areas}")

                            if times_explored_small_town >= 5:
                                if attacked == False:
                                    if "town_center" not in unlocked_areas:
                                        unlocked_areas += ["town_center"]

                                        print("[magenta]you find the town_center while exploring the town![/magenta]")
                                        print("you can go to the town_center by typing [yellow](goto town_center)[/yellow]")
                                        print(f"you can now travel to these areas {unlocked_areas}")
                            
                            if current_room == "town_center":
                                if shops_found == False:
                                    if attacked == False:
                                        if "shop" not in unlocked_areas:
                                            unlocked_areas += ["shop"]
                                        if "carpenter" not in unlocked_areas:
                                            unlocked_areas += ["carpenter"]
                                        if "blacksmith" not in unlocked_areas:
                                            unlocked_areas += ["blacksmith"]

                                        print("[magenta] while exploring the town center you find the shopping district[/magenta]")
                                        print("you can now travel to the shop, carpenter and blacksmith")
                                        print(f"you can now travel to these areas: {unlocked_areas}")
                                        shops_found = True
                else:
                    print("you can not explore while under attack")
                    
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")

        elif action == "goto":
            if playable == True:
                if attacked == False:
                    if len(command) >= 2:
                        direction = command[1]
                        if direction in unlocked_areas:
                            if current_room == direction:
                                print("you are already there")
                            else:
                                current_room = direction
                                print(f"you goto {direction}")
                        
                        else:
                            print(f"that is not in unlocked areas you can go to: {unlocked_areas}")
                    else:
                        print("go where?")
                else:
                    print("you can not leave while under attack")
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")
    

        elif action == "attack":
            if playable == True:
                if attacked == True:
                    if attack_turn == "player":
                        what = list(effects.keys())
                        for str in what:
                            what2 = what[temp_count]
                            effects[f"{what2}"] -= 1
                            temp_count += 1
                        hit = random.randint(1, 10)
                        total_accuracy = accuracy - add_accuracy
                        pickpocket_cooldown -= 1
                        if rage_timer <= 0:
                            rage_cooldown -= 1
                        if hit <= total_accuracy:
                            total_damage = damage + add_damage
                            e_health -= total_damage
                            print(f"you attacked the {caught_by} for {total_damage} damage")
                            attack_turn = "enemy"
                        else:
                            print(f"you attacked the {caught_by} but you missed")
                            attack_turn = "enemy"
                    else:
                        print("its not your turn")
                else:
                    print("you're not under attack")
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")

        elif action == "run":
            if attacked == True:
                if attack_turn == "player":
                    what = list(effects.keys())
                    chance = random.randint(1, 2)
                    pickpocket_cooldown -= 1
                    if rage_timer <= 0:
                        rage_cooldown -= 1
                    if chance == 1:
                        print(f"you were unable to run from the {caught_by}")
                        attack_turn = "enemy"
                    else:
                        print(f"you succsefully run from the {caught_by}")
                        attacked = False
                        attack_turn = "player"
                else:
                    print("its not your turn")
            else:
                print("you're not under attack")

        elif action == "eat":
            if len(command) > 1:
                eat_what = command[1]
                is_food = check_item_stats(f"{eat_what}", "food")
                if is_food == True:
                    f_heal = check_item_stats(f"{eat_what}", "health")
                    f_hunger = check_item_stats(f"{eat_what}", "hunger")
                    f_effect = check_item_stats(f"{eat_what}", "effect")
                    f_effect_time = check_item_stats(f"{eat_what}", "effect time")
                    if eat_what in inventory:
                        if (inventory.get(f"{eat_what}")) >= 1:
                            if f_heal == None:
                                pass
                            else:
                                health += f_heal
                                if health > max_health:
                                    health = max_health
                            if f_effect == None:
                                pass
                            else:
                                if f_effect in effects:
                                    effects[f"{f_effect}"] += f_effect_time
                                else:
                                    effects[f"{f_effect}"] = f_effect_time
                                print(
                                    f"you now have the effect {f_effect} for {f_effect_time} turns"
                                )
                            inventory[f"{eat_what}"] -= 1
                            inventory_used -= 1
                            eat_cooldown = 2
                            if inventory_used <= max_inventory:
                                playable = True
                            print(
                                f"you eat an {eat_what}, it heals you for {f_heal}, you now have {health} health"
                            )
    
                        else:
                            print(f"you do not have {eat_what}")

                    else:
                        print(f"you do not have {eat_what}")
                else:
                    print("that is not food")

            else:
                print("eat what")


        elif action == "skill":
            if playable == True:
                if len(command) > 1:
                    what = command[1]
                    if what in skills:
                        what = list(effects.keys())
                        for str in what:
                            what2 = what[temp_count]
                            effects[f"{what2}"] -= 1
                            temp_count += 1
                        if what != "pickpocket":
                            pickpocket_cooldown -= 1
                        if what != "rage":
                            if rage_timer <= 0:
                                rage_cooldown -= 1
                        if what == "pickpocket":
                            if pickpocket_cooldown <= 0:
                                if attacked == True:
                                    earn = random.randint(1, 5)
                                    gold += earn
                                    seen = random.randint(1, 2)
                                    pickpocket_cooldown = 3
                                    if seen == 1:
                                        print(
                                            f"you pickpocketed the {caught_by} for {earn} gold you now have {gold} gold but you were caught"
                                        )
                                        attack_turn = "enemy"
                                    else:
                                        print(
                                            f"you pickpocketed the {caught_by} for {earn} gold you now have {gold} gold you were not seen so you may make another action this turn"
                                        )

                                else:
                                    print("you must be in combat to use that skill")

                            else:
                                print("that ability is on cooldown")

                        if what == "rage":
                            if rage_cooldown <= 0:
                                add_damage += 3
                                add_accuracy -= 2
                                rage_timer = 5
                                rage_cooldown = 7
                                total_damage = damage + add_damage
                                total_accuracy = accuracy + add_accuracy
                                print(
                                    f"you are now raging for the next 5 turns you damage is now {total_damage} and your accuracy is now {total_accuracy}"
                                )

                            else:
                                print("that ability is on cooldown")

                    else:
                        print("you dont have that skill")
                else:
                    print("what skill")
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")

        elif action == "skillshelp":
            print(f"your unlocked skills are {skills}")
            print(f"the skills you can unlock are {avalable_skills}")
            if "pickpocket" in skills:
                print("\n pickpocket--------------------------")
                print(
                    "pickpocket can only be use in combat you can earn 1 to 5 gold randomly no matter what you're fighting"
                )
                print(
                    "it has a cooldown of 3 turns the following actions will lower the cooldown by 1: explore, attack, skill, run"
                )
            if "rage" in skills:
                print("\n rage--------------------------------")
                print(
                    "rage can be use in or out of combat it increaces you damage by 3 but lowers you accuracy by 2 for 5 turns the following action count as a turn: explore, attack, skill, run"
                )
                print(
                    "it has a cooldown of 7 turns the following actions will lower the cooldown by 1: explore, attack, skill, run"
                )
                print("the cooldown will not start going until the effect ends")

        elif action == "pointhelp":
            print(
                "you can spend your points on the following upgrades: 'heal' which will heal you to your current max health, 'health' which will increace your max health by 3, 'damage' which will increase you damage by 1"
            )
            print(
                f"you can also unlock new skills by typing 'spendpoints skill [skill]', the avalable skills are: {avalable_skills}"
            )

        elif action == "spendpoints":
            if playable == True:
                if points >= 1:
                    if len(command) == 2:
                        what = command[1]
                        points -= 1
                        if what == "heal":
                            health = max_health
                            print(
                                f"you have been healed to you max health which is {health}"
                            )
                        elif what == "health":
                            max_health += 3
                            print(
                                f"you max health has been increased by 3 it is now {max_health}"
                            )
                        elif what == "damage":
                            add_damage += 1
                            print(
                                f"all your attacks now deal 1 more damage the total added damage is now {add_damage}"
                            )

                    elif len(command) == 3:
                        what = command[2]
                        if what not in skills:
                            points -= 1
                            if what == "pickpocket":
                                skills += ["pickpocket"]
                                print(
                                    "you have unlocked pickpocket skill you can use it to pickpocket you enemy use it by typing [yellow](skill pickpocket)[/yellow]"
                                )
                                print(f"you're current unlocked skills are {skills}")

                            if what == "rage":
                                skills += ["rage"]
                                print(
                                    "you have unlocked rage skill you cane use it to increase your damage"
                                )
                                print(f"you're current unlocked skills are {skills}")
                        else:
                            print("you already have that skill")
                    else:
                        print(
                            "spend points on what, you can see the avalable upgrades by typing [yellow](pointshelp)[/yellow]"
                        )
                else:
                    print("you dont have any points")
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")

        elif action == "equip":
            if len(command) > 2:
                what = command[1]
                what2 = command[2]
                try:
                    if len(command) >= 3:
                        what3 = command[3]
                    else:
                        what3 = "none"
                except:
                    what3 = "none"
                if what == "weapon":
                    is_weapon = check_item_stats(f"{what2}", "equip")
                    if is_weapon == "weapon":
                        if what2 in inventory:
                            damage = check_item_stats(f"{what2}", "damage")
                            accuracy = check_item_stats(f"{what2}", "accuracy")
                            if weapon in inventory:
                                inventory[f"{weapon}"] =+ 1
                            else:
                                inventory[f"{weapon}"] = 1
                            weapon = f"{what2}"
                            inventory.pop(f"{what2}")
                            print(
                                f"you equip an {what2}, you damage is now {damage} and you accuracy is now {accuracy}"
                            )
                        else:
                            print(f"you dont have a {what2} in your inventory")
                    else:
                        print("that is not a weapon")
                if what == "charm":
                    is_charm = check_item_stats(f"{what2}", "equip")
                    if is_charm == "charm":
                        if what2 in inventory:
                            if f"{what2}" not in charms:
                                if charms_equiped <= max_charms:
                                    charms[f"{what2}"] = 1
                                    charms_equiped += 1
                                    inventory.pop(f"{what2}")
                                    inventory_used -= 1
                                    print(f"you equip the {what2} charm you now have these charms equiped {charms}")
                                elif what3 == "none":
                                    print("you have the max amout of charms equiped you can replace one by typing the one you want to equip followed be the one you want to replace")
                                else:
                                    if what3 in charms:
                                        if f"{what3}" in inventory:
                                            inventory[f"{what3}"] += 1
                                        else:
                                            inventory[f"{what3}"] = 1
                                        charms[f"{what2}"] = 1
                                        inventory.pop(f"{what2}")
                                        print(f"you unequip {what3} and equip {what2} in its place")
                                    else:
                                        print(f"you do not have a {what3} equiped")
                            else:
                                print("you already have one of that charm equip")
                        else:
                            print(f"you dont have a {what2} in your inventory")
                    else:
                        print("that is not a charm")
                else:
                    print("you can use this command to equip weaponns and charms")
            else:
                print("equip what?")


        elif action == "buy":
            if playable == True:
                if len(command) > 1:
                    if current_room == "shop":
                        chat = random.randint(1, 3)
                        what = command[1]
                        cost = check_item_stats(f"{what}", "cost")
                        what2 = check_item_stats(f"{what}", "equip")
                        if gold >= cost:
                            gold -= cost
                            inventory[f"{what}"] = 1
                            inventory_used += 1
                            if what2 == "weapon":
                                print(f"you bought a {what} you can equip it by typing [yellow]'equip weapon {what}'[/yellow]")
                            elif what2 == "charm":
                                print(f"you bought a {what} you can equip it by typing [yellow]'equip charm {what}'[/yellow]")
                            print(f"you now have these items in your inventory {inventory}")
                        else:
                            print(f"you dont have enough gold it costs {cost}")


                    elif current_room == "carpenter":
                        what = command[1]
                        h_cost = check_house_upgrade(f"{what}", "cost")
                        h_where = check_house_upgrade(f"{ehat}", where)
                        if h_where == "capenter":
                            if what in house_upgrades_unlocked:
                                if gold >= h_cost:
                                    if what not in house_upgrades_owned:
                                        house_upgrades_owned += [f"{what}"]
                                        to_remove = house_upgrades_unlocked.index(what)
                                        house_upgrades_unlocked.pop(to_remove)
                                        gold -= h_cost
                                        if ["house"] not in unlocked_areas:
                                            unlocked_areas += ["house"]
                                            print(f"you have bought a house you have unlocked the 'house' area you can go to it by typing [yellow](goto house)[/yellow]")
                                            print("while in you house you can use the [yellow]'deposit'[/yellow] and [yellow]'retrive'[/yellow] commands to store and save gold and items on death")
                                    else:
                                        print("you already own that")
                                else:
                                    print("you can not afford that")
                            else:
                                print(f"you do not have that unlocked, you can buy these upgrades: {house_upgrades_unlocked}")
                        else:
                            print("you can not buy that upgrade in the carpenter")
                    else:
                        print("you must be in the shop or carpenter it buy stuff")
                else:
                    print("buy what? you can see whats for sale by typing [yellow]'shophelp'[yellow] [red]SOON TO BE REMOVED[/red]")
            else:
                print("you are unable to make this action it may be because you inventory is exeded its max check previous messeges")

        elif action == "shophelp":
            if current_room == "shop":
                print(f"the following item are for sale: sword, axe, backpack")
            elif current_room == "carpenter":
                print("the carpenter can build you a house in the forrest and upgrades for the house")
            else:
                print("you must be in a shop to use this command")
            
            
        elif action == "drop":
            if len(command) > 1:
                what = command[1]
                if what in inventory:
                    inventory[f"{what}"] -= 1
                    inventory_used -= 1
                    print(f"you dropped {what}")
                    if inventory_used <= max_inventory:
                        playable = True
                else:
                    print(f"you do not have {what}")
            else:
                print("drop what")

        
        elif action == "house":
            print("these are you house stats:"
                  f"\n [green]house level:[/green] {house_level},"
                  f"\n [green]house upgrades owned:[/green] {house_upgrades_owned},"
                  f"\n [green]house storage used:[/green] {house_storage_used},"
                  f"\n [green]house storage max:[/green] {house_storage_max},"
                  f"\n [green]hosue storage:[/green] {house_storage}"
                  )


        elif action == "deposit":
            if current_room == "house":
                if len(command) >= 2:
                    deposit_type = command[1]
                    if len(command) >= 3:
                        if deposit_type == "item":
                            item = command[2]
                            deposit_amount = int(command[3])
                            amount = inventory.get(f"{item}")
                            if item in inventory:
                                if deposit_amount <= amount:
                                    if house_storage_max >= (house_storage_used + deposit_amount):
                                        inventory[f"{item}"] -= deposit_amount
                                        inventory_used -= deposit_amount
                                        if item in house_storage:
                                            house_storage[f"{item}"] += deposit_amount
                                        else:
                                            house_storage[f"{item}"] = deposit_amount
                                        print(f"you deposit {deposit_amount} {item}(s) you now have these items in your storage {house_storage}")
                                    else:
                                        print("your house does not have enough storage")
                                else:
                                    print("you do not have enough of that")
                            else:
                                print("you do not have that")

                                
                        elif deposit_type == "gold":
                            gold_amount = int(command[2])
                            if gold >= gold_amount:
                                gold_stored += gold_amount
                                gold -= gold_amount
                                print(f"you deposit {gold_amount} into storage you now have {gold_stored} stored")
                            else:
                                print("you do not have that much gold")
                        else:
                            print("that is not an option pick item or gold")
                    else:
                        print("deposit what? for items type the item name for gold type the amount of gold")
                else:
                    print("deposit what? item or gold")
            else:
                print("you must be in the house to access house storage")


        elif action == "retrieve":
            if current_room == "house":
                if len(command) >= 2:
                    retrieve_type = command[1]
                    if len(command) >= 3:
                        if retrieve_type == "item":
                            item = command[2]
                            retrieve_amount = int(command[3])
                            amount = house_storage.get(f"{item}")
                            if item in house_storage:
                                if retrieve_amount <= amount:
                                    if max_inventory >= (retrieve_amount + inventory_used):
                                        if item in inventory:
                                            inventory[f"{item}"] += retrieve_amount
                                        else:
                                            inventory[f"{item}"] = retrieve_amount
                                        inventory_used += retrieve_amount
                                        house_storage_used -= retrieve_amount
                                        print(f"you retieve {retrieve_amount} {item}(s) from you storage you now have these item in your inventory: {inventory}")
                                    else:
                                        print("you do not have enough inventory space")
                                else:
                                    print("you do not have enough of that in storage")
                            else:
                                print("you do not have that in storage")
                        elif retrieve_type == "gold":
                            gold_amount = int(command[2])
                            if gold_amount >= gold_stored:
                                gold += gold_amount
                                gold_stored -= gold_amount
                                print(f"you retrieve {gold_amount} from storgae you now have {gold}")
                            else:
                                print("you do not have enough gold in storage")
                        else:
                            print("that is not an option pick item or gold")
                    else:
                        print("retrieve what? for items type the item name for gold type the amount of gold")
                else:
                    print("retrieve what? item or gold")
            else:
                print("you must be in the house to access house storage")


        elif action == "stats":
            print("[blue]you're stats are as follows:[/blue]")
            print(
                f"\n [green]current room:[/green] {current_room},"
                f"\n [green]health:[/green] {health},"
                f"\n [green]max health:[/green] {max_health},"
                f"\n [green]weapon:[/green] {weapon},"
                f"\n [green]base weapon damage:[/green] {damage},"
                f"\n [green]base weapon accuracy:[/green] {accuracy},"
                f"\n [green]damage added:[/green] {add_damage},"
                f"\n [green]gold:[/green] {gold},"
                f"\n [green]attacked:[/green] {attacked},"
                f"\n [green]unlocked_areas:[/green] {unlocked_areas},"
                f"\n [green]attack_turn:[/green] {attack_turn},"
                f"\n [green]times_explored_forrest:[/green] {times_explored_forrest},"
                f"\n [green]times_explored_small_town:[/green] {times_explored_small_town},"
                f"\n [green]xp:[/green] {xp},"
                f"\n [green]xp_to_next:[/green] {xp_to_next},"
                f"\n [green]level:[/green] {level},"
                f"\n [green]points:[/green] {points},"
                f"\n [green]skills:[/green] {skills},"
                f"\n [green]avalable_skills:[/green] {avalable_skills},"
                f"\n [green]inventory:[/green] {inventory},"
                f"\n [green]effects:[/green] {effects},"
                f"\n [green]charms_equiped:[/green] {charms_equiped},"
                f"\n [green]house_level:[/green] {house_level},"
                f"\n [green]house_material:[/green] {house_material},"
                f"\n [green]house_upgrades_owned:[/green] {house_upgrades_owned},"
                f"\n [green]house_upgrades_unlocked:[/green] {house_upgrades_unlocked},"
                f"\n [green]house_storage:[/green] {house_storage},"
                f"\n [green]house_storage_used:[/green] {house_storage_used},"
                f"\n [green]house_storage_max:[/green] {house_storage_max},"
                f"\n [green]gold_stored:[/green] {gold_stored}"
            )

        elif action == "debug":
            len_debug = len(command)
            if len_debug == 1:
                pass
            if len(command) == 2 or len(command) == 3:
                what = command[1]
                if what == "points":
                    points = 10000
                    print(f"DEBUG: you now have {points} points")
                elif what == "areas":
                    if ["small_town"] in unlocked_areas:
                        pass
                    else:
                        unlocked_areas += ["small_town"]
                    if ["shop"] in unlocked_areas:
                        pass
                    else:
                        unlocked_areas += ["shop"]
                    if ["carpenter"] in unlocked_areas:
                        pass
                    else:
                        unlocked_areas += ["carpenter"]
                    if  ["house"] in unlocked_areas:
                        pass
                    else:
                        unlocked_areas += ["house"]
                    print(
                        f"DEBUG: you now have all the areas unlocked they are {unlocked_areas}"
                    )
                elif what == "area":
                    if len(command) == 3:
                        what2 = command[2]
                        unlocked_areas += [what2]
                        print(f"you unlocked area {what2} you now have these areas unlocked: {unlocked_areas}")
                    else:
                        print("which area do you want to unlock")
                elif what == "gold":
                    gold = 10000
                    print(f"DEBUG: you now have {gold} gold")

                elif what == "xp":
                    xp = xp_to_next
                    print(f"DEBUG: you have leveled up")

                elif what == "attack":
                    print(f"DEBUG: you have entered combat")
                    attack_turn = "player"
                    if current_room == "forrest":
                        caught_by = random.choice(forrest_enemies)
                        e_health = check_enemy_stats(f"{caught_by}", "health")
                        e_damage = check_enemy_stats(f"{caught_by}", "damage")
                        e_xp = check_enemy_stats(f"{caught_by}", "xp")
                        e_accuracy = check_enemy_stats(f"{caught_by}", "accuracy")
                        e_loot_chance = check_enemy_stats(f"{caught_by}", "loot chance")
                        e_loot = check_enemy_stats(f"{caught_by}", "loot")
                        print(f"youve been attacked by a {caught_by}")
                        attacked = True

                    elif current_room == "small_town":
                        caught_by = random.choice(small_town_enemies)
                        e_health = check_enemy_stats(f"{caught_by}", "health")
                        e_damage = check_enemy_stats(f"{caught_by}", "damage")
                        e_xp = check_enemy_stats(f"{caught_by}", "xp")
                        e_accuracy = check_enemy_stats(f"{caught_by}", "accuracy")
                        e_loot_chance = check_enemy_stats(f"{caught_by}", "loot chance")
                        e_loot = check_enemy_stats(f"{caught_by}", "loot")
                        print(f"youve been attacked by a {caught_by}")
                        attacked = True

                elif what == "die":
                    health = 0
                    print("DEBUG setting health to 0")

                elif what == "give":
                    what2 = command[2]
                    print(f"adding 1 {what2} to inventory")
                    if what2 in inventory:
                        inventory[f"{what2}"] += 1
                    else:
                        inventory[f"{what2}"] = 1
                    inventory_used += 1

                elif what == "storage":
                    house_storage_max = 9999
                    print("house_storage_max has been set to 9999")

                else:
                    print("what debug command")

            else:
                print("what debug command")

        else:
            print("Invalid command.")


        if health <= 0:
            if house_level >= 1:
                current_room = "house"
            else:
                current_room = "forrest"
            print("you have [red]died[/red] you lost you gold and inventory")
            attacked = False
            health = max_health
            inventory_used = 0
            gold = 0
            inventory.clear()
            weapon = "fist"

        if attacked == True:
            if e_health <= 0:
                xp += e_xp
                print(f"you defeated the {caught_by}")
                print(f"[blue]you gained {e_xp} xp you now have {xp}[/blue]")
                get_loot = random.randint(1, 10)
                if e_loot == None:
                    pass
                else:
                    if get_loot <= e_loot_chance:
                        print(f"[blue]the {caught_by} dropped {e_loot}[/blue]")
                        if f"{e_loot}" in inventory:
                            inventory[f"{e_loot}"] += 1
                        else:
                            inventory[f"{e_loot}"] = 1
                        inventory_used += 1
                attacked = False
                attack_turn = "player"

        if attack_turn == "enemy":
            if attacked == True:
                hit = random.randint(1, 10)
                if hit <= e_accuracy:
                    health -= e_damage
                    print(
                        f"[red]the {caught_by} hit you[/red] for {e_damage} you have {health} health remaining"
                    )
                    attack_turn = "player"
                else:
                    print(f"[blue]the {caught_by} tried to hit you but missed[/blue]")
                    attack_turn = "player"

        if xp >= xp_to_next:
            level += 1
            xp -= xp_to_next
            points += 1
            if "pickpocket" in skills:
                avalable_skills -= ["pickpocket"]
            print(
                f"[blue]youve leveled up you are now level {level}, you have {points} point(s)[/blue]"
            )
            print(
                "you can spend points by typing [yellow]'spendpoints health'[/yellow] or [yellow]'damage'[/yellow] if you would like to see the avalable upgrades type [yellow]'pointhelp'[/yellow] [red]SOON TO BE REMOVED[/red]"
            )
            print(
                f"you can also unlock skills by typing [yellow]'spendpoints skill (skill)'[/yellow] the unlockable skills are: {avalable_skills}"
            )

        
        
        for thing, value in effects.items():
            #print(f"{thing}") debug stuff
            #print(f"{value}") debug stuff
            value -= 1
            if value <= 0:
                effects.pop(thing)

        if "drunk" in effects:
            if drunk_applied == False:
                add_damage += 3
                add_accuracy -= 2
                drunk_applied = True
        else:
            drunk_applied = False

        if current_room in unexplorable_rooms:
            explorable = False
        else:
            explorable = True



    #charm effects===========================================
        if "backpack" in charms:
            if backpack_applied == False:
                max_inventory + 10
                backpack_applied = True
            else:
                pass
        else:
            max_inventory - 10
            backpack_applied = False
            

            
            
        for item, count in list(inventory.items()):
            if count <= 0:
                inventory_used -= count
                inventory.pop(item)
            
            
        if inventory_used >= (max_inventory + 1):
            playable = False
            print(f"[red]you have exeaded you max inventory of {max_inventory} you must drop somthing[/red]")
            
            
            
        #house upgrade things========================
        if not house_upgrades_unlocked:
            house_level + 1
            if house_level == 1:
                house_upgrades_unlocked += house_upgrades2
            if house_level == 2:
                house_upgrades_unlocked += house_upgrades3


        if "second_floor" in house_upgrades_owned:
            house_storage_max = 50

        if "house" in house_upgrades_owned:
            house_storage_max = 25

        
            



if __name__ == "__main__":
    show_instructions()
    game_loop() 
