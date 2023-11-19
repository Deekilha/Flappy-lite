import pygame
import pytest
from flappybird import*
import unittest
from flappybird import Bird
from flappybird import Bird, PipePair, load_images, frames_to_msec, msec_to_frames


class TestBird(unittest.TestCase):
    def setUp(self):
        self.bird = Bird(0, 0, 0, None)

    def test_update(self):
        # Test that the bird moves down when there is no climb time left
        self.bird.msec_to_climb = 0
        initial_y = self.bird.x
        self.bird.update()
        self.assertGreater(self.bird.x, initial_y)

        # Test that the bird moves up when there is climb time left
        self.bird.msec_to_climb = Bird.CLIMB_DURATION
        initial_y = self.bird.x
        self.bird.update()
        self.assertLess(self.bird.x, initial_y)

def test_bird():
    #self =< Bird Sprite(in 0 groups)>, x = 0, y = 0, msec_to_climb = 0, images = [0]

    def __init__(self, x, y, msec_to_climb, images):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images[0]
    bird = Bird(0, 0, 0, [2])
    assert bird.x == 0
    assert bird.y == 0
    assert bird.msec_to_climb == 0
    assert bird.self._img_wingup == 0 
    assert bird.self._img_wingdown == 0

def test_pipe_pair():
    pipe_pair = PipePair(2, 1)
    assert pipe_pair.x == 568
    assert pipe_pair.score_counted == False

@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_frames_conversion():
    assert frames_to_msec(40) == 666.6666666666666 
    assert msec_to_frames(1000) == 60

def test_bird_initialization(setup_pygame):

    images = load_images()
    bird = Bird(50, 100, 2, (images['images/bird_wing_up.png'], images['images/bird_wing_down.png']))
    assert bird.x == 50
    assert bird.y == 100
    assert bird.msec_to_climb == 3
    assert bird.image is not None
    assert bird.mask is not None
    assert isinstance(bird.rect, pygame.Rect)

def test_pipe_pair_initialization():
    images = load_images()
    pipe_pair = PipePair(images['images/pipe_end.png'], images['images/pipe_body.png'])
    assert pipe_pair.x == 568.0  # Check the default starting position
    assert pipe_pair.score_counted is False
    assert pipe_pair.image is not None
    assert pipe_pair.mask is not None
    assert pipe_pair.top_height_px == 0
    assert pipe_pair.bottom_height_px == 0
    assert pipe_pair.visible is False
    assert isinstance(pipe_pair.rect, pygame.Rect)

# Add more test cases as needed...
if __name__ == '__main__':
    pytest.main()