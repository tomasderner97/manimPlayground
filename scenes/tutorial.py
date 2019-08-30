import random

import math

from manimlib.mobject.coordinate_systems import NumberPlane
from math import factorial
import numpy as np
from manimlib.animation.creation import ShowCreation, Write
from manimlib.animation.fading import FadeOut, FadeIn
from manimlib.animation.growing import GrowFromCenter, GrowArrow
from manimlib.animation.rotation import Rotating
from manimlib.animation.transform import Transform, ApplyMethod
from manimlib.constants import *
from manimlib.mobject.geometry import Circle, Square, Line, Polygon, Rectangle, Ellipse, CurvedArrow, Arrow, Annulus, \
    Vector
from manimlib.mobject.shape_matchers import BackgroundRectangle, SurroundingRectangle
from manimlib.mobject.svg.brace import Brace
from manimlib.mobject.svg.tex_mobject import TextMobject, TexMobject
from manimlib.mobject.types.vectorized_mobject import VGroup, VectorizedPoint
from manimlib.scene.graph_scene import GraphScene
from manimlib.scene.scene import Scene

from customutils2.manimutils.make_scene import make_scene


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

        circle2 = Circle()
        circle2.surround(rectangle, buffer_factor=1)

        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.add(circle2)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

        self.wait()


class AddingText(Scene):

    def construct(self):
        my_first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(my_first_text, DOWN)
        third_line = TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line, third_line))
        self.wait(2)
        second_line.shift(3 * DOWN)
        self.play(ApplyMethod(my_first_text.shift, 3 * UP))
        self.wait()


class AddingText2(Scene):

    def construct(self):
        my_first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(my_first_text, DOWN)
        third_line = TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)

        self.play(FadeIn(my_first_text),
                  FadeIn(second_line))
        self.wait(2)
        self.play(Transform(second_line, third_line))
        self.wait(2)

        self.play(ApplyMethod(my_first_text.shift, 3 * UP))
        self.play(Rotating(second_line), radians=PI, run_time=2)
        self.wait()


class AddingMoreText(Scene):

    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)

        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author = TextMobject("- Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

        self.add(quote, author)
        self.wait(2)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))
        self.wait()


class AddingMoreText2(Scene):

    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)

        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author = TextMobject("- Albert Einstein")
        author.scale(0.75)

        corner = quote.get_corner(DOWN + RIGHT)
        print("corner", corner)
        author.next_to(corner, ORIGIN)

        self.add(quote, author)
        self.wait(2)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote),
                  FadeOut(author))
        self.wait()


class RotateAndHighlight(Scene):

    def construct(self):
        square = Square(side_length=5, fill_color=YELLOW, fill_opacity=1)
        label = TextMobject("Text at an angle")
        label.bg = BackgroundRectangle(label, fill_opacity=1)
        label_group = VGroup(label.bg, label)

        label_group.rotate(TAU / 8)

        label2 = TextMobject("Boxed text", color=BLACK)
        label2.bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=.5)
        label2_group = VGroup(label2, label2.bg)
        label2_group.next_to(label_group, DOWN)

        label3 = TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait(2)


class RotateAndHighlight2(Scene):

    def construct(self):
        square = Square(side_length=5, fill_color=YELLOW, fill_opacity=1)
        label = TextMobject("Text at an angle")
        label_bg = BackgroundRectangle(label, fill_opacity=1)
        label_group = VGroup(label_bg, label)

        label_group.rotate(TAU / 8)

        label2 = TextMobject("Boxed text", color=BLACK)
        label2_bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=.5)
        label2_group = VGroup(label2, label2_bg)
        label2_group.next_to(label_group, DOWN)

        label3 = TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, GREEN, BLUE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait(2)


class BasicEquations(Scene):

    def construct(self):
        eq1 = TextMobject(r"$ \vec{X}_0 \cdot \vec{Y}_1 = 3 $")
        eq1.shift(2 * UP)

        eq2 = TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2 * DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait()


