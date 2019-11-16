import numpy as np
from colour import Color
from customutils2.manimutils.make_scene import make_scene
from manimlib.animation.composition import LaggedStartMap
from manimlib.animation.creation import ShowCreation
from manimlib.animation.fading import FadeIn
from manimlib.constants import *
from manimlib.mobject.geometry import Circle, Square, Line, Dot, Arrow, Triangle
from manimlib.mobject.svg.svg_mobject import SVGMobject
from manimlib.mobject.svg.tex_mobject import TexMobject, TextMobject
from manimlib.mobject.types.vectorized_mobject import VMobject, VGroup
from manimlib.scene.scene import Scene
from manimlib.utils.rate_functions import linear


class Waiting(Scene):

    def construct(self):
        self.wait()


class TestingPointFromProportion(Scene):

    def construct(self):
        obj = SVGMobject("dvsv").scale(3)

        points = VGroup(*[Dot(obj.point_from_proportion(alpha)) for alpha in np.linspace(0, 1, 33)])

        self.add(obj)
        self.add(points)
        self.wait()


if __name__ == '__main__':
    make_scene(TestingPointFromProportion)
