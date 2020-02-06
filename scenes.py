from sys import exit
import random
from textwrap import dedent

class Engine(object):

    def __init__(self, scene):
        self.scene = scene

    def play(self):
        scene_now = self.scene.start()
        scene_end = self.scene.end('*****')

        while scene_now != scene_end:
            print("\n--------")
            next_scene = scene_now.play()
            scene_now = self.scene.scene_now(scene_now)


class Scene(object):

    def play(self):
        pass

class ChoosePath(Scene):

    path = ["""
        You come across two paths while hiking alone in the woods.
        You look down at your map and see that only the right path
        is shown on the map.
        """]

    def play(self):
        print(dedent("""
            Which path will you take?

            Will you be adventures and take the LEFT paths?

            Will you play it safe and stick with the RIGHT path?
            """))

    choice = input('Left or Right?')
    if choice == 'Right':
        print('Travel safe and enjoy the rest of your hike.')
        print(ChoosePath.path[random.radint(0,4)])
        exit(1)

    else:
        print(dedent("""
            ------------------------------------------
            The Adventure begins! Let's continue onto
                    the path of the unknown !
            """))

        return 'leftpath'

class LeftPath(Scene):

    left = ["""
            As you continue down the left path the fog keeps
            growing thicker and thicker. You hear the wind howling,
            and trees swaying in the wind. The further you walk,
            the colder your body feels.
            """]

    def play(self):
        print(dedent("""
                --------------------------------------------------
                You continue down the path until you come across a
                well. As you approach the well you hear very faint
                voices coming from it. Chills run down your spine
                as the voices get louder the closer you get to the
                well.

                You stop in your tracks and the voices turn into
                screams. Your palms start sweating as you decide
                what you should do. What if there are people trapped
                down in the well? What if it's something not from this
                world?
                """))

        choice = input('Do you continue to the well or walk by?')

        if choice == 'well':
            print(dedent("""
                    --------------------------------------------------
                    Walking towards the well the screams suddenly stop.
                    You decide to look down the well and see nothing but
                    a very dim light that seems to be miles away. You lean
                    over to get a closer look when suddenly something grabs
                    you and send you spiraling down deep and deeper into the
                    well.
                    """))

            return 'well'

        else:
            print(dedent("""
                    --------------------------------------------------
                    You quickly run past the well and continue safely
                    along the path of the unknown!
                    """))
            print(LeftPath.left[random.radint(0,4)])
            exit(1)


class Well(Scene):


    def play(self):
        print(dedent("""
                --------------------------------------------------
                You wake up on a cold wet ground. You slowly open your
                eyes and see dead trees and dead plants everywhere. Ashes
                fall from the sky. You stand up and wonder "Where the hell
                am I?" You spot a door off to your right and walk towards it.
                The door is tall, red and carved onto it are intricit little
                designs and figures of people.

                Part of you is drawn to the door. An energy is urging you
                to open it. But part of you knows that what ever is hidden
                behind the door might not be safe. You contimplate exploring
                the area that you unexpectedly fell into.
                """))

        choice = input('Open the door? yes or no?')

        if choice == 'open':
            print(dedent("""
                    --------------------------------------------------
                    A gust of wind blows you onto the ground. A bright
                    light blinds you for a few seconds. You peer past the
                    door and see a parking lot? There in the parking lot
                    is your car where you left it before your hike. You
                    step through the door and start running towards your car.
                    You feel something running behind you but are too scared
                    to turn around. You reach your car door only to realize
                    you dont have your keys. You quickly tun around to only
                    see a pair of black eyes and then nothing.....
                    """))

            return 'car'

        else:
            print(dedent("""
                    --------------------------------------------------
                    You start walking through the dark, ash filled forest.
                    High pitched screams could be heard in the distance.
                    You chicken out and run towards the door, open it and
                    fall through.
                    """))
            return 'car'

class Car(Scene):

    def play(self):
        print(dedent("""
                --------------------------------------------------
                --------------------------------------------------
                Your eyes shoot open and you suddenly gasp for air.
                You wake up drenched in sweat and your arms covered
                in mud. You look around to realize your sitting in
                your car. The bag of of brain melters are sitting in
                the passenger seat of your car. You realize that you
                never left your car and you were just having a really
                bad trip.
                --------------------------------------------------
                --------------------------------------------------
                """))

class stuff(object):

    scenes = {'choosepath': ChoosePath(), 'leftpath': LeftPath(), 'well': Well(), 'car': Car()}

    def __init__(self, scene_1):
        self.scene_1 = scene_1

    def scene_now(self, chapter):
        point = Contents.scenes.get(point)
        return point

    def start(self):
        return self.scene_now(self.scene_1)
