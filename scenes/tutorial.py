from manimlib.animation.creation import ShowCreation
from manimlib.animation.fading import FadeOut, FadeIn
from manimlib.animation.growing import GrowFromCenter, GrowArrow
from manimlib.animation.rotation import Rotating
from manimlib.animation.transform import Transform
from manimlib.mobject.geometry import Circle, Square, Line, Polygon, Rectangle, Ellipse, CurvedArrow, Arrow, Annulus
from manimlib.scene.scene import Scene
from manimlib.constants import *
import numpy as np

from make_scene import make_scene


class Shapes(Scene):

    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(np.array([3, 0, 0]), np.array([5, 0, 0]))
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]))

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))
        self.wait()


class Shapes2(Scene):

    def construct(self):
        circle = Circle()
        square = Square()
        line = Line((3, 0, 0), (5, 0, 0))
        triangle = Polygon((0, 0, 0), (1, 1, 0), (1, -1, 0))

        self.play(ShowCreation(circle), run_time=5)
        self.play(FadeOut(circle), GrowFromCenter(square))
        self.add(line)
        self.play(Transform(square, triangle))
        self.play(Transform(triangle))
        self.wait()


class MoreShapes(Scene):

    def construct(self):
        circle = Circle(color=PURPLE_A)

        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP + LEFT)

        circle.surround(square)

        rectangle = Rectangle(height=2, width=3)

        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2 * DOWN + 2 * RIGHT)

        pointer = CurvedArrow(2 * RIGHT, 5 * RIGHT, color=MAROON_C)

        arrow = Arrow(LEFT, UP)
        arrow.next_to(circle, DOWN + LEFT)

        rectangle.next_to(arrow, DOWN + LEFT)

        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

        self.wait()


class MoreShapes2(Scene):

    def construct(self):
        circle = Circle(color=PURPLE_A)

        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP + LEFT)

        circle.surround(square)

        rectangle = Rectangle(height=2, width=3)

        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2 * DOWN + 2 * RIGHT)

        pointer = CurvedArrow(2 * RIGHT, 5 * RIGHT, color=MAROON_C)

        arrow = Arrow(LEFT, UP)
        arrow.next_to(circle, DOWN + LEFT)

        rectangle.next_to(arrow, DOWN + LEFT)

        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

        self.wait()

if __name__ == '__main__':
    make_scene(MoreShapes2)
