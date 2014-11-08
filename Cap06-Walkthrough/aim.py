import Rasterizer
cont = GameLogic.getCurrentController()
player = cont.getOwner()
mousemove = cont.getSensor('mousemove')

Rasterizer.showMouse(0)

player.mouseX = mousemove.getXPosition()
player.mouseY = mousemove.getYPosition()
player.moveX = 0.0
player.moveY = 0.0

shoulderipo = cont.getActuator('shoulderipo')
playerrot = cont.getActuator('playerrot')
shoulder = shoulderipo.getOwner()
player.deltaMouseX =  player.mouseX - (Rasterizer.getWindowWidth() / 2)
player.deltaMouseY = player.mouseY - (Rasterizer.getWindowHeight() / 2)
player.moveX= (player.deltaMouseX - player.moveX) * player.mousefilter
player.moveY= (player.deltaMouseY - player.moveY) * player.mousefilter

player.rot -= (player.moveX * player.sensitivity)
shoulder.pitch -= (player.moveY * player.sensitivity)
GameLogic.addActiveActuator(playerrot, 1)
GameLogic.addActiveActuator(shoulderipo, 1)
	
Rasterizer.setMousePosition(Rasterizer.getWindowWidth() / 2, Rasterizer.getWindowHeight() / 2)