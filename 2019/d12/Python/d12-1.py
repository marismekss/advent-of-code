
class Moon:
    def __init__ (self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        self.potential = 0
        self.kinetic = 0
        self.total = 0

    def updatePosition (self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z


    def calculateEnergy (self):
        self.potential += abs(self.pos_x)
        self.potential += abs(self.pos_y)
        self.potential += abs(self.pos_z)

        self.kinetic += abs(self.vel_x)
        self.kinetic += abs(self.vel_y)
        self.kinetic += abs(self.vel_z)

        self.total += self.potential * self.kinetic


 

def createMoons_test ():
    #io, europa, ganymede, callisto = createMoons_test()
    moon1 = Moon(-1, 0, 2)
    moon2 = Moon(2, -10, -7)
    moon3 = Moon(4, -8, 8)
    moon4 = Moon(3, 5, -1)

    return moon1, moon2, moon3, moon4


def createMoons ():
    #io, europa, ganymede, callisto = createMoons()
    moon1 = Moon(5, 13, -3)
    moon2 = Moon(18, -7, 13)
    moon3 = Moon(16, 3, 4)
    moon4 = Moon(0, 8, 8)

    return moon1, moon2, moon3, moon4


def updateVelocity (moon1, moon2):
    ## -X-
    if moon1.pos_x > moon2.pos_x: 
        moon2.vel_x += 1 
        moon1.vel_x -= 1
    elif moon1.pos_x < moon2.pos_x:
        moon1.vel_x += 1
        moon2.vel_x -= 1

    ## -Y-
    if moon1.pos_y > moon2.pos_y: 
        moon2.vel_y += 1 
        moon1.vel_y -= 1
    elif moon1.pos_y < moon2.pos_y:
        moon1.vel_y += 1
        moon2.vel_y -= 1

    ## -Z-
    if moon1.pos_z > moon2.pos_z: 
        moon2.vel_z += 1 
        moon1.vel_z -= 1
    elif moon1.pos_z < moon2.pos_z:
        moon1.vel_z += 1
        moon2.vel_z -= 1

    return moon1, moon2


##################################

maxSteps = 1000

io, europa, ganymede, callisto = createMoons()



## --- iterate through steps ---

for step in range(1,maxSteps + 1): 

    ## --- Updating VELOCITY by applying gravity ---
    io, europa = updateVelocity(io, europa)
    io, ganymede = updateVelocity(io, ganymede)
    io, callisto = updateVelocity(io, callisto)
    europa, ganymede = updateVelocity(europa, ganymede)
    europa, callisto = updateVelocity(europa, callisto)
    ganymede, callisto = updateVelocity(ganymede, callisto)


    ## --- Updating POSITION by applying velocity ---
    io.updatePosition()
    europa.updatePosition()
    ganymede.updatePosition()
    callisto.updatePosition()




## --- Calculate energy ---
io.calculateEnergy()
europa.calculateEnergy()
ganymede.calculateEnergy()
callisto.calculateEnergy()


## --- Output results ---
sum = io.total + europa.total + ganymede.total + callisto.total
print('Total energy: ', sum)