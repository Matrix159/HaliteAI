import os
import time

ship_requirement = 10
damage_requirement = 1000


def get_ships(data):
    return int(data.split("producing ")[1].split(" ships")[0])


def get_damage(data):
    return int(data.split("dealing ")[1].split(" damage")[0])


def get_rank(data):
    return int(data.split("rank #")[1].split(" and")[0])


player_1_wins = 0
player_2_wins = 0
player_3_wins = 0
player_4_wins = 0

for num in range(5000):
    try:
        print("Currently on: {}".format(num))
        if player_1_wins > 0 or player_2_wins > 0 or player_3_wins > 0 or player_4_wins > 0:
            p1_pct = round(player_1_wins / (player_1_wins + player_2_wins + player_3_wins + player_4_wins) * 100.0, 2)
            p2_pct = round(player_2_wins / (player_1_wins + player_2_wins + player_3_wins + player_4_wins) * 100.0, 2)
            p3_pct = round(player_3_wins / (player_1_wins + player_2_wins + player_3_wins + player_4_wins) * 100.0, 2)
            p4_pct = round(player_4_wins / (player_1_wins + player_2_wins + player_3_wins + player_4_wins) * 100.0, 2)
            print("Player 1 win: {}%; Player 2 win: {}%; Player 3 win: {}%; Player 4 win: {}%;".format(p1_pct, p2_pct, p3_pct, p4_pct))

        os.system('halite.exe -d "360 240" "python MyBot-1.py" "python MyBot-2.py" '
                  '"python MyBot-3.py" "python MyBot-4.py" --noreplay >> data.gameout')

        with open('data.gameout', 'r') as f:
            contents = f.readlines()
            CharlesBot1 = contents[-8]
            CharlesBot2 = contents[-7]
            CharlesBot3 = contents[-6]
            CharlesBot4 = contents[-5]
            print(CharlesBot1)
            print(CharlesBot2)
            print(CharlesBot3)
            print(CharlesBot4)
            CharlesBot1_ships = get_ships(CharlesBot1)
            CharlesBot1_dmg = get_damage(CharlesBot1)
            CharlesBot1_rank = get_rank(CharlesBot1)

            CharlesBot2_ships = get_ships(CharlesBot2)
            CharlesBot2_dmg = get_damage(CharlesBot2)
            CharlesBot2_rank = get_rank(CharlesBot2)

            CharlesBot3_ships = get_ships(CharlesBot3)
            CharlesBot3_dmg = get_damage(CharlesBot3)
            CharlesBot3_rank = get_rank(CharlesBot3)

            CharlesBot4_ships = get_ships(CharlesBot4)
            CharlesBot4_dmg = get_damage(CharlesBot4)
            CharlesBot4_rank = get_rank(CharlesBot4)
            print("Charles1 rank: {} ships: {} dmg: {}".format(CharlesBot1_rank, CharlesBot1_ships, CharlesBot1_dmg))
            print("Charles2 rank: {} ships: {} dmg: {}".format(CharlesBot2_rank, CharlesBot2_ships, CharlesBot2_dmg))
            print("Charles3 rank: {} ships: {} dmg: {}".format(CharlesBot3_rank, CharlesBot3_ships, CharlesBot3_dmg))
            print("Charles4 rank: {} ships: {} dmg: {}".format(CharlesBot4_rank, CharlesBot4_ships, CharlesBot4_dmg))

        if CharlesBot1_rank == 1:
            print("c1 won")
            player_1_wins += 1
            if CharlesBot1_ships >= ship_requirement and CharlesBot1_dmg >= damage_requirement:
                with open("c1_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train4v4.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c1_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train4v4.out", "a") as f:
                    for l in output_lines:
                        f.write(l)

        elif CharlesBot2_rank == 1:
            print("c2 won")
            player_2_wins += 1
            if CharlesBot2_ships >= ship_requirement and CharlesBot2_dmg >= damage_requirement:
                with open("c2_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train4v4.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c2_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train4v4.out", "a") as f:
                    for l in output_lines:
                        f.write(l)
        elif CharlesBot3_rank == 1:
            print("c3 won")
            player_3_wins += 1
            if CharlesBot3_ships >= ship_requirement and CharlesBot3_dmg >= damage_requirement:
                with open("c3_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train4v4.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c3_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train4v4.out", "a") as f:
                    for l in output_lines:
                        f.write(l)
        elif CharlesBot4_rank == 1:
            print("c4 won")
            player_4_wins += 1
            if CharlesBot4_ships >= ship_requirement and CharlesBot4_dmg >= damage_requirement:
                with open("c4_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train4v4.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c4_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train4v4.out", "a") as f:
                    for l in output_lines:
                        f.write(l)
        time.sleep(2)
    except Exception as e:
        print(str(e))
        time.sleep(2)
