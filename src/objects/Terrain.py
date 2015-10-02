'''
Created on 2/10/2015

@author: probercame
'''
from random import randint

class Terrain(object):
    '''
    The terrain object automatically generates terrain using fractals
    '''

    MAX_X = 128
    '''Width of the terrain'''
    MAX_Y = 128
    '''Height of the terrain'''
    MAX_Z = 128
    '''Depth of the terrain'''

    points = {}
    noise = {}

    def generateTerrain(self):
        '''Generates the terrain and stores it in points'''
        self.generateNoise()

    def generateNoise(self):
        '''Generates the noise map'''
        indX = 0
        while (indX < self.MAX_X):
            indZ = 0
            while (indX < self.MAX_X):
                self.noise[indX][indZ] = randint(0,self.MAX_Y-1)
                indZ+=1
            indX+=1

    def __init__(self, params):
        '''
        Constructor
        '''
        self.generateTerrain()


    def toString(self):
        print ('Max X: ' + str(self.MAX_X))
        print ('Max Y: ' + str(self.MAX_Y))
        print ('Max Z: ' + str(self.MAX_Z))