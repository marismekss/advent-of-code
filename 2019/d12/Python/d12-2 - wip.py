
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



#function Get-GCD ($a, $b)  {
#    function pgcd ($n, $m)  {
#        if($n -le $m) { 
#            if($n -eq 0) {$m}
#            else{pgcd $n ($m%$n)}
#        }
#        else {pgcd $m $n}
#    }
#    $n = [Math]::Abs($a)
#    $m = [Math]::Abs($b)
#    (pgcd $n $m)
#}
#function Get-LCM ($a, $b)  {
#    [Math]::Abs($a*$b)/(Get-GCD $a $b)
#}


##################################

io, europa, ganymede, callisto = createMoons_test()


maxSteps = 400000


x1 = 5
x2 = 18
x3 = 16
x4 = 0


y1 = 13
y2 = -7
y3 = 3
y4 = 8

z1 = -3
z2 = 13
z3 = 4
z4 = 8




## --- iterate through steps ---
for step in range(1, maxSteps + 1):

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

    initialPosX = "(5,18,16,0)"
    initialVelX = "(0,0,0,0)"
    currentPosX = "($($io.position_x),$($europa.position_x),$($ganymede.position_x),$($callisto.position_x))"
    currentVelX = "($($io.velocity_x),$($europa.velocity_x),$($ganymede.velocity_x),$($callisto.velocity_x))"

    initialPosY = "(13,-7,3,8)"
    initialVelY = "(0,0,0,0)"
    currentPosY = "($($io.position_y),$($europa.position_y),$($ganymede.position_y),$($callisto.position_y))"
    currentVelY = "($($io.velocity_y),$($europa.velocity_y),$($ganymede.velocity_y),$($callisto.velocity_y))"

    initialStateZ = "($z1,$z2,$z3,$z4)"
    currentStateZ = "($($io.position_z),$($europa.position_z),$($ganymede.position_z),$($callisto.position_z))"




    #$initialState

    #If ( $currentPosX -eq $initialPosX -and $currentVelX -eq $initialVelX ) { 
    #    Write-Host "X repeats at step: $step" 
    #    break
    #}
    if currentPosY == initialPosY and currentVelY == initialVelY:
        print('Y repeats at step: ', step)
        break
    # If ( $currentStateZ -eq $initialStateZ ) { Write-Host "Z repeats at step: $step" }
           

