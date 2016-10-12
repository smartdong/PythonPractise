import sys, pygame
from pygame.locals import *

class Trivia(object):
	def __init__(self, filename):
		self.data = []
		self.current = 0
		self.total = 0
		self.correct = 0
		self.score = 0
		self.scored = False
		self.failed = False
		self.wronganswer = 0
		self.colors = [white,white,white,white]