class ColoringEquations(Scene):

    def construct(self):
        line1 = TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",
                           r"\text{force}",
                           r"\text{ on object of mass }")
        line1.set_color_by_tex("force", BLUE)

        line2 = TexMobject("m",
                           r"\text{ and acceleration }",
                           r"\vec{a}",
                           ".")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })

        sentence = VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
        self.wait(3)


class ColoringEquations2(Scene):

    def construct(self):
        line1 = TextMobject(r"The vector $\vec{F}_{net}$ is the net ",
                            "force",
                            " on object of mass ")
        line1.set_color_by_tex("force", BLUE)

        line2 = TextMobject("$m$",
                            " and acceleration ",
                            r"$\vec{a}$",
                            ".")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })

        sentence = VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
        self.wait(3)


class UsingBraces(Scene):

    def construct(self):
        eq1a = TextMobject("4x + 3y")
        eq1b = TextMobject("=")
        eq1c = TextMobject("0")

        eq2a = TextMobject("5x - 2y")
        eq2b = TextMobject("=")
        eq2c = TextMobject("3")

        eq1b.next_to(eq1a, RIGHT)
        eq1c.next_to(eq1b, RIGHT)

        eq2a.shift(DOWN)
        eq2b.shift(DOWN)
        eq2c.shift(DOWN)

        eq2a.align_to(eq1a, LEFT)
        eq2b.align_to(eq1b, LEFT)
        eq2c.align_to(eq1c, LEFT)

        eq_group = VGroup(eq1a, eq2a)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1a, eq1b, eq1c)
        self.add(eq2a, eq2b, eq2c)
        self.play(GrowFromCenter(braces), Write(eq_text))

        self.wait(3)


class UsingBraces2(Scene):

    def construct(self):
        eq1a = TexMobject("4x + 3y")
        eq1b = TexMobject("=")
        eq1c = TexMobject("0")

        eq2a = TexMobject("5x - 2y")
        eq2b = TexMobject("=")
        eq2c = TexMobject("3")

        eq1b.next_to(eq1a, RIGHT)
        eq1c.next_to(eq1b, RIGHT)

        eq2a.shift(DOWN)
        eq2b.shift(DOWN)
        eq2c.shift(DOWN)

        eq2a.align_to(eq1a, LEFT)
        eq2b.align_to(eq1b, LEFT)
        eq2c.align_to(eq1c, LEFT)

        eq_group = VGroup(eq1a, eq2a)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1a))
        self.play(Write(eq1b))
        self.play(Write(eq1c))
        self.play(Write(eq2a))
        self.play(Write(eq2b))
        self.play(Write(eq2c))
        self.play(GrowFromCenter(braces), Write(eq_text))

        self.wait(3)


class Intermezzo(Scene):

    def construct(self):
        shape = Ellipse(fill_color=BLUE, fill_opacity=1)
        brace = Brace(shape, LEFT)

        self.play(Write(shape), GrowFromCenter(brace))
        self.wait(2)


class UsingBracesConcise(Scene):

    def construct(self):
        eq1_text = "4 x + 3 y = 0".split()
        eq2_text = "5 x - 2 y = 3".split()

        eq1_mob = TexMobject(*eq1_text)
        eq2_mob = TexMobject(*eq2_text)

        color_map = {
            "x": RED_B,
            "y": GREEN_C
        }
        eq1_mob.set_color_by_tex_to_color_map(color_map)
        eq2_mob.set_color_by_tex_to_color_map(color_map)

        for eq1_item, eq2_item in zip(eq1_mob, eq2_mob):
            eq2_item.align_to(eq1_item, LEFT)

        eq1 = VGroup(*eq1_mob)
        eq2 = VGroup(*eq2_mob)
        eq2.shift(DOWN)

        eq_group = VGroup(eq1, eq2)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq_text))
        self.play(GrowFromCenter(braces))
        self.play(Write(eq1), Write(eq2))
        self.wait(2)


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2)
    }

    def construct(self):
        self.setup_axes(animate=True)

        func_graph = self.get_graph(self.func_to_graph, color=RED)
        func_graph2 = self.get_graph(self.func_to_graph2)

        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label=r"\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label=r"\sin(x)", x_val=-10, direction=UP / 2)

        two_pi = TexMobject(r"x = 2 \pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait(2)

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)


