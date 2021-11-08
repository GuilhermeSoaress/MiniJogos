import pyxel
import random
import math

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
SKEET_MAX_SPEED = 1.8
SKEET_INITIAL_COUNT = 3
SKEET_CHANGE_SPACE = 1
points = 0


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Skeet1:
    def __init__(self):
        self.r = random.uniform(5, 10)

        self.space = Vec2(
            random.uniform(1, 256),
            random.uniform(1, 256))

        self.vel = Vec2(
            random.uniform(-SKEET_MAX_SPEED, SKEET_MAX_SPEED),
            random.uniform(-SKEET_MAX_SPEED, SKEET_MAX_SPEED))
        self.color = 7

    def update(self):
        self.space.x += self.vel.x
        self.space.y += self.vel.y

        if self.vel.x < 0 and self.space.x < self.r:
            self.vel.x *= -1
        if self.vel.x > 0 and self.space.x > SCREEN_WIDTH - self.r:
            self.vel.x *= -1
        if self.vel.y < 0 and self.space.y < self.r:
            self.vel.y *= -1
        if self.vel.y > 0 and self.space.y > SCREEN_HEIGHT - self.r:
            self.vel.y *= -1


class game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.mouse(True)
        self.skeet = [Skeet1() for _ in range(SKEET_INITIAL_COUNT)]
        pyxel.run(self.update, self.draw)

    def update(self):
        global points

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        skeet_count = len(self.skeet)

        if pyxel.btnp(pyxel.KEY_R):
            points = 0

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for i in range(skeet_count):
                skeet = self.skeet[i]
                dx = skeet.space.x - pyxel.mouse_x
                dy = skeet.space.y - pyxel.mouse_y

                if dx * dx + dy * dy < skeet.r * skeet.r:
                    new_r = random.uniform(5, 10)

                    for j in range(SKEET_CHANGE_SPACE):
                        points += 1
                        angle = random.uniform(1, 100)
                        new_skeet = Skeet1()
                        new_skeet.r = new_r
                        new_skeet.space.x = random.uniform(1, 256)
                        new_skeet.space.y = random.uniform(1, 256)
                        new_skeet.vel.x = math.cos(angle) * SKEET_MAX_SPEED
                        new_skeet.vel.y = math.sin(angle) * SKEET_MAX_SPEED
                        self.skeet.append(new_skeet)

                    del self.skeet[i]

        for i in range(skeet_count - 1, -1, -1):
            self.skeet[i].update()

    def draw(self):
        pyxel.cls(5)

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            pyxel.cls(7)

        for skeet in self.skeet:
            pyxel.circ(skeet.space.x, skeet.space.y, skeet.r, skeet.color)
            pyxel.circb(skeet.space.x, skeet.space.y, skeet.r, 0)
            pyxel.text(5, 5, f"pts:{points}", pyxel.COLOR_WHITE)


game()
