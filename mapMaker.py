import arcade

SPRITE_SCALING = .5

def get_map(map):
    map_file = open(map)
    map_array = []
    for line in map_file:
        line = line.strip()
        map_row = line.split(",")
        for index, item in enumerate(map_row):
            map_row[index] = int(item)
        map_array.append(map_row)

    return map_array

def draw_map(app, map):
    map_array = get_map(map)

    for row_index, row in enumerate(map_array):
        for column_index, item in enumerate(row):

            if item == 9:
                continue
            elif item == 0:
                wall = arcade.Sprite("images/grass.png",
                                     SPRITE_SCALING)
            elif item == 1:
                wall = arcade.Sprite("images/stoneMid.png",
                                     SPRITE_SCALING)
            elif item == 2:
                wall = arcade.Sprite("images/grassMid.png",
                                     SPRITE_SCALING)
            elif item == 3:
                wall = arcade.Sprite("images/grassCenter.png",
                                     SPRITE_SCALING)

                wall.points = ((-wall.width // 2, wall.height // 2),
                                     (wall.width // 2, -wall.height // 2),
                                     (-wall.width // 2, -wall.height // 2),
                                     (wall.width // 2, wall.height // 2))
            elif item == 4:
                wall = arcade.Sprite("images/stoneCenter.png",
                                     SPRITE_SCALING)
            elif item == 5:
                death_spot = arcade.Sprite("images/spikes.png",
                                           SPRITE_SCALING + .31)

                # change shape of block
                death_spot.points = ((-death_spot.width // 8, death_spot.height // 8),
                                     (death_spot.width // 2, -death_spot.height // 2),
                                     (-death_spot.width // 2, -death_spot.height // 2),
                                     (death_spot.width // 8, death_spot.height // 8))

                death_spot.right = column_index * 64 - 5
                death_spot.top = (7 - row_index) * 64 + 421
                app.all_sprites_list.append(death_spot)
                app.death_spots_up.append(death_spot)
            elif item == 6:
                plant = arcade.Sprite("images/plant.png",
                                      SPRITE_SCALING + .5)
                plant.right = column_index * 64
                plant.top = (7 - row_index) * 64 + 450
                app.all_sprites_list.append(plant)
            elif item == 7:
                wall = arcade.Sprite("images/iceBlock.png",
                                     SPRITE_SCALING * 1.82)
            elif item == 8:
                death_spot = arcade.Sprite("images/spikesTop.png", SPRITE_SCALING + .4)

                # change shape of block
                death_spot.points = ((-death_spot.width // 8, death_spot.height // 8),
                                     (death_spot.width // 2, -death_spot.height // 2),
                                     (-death_spot.width // 2, -death_spot.height // 2),
                                     (death_spot.width // 8, death_spot.height // 8))

                death_spot.right = column_index * 64 - 1
                death_spot.top = (7 - row_index) * 64 + 426
                app.all_sprites_list.append(death_spot)
                app.death_spots_down.append(death_spot)

            # 9 is the empty space

            elif item == 10:
                new_item = arcade.Sprite("images/hudKey_yellow.png",
                                         SPRITE_SCALING)
                new_item.right = column_index * 64
                new_item.top = (7 - row_index) * 64 + 450
                app.items.append(new_item)
                app.all_sprites_list.append(new_item)
                app.keys.append(new_item)

            elif item == 11:
                wall = arcade.Sprite("images/doorClosed_mid.png",
                                     SPRITE_SCALING)
                app.doors.append(wall)
            elif item == 12:
                spring = arcade.Sprite("images/springboardUp.png",
                                       SPRITE_SCALING + .5)
                spring.right = column_index * 64
                spring.top = (7 - row_index) * 64 + 455
                app.springs.append(spring)
                app.all_sprites_list.append(spring)
            elif item == 13:
                goal = arcade.Sprite("images/flagBlue.png", SPRITE_SCALING * 2)
                goal.right = column_index * 64
                goal.top = (7 - row_index) * 64 + 455
                app.goals.append(goal)
                app.all_sprites_list.append(goal)
            elif item == 14:
                gem = arcade.Sprite("images/gemRed.png", SPRITE_SCALING * 2)
                gem.right = column_index * 64
                gem.top = (7 - row_index) * 64 + 450
                app.gems.append(gem)
                app.all_sprites_list.append(gem)

            elif item == 15:
                death_spot = arcade.Sprite("images/spikesBottom.png", SPRITE_SCALING + .4)

                # change shape of block
                death_spot.points = ((-death_spot.width // 8, death_spot.height // 8),
                                     (death_spot.width // 2, -death_spot.height // 2),
                                     (-death_spot.width // 2, -death_spot.height // 2),
                                     (death_spot.width // 8, death_spot.height // 8))

                death_spot.right = column_index * 64 - 1
                death_spot.top = (7 - row_index) * 64 + 423
                app.all_sprites_list.append(death_spot)
                app.death_spots_up.append(death_spot)

            elif item == 16:
                wall = arcade.Sprite("images/slice28_28.png", SPRITE_SCALING * 1.83)

            elif item == 17:
                wall = arcade.Sprite("images/slice32_32.png", SPRITE_SCALING * 1.83)

            elif item == 18:
                wall = arcade.Sprite("images/slice20_20.png", SPRITE_SCALING * 1.83)

            elif item == 19:
                wall = arcade.Sprite("images/slice24_24.png", SPRITE_SCALING * 1.83)

            elif item == 20:
                wall = arcade.Sprite("images/slice19_19.png", SPRITE_SCALING * 1.83)

            elif item == 21:
                wall = arcade.Sprite("images/slice23_23.png", SPRITE_SCALING * 1.83)

            # don't collide with this
            elif item == 22:
                wall = arcade.Sprite("images/slice33_33.png", SPRITE_SCALING * 1.83)

            # platforms which move at various speeds
            elif item == 23:
                wall = arcade.Sprite("images/iceBlock.png", SPRITE_SCALING * 1.82)
            elif item == 24:
                wall = arcade.Sprite("images/iceBlock.png", SPRITE_SCALING * 1.82)
            elif item == 25:
                wall = arcade.Sprite("images/iceBlock.png", SPRITE_SCALING * 1.82)


            if (item is 0) or (item is 1) or (item is 2) \
                    or (item is 3) or (item is 4) or (item is 11) \
                    or (item is 7) or (item is 16) or (item is 17)\
                    or (item is 18) or (item is 19) or (item is 20)\
                    or (item is 21) or (item is 22) or (item is 23)\
                    or (item is 24) or (item is 25):
                wall.right = column_index * 64
                wall.top = (7 - row_index) * 64 + 450

                if item is 23:
                    wall.boundary_left = wall.right - 200
                    wall.boundary_right = wall.right + 200
                    wall.change_x = 1
                if item is 24:
                    wall.boundary_left = wall.right - 200
                    wall.boundary_right = wall.right + 200
                    wall.change_x = 3
                if item is 25:
                    wall.boundary_left = wall.right - 200
                    wall.boundary_right = wall.right + 200
                    wall.change_x = 2

                app.all_sprites_list.append(wall)
                app.walls.append(wall)