class PlotFunctions2(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "y_bottom_tick": -1,
        "graph_origin": ORIGIN,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
    }

    def construct(self):
        self.setup_axes(animate=True)

        func_graph = self.get_graph(self.func_to_graph, color=RED)
        func_graph2 = self.get_graph(self.func_to_graph2)

        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label=r"\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label=r"\sin(x)", x_val=-10, direction=LEFT)

        two_pi = TexMobject(r"x = 2 \pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait(2)

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "x_labeled_nums": range(-10, 12, 2)
    }

    def taylor(self, x, n):
        res = 1
        for i in range(1, n + 1):
            res += (-1) ** i * x ** (2 * i) / factorial(2 * i)

        return res

    def construct(self):
        N = 15

        self.setup_axes(animate=True)

        func_graph = self.get_graph(np.cos, color=BLUE)
        approx_graphs = [self.get_graph(lambda x: self.taylor(x, n), color=GREEN) for n in range(0, N)]

        term_nums = [TexMobject(f"n = {n}", aligned_edge=TOP) for n in range(0, N)]
        term = VectorizedPoint()
        term.to_edge(BOTTOM, buff=SMALL_BUFF)

        for term_num in term_nums:
            term_num.to_edge(BOTTOM, buff=SMALL_BUFF)

        approx_graph = VectorizedPoint(self.input_to_graph_point(0, func_graph))

        self.play(ShowCreation(func_graph))
        for graph, term_num in zip(approx_graphs, term_nums):
            self.play(Transform(approx_graph, graph, run_time=1), Transform(term, term_num))
            self.wait()

        self.wait()


class DrawAnAxis(Scene):

    def construct(self):
        my_plane = NumberPlane(x_line_frequency=2,
                               y_line_frequency=2,
                               faded_line_ratio=2)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        self.wait()


class SimpleField(Scene):

    def construct(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels())
        self.add(plane)

        points = [x * RIGHT + y * UP for x in np.arange(-5, 5, 1) for y in np.arange(-5, 5, 1)]

        vec_field = []
        for point in points:
            field = 0.5 * RIGHT + 0.5 * UP
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field)

        self.play(ShowCreation(draw_field))
        self.wait(2)


# noinspection PyAttributeOutsideInit
class MovingCharges(Scene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B,
        },
        "point_charge_loc": 0.5 * RIGHT - 1.5 * UP,
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        self.field = VGroup(*[self.calc_field(x * RIGHT + y * UP)
                              for x in np.arange(-9, 9, 1)
                              for y in np.arange(-5, 5, 1)
                              ])

        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(self.field))
        self.moving_charge()

    def calc_field(self, point):
        x, y = point[:2]
        Rx, Ry = self.point_charge_loc[:2]
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return Vector(efield).shift(point)

    def field_at_point(self, point):
        x, y = point[:2]
        Rx, Ry = self.point_charge_loc[:2]
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return efield

    def moving_charge(self):
        num_charges = 4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, num_charges)

        particles = VGroup(*[self.Positron().move_to(point) for point in points])
        for particle in particles:
            particle.velocity = np.array((0, 0, 0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles)
        self.always_continually_update = True
        self.wait(10)

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel * dt
                p.shift(p.velocity * dt)

    class Positron(Circle):
        CONFIG = {
            "radius": 0.2,
            "stroke_width": 3,
            "color": RED,
            "fill_color": RED,
            "fill_opacity": 0.5,
        }

        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


if __name__ == '__main__':
    make_scene(MovingCharges,
               video_dir="../video",
               tex_dir="../tex")
