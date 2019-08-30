from customutils2.manimutils.make_scene import make_scene
from manimlib.animation.fading import FadeIn
from manimlib.constants import *
from manimlib.mobject.geometry import Circle
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.scene.scene import Scene


class Waiting(Scene):

    def construct(self):
        self.wait()


class BasicAnim(Scene):

    def construct(self):
        circle = Circle()

        self.play(FadeIn(circle))
        self.wait()


if __name__ == '__main__':
    make_scene(BasicAnim,
               video_dir="../video",
               tex_dir="../tex",)
