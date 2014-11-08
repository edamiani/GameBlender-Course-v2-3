from math import sqrt

def VEC_length(x):
	return sqrt(x[0]*x[0]+x[1]*x[1]+x[2]*x[2])

def VEC_normalize(x): 
	length = VEC_length(x)
	return [x[0]/length,x[1]/length,x[2]/length]

def VEC_mul(s, x):
	return [s * x[0], s * x[1], s * x[2]]

def VEC_add(x, y):
	return [x[0] + y[0], x[1] + y[1], x[2] + y[2]]

cont = GameLogic.getCurrentController()

fwdkey = cont.getSensor('fwdkey')
backkey = cont.getSensor('backkey')
leftkey = cont.getSensor('leftkey')
rightkey = cont.getSensor('rightkey')

floormove = cont.getActuator('floormove')
GameLogic.addActiveActuator(floormove, 0)

player = cont.getOwner()
speed = player.maxspeed
vec = [0, 0, 0]

if player.flymode:
	shoulder = cont.getActuator('shoulderipo').getOwner()
	playerOri = shoulder.getOrientation()

else:
	playerOri = player.getOrientation()

playerX = [playerOri[0][0], playerOri[1][0], playerOri[2][0]]
playerY = [playerOri[0][1], playerOri[1][1], playerOri[2][1]]

if fwdkey.isPositive():
	vec = VEC_add(vec, playerY)

if backkey.isPositive():
	vec = VEC_add(vec, VEC_mul(-1, playerY))

if rightkey.isPositive():
	vec = VEC_add(vec, playerX)

if leftkey.isPositive():
	vec = VEC_add(vec, VEC_mul(-1, playerX))

if vec == [0, 0, 0]:
	GameLogic.addActiveActuator(floormove, 0)

else:
	vec = VEC_normalize(vec)
	vel = VEC_mul(speed, vec)
	floormove.setLinearVelocity(vel[0], vel[1], vel[2], 0)
	GameLogic.addActiveActuator(floormove, 1)

