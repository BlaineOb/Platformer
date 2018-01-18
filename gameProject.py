import arcade
import mapMaker
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
VIEWPORT_MARGIN = 40
SPRITE_SCALING = .5
BULLET_SPEED = 11

#TODO:
"""
-Level Design
    ~Vertical Level
-Enemies
-Animation for springs?
-Fix collision box for downward snow spikes -- it's too big
-Title Screen
-Level Select
-Saves
-Death penalty
-Boss Fight
-Ladders
"""

class Bullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.player = None
        self.walls = None
        self.death_spots_up = None
        self.death_spots_down = None
        self.bullets = None
        self.destructibles = None
        self.items = None
        self.springs = None
        self.goals = None
        self.background = None
        self.background2 = None
        self.background3 = None
        self.background4 = None
        self.background5 = None
        self.background6 = None
        self.background7 = None
        self.physics_engine = None
        self.all_sprites_list = None
        self.keys = None
        self.gems = None
        self.doors = None
        self.x_traveled = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.num_keys = 0
        self.level = 1
        self.view_bottom = 0
        self.view_left = 0

    def setup_player(self):

        self.player.key = None
        self.player.lives = 5
        self.player.gems = 0

        self.player.center_x = 4000
        self.player.center_y = 300

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("images/player_stand.png",
                                                             scale=.5))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("images/player_stand.png",
                                                            scale=.5, mirrored=True))
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture("images/player_walk1.png",
                                                            scale=.5, mirrored=False))
        self.player.walk_right_textures.append(arcade.load_texture("images/player_walk2.png",
                                                            scale=.5, mirrored=False))
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture("images/player_walk1.png",
                                                                   scale=.5, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/player_walk2.png",
                                                                   scale=.5, mirrored=True))
        self.player.walk_up_textures = []
        self.player.walk_up_textures.append(arcade.load_texture("images/player_jump.png",
                                                                  scale=.5, mirrored=False))

    def setup(self):

        self.walls = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.springs = arcade.SpriteList()
        self.gems = arcade.SpriteList()
        self.death_spots_up = arcade.SpriteList()
        self.death_spots_down = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.destructibles = arcade.SpriteList()
        self.goals = arcade.SpriteList()
        self.keys = arcade.SpriteList()
        self.doors = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()
        self.setup_player()

        self.background = arcade.load_texture("images/colored_grass.png")
        self.background2 = arcade.load_texture("images/colored_land.png")
        self.background3 = arcade.load_texture("images/colored_grass.png")
        self.background4 = arcade.load_texture("images/colored_land.png")
        self.background5 = arcade.load_texture("images/colored_land.png")
        self.all_sprites_list.append(self.player)

        mapMaker.draw_map(self, "map.csv")

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.walls, 1.0)


    def on_draw(self):
        arcade.start_render()
        # load backgrounds 1-6
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 1.5, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 2.25, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background3)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 3, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background4)

        arcade.draw_texture_rectangle(SCREEN_WIDTH * 3.75, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background5)
        if (self.background6 is not None):
            arcade.draw_texture_rectangle(SCREEN_WIDTH * 4.8754, SCREEN_HEIGHT // 2,
                                          SCREEN_WIDTH * 1.25, SCREEN_HEIGHT, self.background6)

        if (self.background7 is not None):
            arcade.draw_texture_rectangle(SCREEN_WIDTH * 6, SCREEN_HEIGHT // 2,
                                          SCREEN_WIDTH, SCREEN_HEIGHT, self.background7)

        self.all_sprites_list.draw()
        self.draw_text()

    def draw_text(self):
        if self.level == 1:
            t1 = arcade.create_text("Level 1", arcade.color.BLACK, 20)
            arcade.render_text(t1, 200, 860)
        elif self.level == 2:
            t1 = arcade.create_text("Level 2", arcade.color.BLACK, 20)
            arcade.render_text(t1, 200, 860)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_x = x
        self.mouse_y = y

    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            # Jump up
            if self.physics_engine.can_jump():
                self.player.change_y = 21
        elif key == arcade.key.S:
            # Go down
            self.player.change_y = -10
        elif key == arcade.key.A:
            # Go Left
            self.player.change_x = -10
        elif key == arcade.key.D:
            # Go Right
            self.player.change_x = 10
        elif key == arcade.key.F:
            # Fire Bullet
            bullet = Bullet("images/laserPurple.png")

            start_x = self.player.center_x
            start_y = self.player.center_y
            bullet.center_x = start_x
            bullet.center_y = start_y

            dest_x = self.mouse_x + self.view_left
            dest_y = self.mouse_y
            print(dest_x)
            print(dest_y)

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            print(angle)

            bullet.angle = math.degrees(angle)
            bullet.change_x = math.cos(angle) * BULLET_SPEED
            bullet.change_y = math.sin(angle) * BULLET_SPEED

            self.all_sprites_list.append(bullet)
            self.bullets.append(bullet)


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(self.player.center_x + x, y)

    def update_player(self, dt):

        if self.player.left < 1:
            self.player.left = 1
        elif self.player.right > SCREEN_WIDTH + 5501:
            self.player.right = SCREEN_WIDTH + 5500

        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT - 1:
            self.player.top = SCREEN_HEIGHT - 1

    def update(self, dt):

        self.update_player(dt)
        self.player.update_animation()
        self.physics_engine.update()

        # if player has no lives left, end game here

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

        if changed and self.view_left > 0:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
        # update bullets
        for bullet in self.bullets:

            bullet.update()

            hit_list = arcade.check_for_collision_with_list(bullet, self.destructibles)

            if len(hit_list) > 0:
                bullet.kill()

            for destructible in hit_list:
                destructible.kill()

            if bullet.left > self.player.center_x + SCREEN_WIDTH or bullet.right < 0:
                bullet.kill()

        # check for collision with key
        if arcade.check_for_collision_with_list(self.player, self.keys):
            collision_list = arcade.check_for_collision_with_list(self.player, self.keys)
            for key in collision_list:
                self.num_keys += 1
                key.kill()
            # make all doors open
            for door in self.doors:
                for wall in self.walls:
                    if wall is door:
                        self.walls.remove(wall)

        # check for collision with doors
        if arcade.check_for_collision_with_list(self.player, self.doors):
            if self.num_keys > 0:
                self.num_keys -= 1
                collision_list = arcade.check_for_collision_with_list(self.player, self.doors)
                for door in collision_list:
                    door.kill()

                # close all doors again if no more keys are left
                for door in self.doors:
                    self.walls.append(door)

        # check for collision with gems
        if arcade.check_for_collision_with_list(self.player, self.gems):
            collision_list = arcade.check_for_collision_with_list(self.player, self.gems)
            for gem in collision_list:
                gem.kill()
                self.player.gems += 1
                print(self.player.gems)

        # check for collision with upward facing death spots
        if arcade.check_for_collision_with_list(self.player, self.death_spots_up):
            self.player.change_y = 15
            self.player.lives -= 1
            print("player hit")

        # check for collision with downward facing death spots
        if arcade.check_for_collision_with_list(self.player, self.death_spots_down):
            self.player.change_y = -15
            self.player.lives -= 1
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
            self.death_spots_up = None
            self.death_spots_up = arcade.SpriteList()
            self.death_spots_down = None
            self.death_spots_down = arcade.SpriteList()
            self.springs = None
            self.springs = arcade.SpriteList()

            self.level += 3

            if (self.level == 2) :
                # change old variables
                self.background = arcade.load_texture("images/glacial_mountains.png")
                self.background2 = arcade.load_texture("images/glacial_mountains.png")
                self.background3 = arcade.load_texture("images/glacial_mountains.png")
                self.background4 = arcade.load_texture("images/glacial_mountains.png")
                self.background5 = arcade.load_texture("images/glacial_mountains.png")

                # draw new level
                mapMaker.draw_map(self, "map2.csv")
                self.all_sprites_list.draw()
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                                     self.walls, 1.0)
            #TODO: Sort out load order of levels
            elif (self.level == 3):
                # change old variables
                self.background = arcade.load_texture("images/colored_grass.png")
                self.background2 = arcade.load_texture("images/colored_land.png")
                self.background3 = arcade.load_texture("images/colored_grass.png")
                self.background4 = arcade.load_texture("images/colored_land.png")
                self.background5 = arcade.load_texture("images/colored_land.png")
                self.background6 = arcade.load_texture("images/colored_grass.png")
                self.background7 = arcade.load_texture("images/colored_grass.png")

                # draw new level
                mapMaker.draw_map(self, "map3.csv")
                self.all_sprites_list.draw()
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                                     self.walls, 1.0)

            elif (self.level == 4):
                # change old variables
                self.background = arcade.load_texture("images/sea.png")
                self.background2 = arcade.load_texture("images/sea.png")
                self.background3 = arcade.load_texture("images/sea.png")
                self.background4 = arcade.load_texture("images/sea.png")
                self.background5 = arcade.load_texture("images/sea.png")
                self.background6 = arcade.load_texture("images/sea.png")
                self.background7 = arcade.load_texture("images/sea.png")

                # draw new level
                mapMaker.draw_map(self, "map4.csv")
                self.all_sprites_list.draw()
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                                     self.walls, 1.0)

            # spawn player at start of new level
            self.player.center_x = 550
            self.player.center_y = 355



def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()
