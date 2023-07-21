import pytest
from dragonballweb.scenes import *


def test_thesaurus():
    assert thesaurus('kamehameha') == 'beam'
    assert thesaurus('what') == 'error'
    assert thesaurus('BEAM') == 'beam'
    assert thesaurus('beam shoot') == 'beam'
    assert thesaurus('shoot beam') == 'beam'
    assert thesaurus('what WHAT who JOAN') == 'crone'

def test_scene():
    fake = Scene('FakeScene', 'This is a fake Scene.')
    assert fake.name == 'FakeScene'
    assert fake.choices == {}

def test_scene_choices():
    center = Scene('Center', "Test room in the center.")
    north = Scene('North', 'Test room in the north.')
    south = Scene('South', 'Test room in the south.')

    center.add_choices({'north': north, 'south': south})
    assert center.choose('north') == north
    assert center.choose('south') == south

def test_all_choices():
    assert intro.choose('tail') == intro_tail
    assert intro.choose('beam') == intro_beam
    assert intro.choose('swim') == intro_swim
    assert intro.choose('nimbus') == intro_nimbus
    assert intro.choose('pole') == intro_pole
    assert intro.choose('image') == intro_image
    assert intro.choose('crone') == intro_crone
    assert intro.choose('hint') == intro_hint
    assert intro.choose('error') == intro_error

    print(error.name)
    print(error.description)

    print(intro_error.name)
    print(intro_error.description)

    assert intro_tail.choose('next') == goons
    assert intro_beam.choose('next') == goons
    assert intro_swim.choose('back') == intro
    assert intro_nimbus.choose('back') == intro
    assert intro_pole.choose('back') == intro
    assert intro_image.choose('back') == intro
    assert intro_crone.choose('back') == intro
    assert intro_hint.choose('back') == intro

    assert goons.choose('fight') == goons_fight
    assert goons.choose('pole') == goons_pole
    assert goons.choose('beam') == goons_beam
    assert goons.choose('image') == goons_image
    assert goons.choose('hint') == goons_hint
    assert goons.choose('error') == error

    assert goons_fight.choose('next') == goons_win
    assert goons_pole.choose('next') == goons_win
    assert goons_beam.choose('next') == goons_win
    assert goons_image.choose('next') == goons_win
    assert goons_hint.choose('back') == goons
    assert goons_win.choose('next') == chartreuse

    # assert chartreuse.choose('red') == chartreuse
    assert chartreuse.choose('green') == chartreuse_green
    # assert chartreuse_green.choose('yell') == round1
    assert round1.choose('next') == round2

    assert round2.choose('fight') == round2_fight
    assert round2.choose('beam') == round2_beam
    assert round2.choose('pole') == round2_pole
    assert round2.choose('nimbus') == round2_nimbus
    assert round2.choose('image') == round2_image
    assert round2.choose('hint') == round2_hint
    assert round2.choose('error') == error

    assert round2_fight.choose('back') == round2
    assert round2_beam.choose('back') == round2
    assert round2_pole.choose('back') == round2
    assert round2_nimbus.choose('back') == round2
    assert round2_image.choose('next') == piper
    assert round2_hint.choose('back') == round2

    assert piper.choose('fight') == piper_fight
    assert piper.choose('beam') == piper_beam
    assert piper.choose('pole') == piper_pole
    assert piper.choose('nimbus') == piper_nimbus
    assert piper.choose('image') == piper_image
    assert piper.choose('hint') == piper_hint
    assert piper.choose('error') == error

    assert piper_fight.choose('back') == piper
    assert piper_beam.choose('back') == piper
    assert piper_pole.choose('next') == chase
    assert piper_nimbus.choose('back') == piper
    assert piper_image.choose('back') == piper
    assert piper_hint.choose('back') == piper

    assert chase.choose('fight') == chase_fight
    assert chase.choose('beam') == chase_beam
    assert chase.choose('nimbus') == chase_nimbus
    assert chase.choose('image') == chase_image
    assert chase.choose('hint') == chase_hint
    assert chase.choose('error') == error

    assert chase_fight.choose('back') == chase
    assert chase_beam.choose('back') == chase
    assert chase_nimbus.choose('next') == chase2
    assert chase_image.choose('back') == chase
    assert chase_hint.choose('back') == chase

    assert chase2.choose('fight') == chase2_fight
    assert chase2.choose('beam') == chase2_beam
    assert chase2.choose('pole') == chase2_pole
    assert chase2.choose('nimbus') == chase2_nimbus
    assert chase2.choose('image') == chase2_image
    assert chase2.choose('hint') == chase2_hint
    assert chase2.choose('error') == error

    assert chase2_fight.choose('back') == chase2
    assert chase2_beam.choose('next') == ending
    assert chase2_pole.choose('back') == chase2
    assert chase2_nimbus.choose('back') == chase2
    assert chase2_image.choose('back') == chase2
    assert chase2_hint.choose('back') == chase2
    
    assert crash.choose('restart') == intro
