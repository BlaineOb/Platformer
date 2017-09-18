import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
VIEWPORT_MARGIN = 40

"""-Add death spots
   -Figure out screen scrolling
   -Flesh out level design
   -Figure out how to load second level
   -Enemies?"""

class Player(arcade.Sprite):

    def update(self, dt):
        """ Move everything """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH + 2001:
            self.right = SCREEN_WIDTH + 2000

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.goal = None
        self.player = None
        self.walls = None
        self.background = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        arcade.set_background_color(arcade.color.DARK_LAVA)

    def setup(self):

        self.walls = arcade.SpriteList()
        self.player = Player("images/player_stand.png", 0.5)
        self.player.center_x = 200
        self.player.center_y = 115

        self.background = arcade.load_texture("images/colored_grass.png")

        """level one ground"""
        for x in range(0, 360, 60):
            wall = arcade.Sprite("images/grass.png", 0.5)
            wall.center_x = x
            wall.center_y = 50
            self.walls.append(wall)
        """level one ground"""
        for x in range(540, 800, 60):
            wall = arcade.Sprite("images/grass.png", 0.5)
            wall.center_x = x
            wall.center_y = 50
            self.walls.append(wall)
        """level two ground"""
        for x in range(0, 600, 60):
            wall = arcade.Sprite("images/grass.png", 0.5)
            wall.center_x = x
            wall.center_y = 450
            self.walls.append(wall)
        """wall 1"""
        for y in range(50, 450, 63):
            wall = arcade.Sprite("images/grassCenter_round.png", 0.5)
            wall.center_x = 840
            wall.center_y = y
            self.walls.append(wall)

        for x in range(840, 2830, 63):
            wall = arcade.Sprite("images/grass.png", 0.5)
            wall.center_x = x
            wall.center_y = 650
            self.walls.append(wall)

        self.goal = arcade.Sprite("images/stone.png", 0.5)
        self.goal.center_x = 776
        self.goal.center_y = 115


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.walls, 2.0)


    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        arcade.draw_texture_rectangle(SCREEN_WIDTH, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH * 2, SCREEN_HEIGHT, self.background)

        self.walls.draw()
        self.player.draw()
        self.goal.draw()

        self.t1 = arcade.create_text("Try bouncing", arcade.color.BLACK, 12)
        arcade.render_text(self.t1, 500, 500)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 20
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

        if arcade.check_for_collision(self.player, self.goal):
            self.player.change_y = 30

        self.player.update(dt)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_bndry = self.view_left - 10
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

def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()
