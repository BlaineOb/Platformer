import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
VIEWPORT_MARGIN = 40
SPRITE_SCALING = .5

"""
-Level Design
-Enemies
-Animation for character/springs
"""


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
                    wall = arcade.Sprite("images/stone.png",
                                         SPRITE_SCALING)
                elif item == 2:
                    wall = arcade.Sprite("images/grassMid.png",
                                         SPRITE_SCALING)
                elif item == 3:
                    wall = arcade.Sprite("images/grassCenter.png",
                                         SPRITE_SCALING)
                elif item == 4:
                    wall = arcade.Sprite("images/stoneCenter.png",
                                         SPRITE_SCALING)
                elif item == 5:
                    death_spot = arcade.Sprite("images/spikes.png",
                                               SPRITE_SCALING + .3)
                    death_spot.right = column_index * 64 - 5
                    death_spot.top = (7 - row_index) * 64 + 442
                    app.all_sprites_list.append(death_spot)
                    app.death_spots.append(death_spot)
                elif item == 6:
                    plant = arcade.Sprite("images/plant.png",
                                          SPRITE_SCALING + .5)
                    plant.right = column_index * 64
                    plant.top = (7 - row_index) * 64 + 450
                    app.all_sprites_list.append(plant)
                elif item == 7:
                    wall = wall = arcade.Sprite("images/iceBlock.png",
                                         SPRITE_SCALING * 1.82)

                elif item == 10:
                    new_item = arcade.Sprite("images/hudKey_yellow.png",
                                             SPRITE_SCALING)
                    new_item.right = column_index * 64
                    new_item.top = (7 - row_index) * 64 + 450
                    app.items.append(new_item)
                    app.all_sprites_list.append(new_item)
                    app.yellow_key = new_item

                elif item == 11:
                    wall = arcade.Sprite("images/doorClosed_mid.png",
                                         SPRITE_SCALING)
                    app.wood_door = wall
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
                    coin = arcade.Sprite("images/gemRed.png", SPRITE_SCALING * 2)
                    coin.right = column_index * 64
                    coin.top = (7 - row_index) * 64 + 450
                    app.all_sprites_list.append(coin)

                if (item is 0) or (item is 1) or (item is 2) \
                        or (item is 3) or (item is 4) or (item is 11) or (item is 7):
                    wall.right = column_index * 64
                    wall.top = (7 - row_index) * 64 + 450
                    app.all_sprites_list.append(wall)
                    app.walls.append(wall)

class Player(arcade.Sprite):

    key = None

    def update(self, dt):

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH + 3501:
            self.right = SCREEN_WIDTH + 3500

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.player = None
        self.walls = None
        self.death_spots = None
        self.items = None
        self.springs = None
        self.goals = None
        self.background = None
        self.background2 = None
        self.background3 = None
        self.background4 = None
        self.physics_engine = None
        self.all_sprites_list = None
        self.yellow_key = None
        self.wood_door = None
        self.level = 1
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.walls = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.springs = arcade.SpriteList()
        self.death_spots = arcade.SpriteList()
        self.goals = arcade.SpriteList()
        self.player = Player("images/player_stand.png", 0.5)
        self.player.center_x = 200
        self.player.center_y = 355

        self.background = arcade.load_texture("images/colored_grass.png")
        self.background2 = arcade.load_texture("images/colored_land.png")
        self.background3 = arcade.load_texture("images/colored_grass.png")
        self.background4 = arcade.load_texture("images/colored_land.png")
        self.all_sprites_list.append(self.player)

        draw_map(self, "map.csv")

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.walls, 1.0)


    def on_draw(self):
        arcade.start_render()
        # load backgrounds 1-4
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 1.5, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 2.25, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 3, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)

        self.all_sprites_list.draw()
        self.draw_text()

    def draw_text(self):
        if self.level == 1:
            t1 = arcade.create_text("Level 1", arcade.color.BLACK, 20)
            arcade.render_text(t1, 200, 860)
        elif self.level == 2:
            t1 = arcade.create_text("Level 2", arcade.color.BLACK, 20)
            arcade.render_text(t1, 200, 860)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 21
        elif key == arcade.key.DOWN:
            self.player.change_y = -10
        elif key == arcade.key.LEFT:
            self.player.change_x = -10
        elif key == arcade.key.RIGHT:
            self.player.change_x = 10

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def update(self, dt):

        self.player.update(dt)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_bndry = self.view_left + 500
        if self.player.left < left_bndry:
            self.view_left -= left_bndry - self.player.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN - 400
        if self.player.right > right_bndry:
            self.view_left += self.player.right - right_bndry
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # check for collision with key
        if arcade.check_for_collision(self.player, self.yellow_key):
            for p in self.walls:
                if p is self.wood_door:
                    self.walls.remove(p)
            self.yellow_key.kill()

        # check for collision with door 1
        if arcade.check_for_collision(self.player, self.wood_door):
            self.wood_door.kill()

        # check for collision with death spots
        if arcade.check_for_collision_with_list(self.player, self.death_spots):
            self.player.change_y = 15
            print("player hit")

        # check for collision with springs
        if arcade.check_for_collision_with_list(self.player, self.springs):
            self.player.change_y = 30

        # check for collision with goals
        if arcade.check_for_collision_with_list(self.player, self.goals):

            for sprite in self.all_sprites_list:
                if sprite in self.walls:
                    self.walls.remove(sprite)
                self.all_sprites_list.remove(sprite)

            # reset terrain lists
            self.all_sprites_list = None
            self.all_sprites_list = arcade.SpriteList()
            self.walls = None
            self.walls = arcade.SpriteList()
            self.all_sprites_list.append(self.player)

            # change old variables
            self.level += 1
            self.background = arcade.load_texture("images/bg_grasslands.png")
            self.background2 = arcade.load_texture("images/bg_grasslands.png")
            self.background3 = arcade.load_texture("images/bg_grasslands.png")

            # draw new level
            draw_map(self, "map2.csv")
            self.all_sprites_list.draw()
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                                 self.walls, 1.0)
            # spawn player at start of new level
            self.player.center_x = 200
            self.player.center_y = 355



def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()
