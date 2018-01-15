import hlt
import logging
from collections import OrderedDict
game = hlt.Game("MatrixBot")
logging.info("Starting MatrixBot")

while True:
    game_map = game.update_map()
    command_queue = []
    player_id = game_map.my_id
    logging.info("Player id: " + str(player_id))
    for ship in game_map.get_me().all_ships():
        shipid = ship.id
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            # Skip this ship
            continue

        entities_by_distance = game_map.nearby_entities_by_distance(ship)
        #Debug logging
        #logging.info(str(entities_by_distance))

        entities_by_distance = OrderedDict(sorted(entities_by_distance.items(), key=lambda t: t[0]))
        
        closest_empty_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and not entities_by_distance[distance][0].is_owned()]
        closest_owned_unfilled_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet)
                                          and entities_by_distance[distance][0].is_owned()
                                          and entities_by_distance[distance][0].owner.id == player_id
                                          and not entities_by_distance[distance][0].is_full()]
        #logging.info(str(closest_owned_unfilled_planets))
        team_ships = game_map.get_me().all_ships()
        closest_enemy_ships = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] not in team_ships]
        planet_owner_ids = ""
        for planet in game_map.all_planets():
            if planet.owner is not None:
                planet_owner_ids += str(planet.owner.id)
        logging.info(planet_owner_ids)
        # Fill owned planets first
        if len(closest_owned_unfilled_planets) > 0:
            target_planet = closest_owned_unfilled_planets[0]
            if ship.can_dock(target_planet):
                command_queue.append(ship.dock(target_planet))
            else:
                navigate_command = ship.navigate(
                    ship.closest_point_to(target_planet),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED),
                    ignore_ships=False)
                if navigate_command:
                    command_queue.append(navigate_command)
        # If there are any empty planets, let's try to mine!
        elif len(closest_empty_planets) > 0:
            target_planet = closest_empty_planets[0]

            if ship.can_dock(target_planet):
                command_queue.append(ship.dock(target_planet))
            else:
                navigate_command = ship.navigate(
                            ship.closest_point_to(target_planet),
                            game_map,
                            speed=int(hlt.constants.MAX_SPEED),
                            ignore_ships=False)

                if navigate_command:
                    command_queue.append(navigate_command)

        # FIND SHIP TO ATTACK!
        elif len(closest_enemy_ships) > 0:
            target_ship = closest_enemy_ships[0]
            navigate_command = ship.navigate(
                        ship.closest_point_to(target_ship),
                        game_map,
                        speed=int(hlt.constants.MAX_SPEED),
                        ignore_ships=False)

            if navigate_command:
                command_queue.append(navigate_command)

    game.send_command_queue(command_queue)
    # TURN END
# GAME END