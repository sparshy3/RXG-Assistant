import numpy as np
import scipy as sp
# map (RGBYOW) -> (123456)
class rxc:
  solved_state = np.array([])
  def __init__(self):
    self.state = self.solved_state
  def scramble(self, len):
      alg = np.array([])
      self.applyAlg(alg)
  def applyAlg(self, alg):
    for i in alg:
      self.turn(i)
  def turn(self, move)
    curr = 
    new = 
    self.state = new
