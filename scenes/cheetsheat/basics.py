from colour import Color
from customutils2.manimutils.make_scene import make_scene
from manimlib.animation.composition import LaggedStartMap
from manimlib.animation.creation import Write, ShowCreation
from manimlib.constants import *
from manimlib.mobject.geometry import Line
from manimlib.mobject.svg.tex_mobject import TextMobject
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.scene.scene import Scene
from manimlib.utils.rate_functions import smooth, linear


class SceneAndConfig(Scene):
    """
    All manim scenes inherit the Scene class.
    All manim classes can have a configuration dictionary CONFIG, contents of which are
    recursively merged, the youngest child having the highest priority.
    """
    CONFIG = {
        "some_property": "some value",
        # Overriding configuration of parent class
        # Background color can be changed this way, but not resolution or fps
        "camera_config": {"background_color": Color("red")},
    }

    def construct(self):
        """
        All drawing is done in this method.
        """
        # Properties defined in CONFIG are put in self.__dict__ after merging
        # Therefore they can be treated as fields of the class
        # IDEs don't like this
        print(self.some_property)


class Updaters(Scene):
    # TODO
    def construct(self):
        pass


class PlayAnimationsBackwards(Scene):

    def construct(self):
        text = TextMobject("Hello")

        # Just run rate_func backward
        self.play(Write(text, rate_func=lambda t: smooth(1 - t)))
        self.wait()


class LaggedStartMapHowTo(Scene):

    def construct(self):
        # construction of demo props
        lines = VGroup()
        for i in range(-5, 6):
            lines.add(Line(3 * UP + i * RIGHT, 3 * DOWN + i * RIGHT))

        # LaggedStartMap is used when you want to apply one animation to lots of mobjects
        # with lagged start

        # run_time is for the whole LaggedStartMap animation, not for individual animations
        # lag_ratio - how much does it wait before running next animation (as a ratio of the time
        # of one animation)
        # rate_func applies for individual animations, launching the animations is always linear,
        # because lag_ratio is constant
        self.play(LaggedStartMap(ShowCreation, lines, run_time=10, lag_ratio=0.5, rate_func=linear))
        self.wait()


if __name__ == '__main__':
    make_scene(PlayAnimationsBackwards)
