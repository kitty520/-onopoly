import random
import datetime
from time import sleep
import pygame
from pygame.locals import *
import os

pygame.init()

#顏色參數
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 100)
GREEN = (100, 225, 0)
BLUE = (0, 130, 250)
YELLOW = (255, 255, 0)

#視窗名稱
title = "112 Monopoly"

#視窗長800, 寬600
display_width = 800
display_height = 600

#color tuple (反白色, 矩形顏色, 字體顏色)
button_color = (WHITE, GRAY, BLACK)
information_color = (GRAY, BLACK, WHITE)

#畫面代號
s = 0

def text_objects(text, font, color): #把字貼到長方形上
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

# 菜單按鈕
class Menu_Button: 

	def __init__(self, msg, x, y, w, h, color):
		self.msg = msg
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ac = color[0]
		self.ic = color[1]
		self.tc = color[2]

	def Add_text(self):
		mouse = pygame.mouse.get_pos()

		if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
			pygame.draw.rect(screen, self.ac, (self.x, self.y, self.w, self.h))

		else:
			pygame.draw.rect(screen, self.ic, (self.x, self.y, self.w, self.h))

		smallText = pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\mingliu.ttc", 20)
		TextSurf, TextRect = text_objects(self.msg, smallText, self.tc)
		TextRect.center = ((self.x+(self.w/2)), (self.y+(self.h/2)))
		screen.blit(TextSurf, TextRect)

# 畫面文字
def Show_Text(font_size, show, color):
	font = pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\mingliu.ttc", font_size)
	text = font.render(show, True, color)
	return text

	
# 遊戲選單畫面（s=0）
def Game_Menu():
	
	# 畫面標題 "112 Monopoly"
	text = Show_Text(80, title, WHITE)
	x_text = (800-text.get_width()) / 2
	y_text = (300-text.get_height()) / 2
	screen.blit(text, (x_text, y_text))

	#按鈕文字
	start = "Start Game"
	quit = "Quit"
	rule = "Game Rules"

	
	# 遊戲菜單的按鈕
	start_Button = Menu_Button(start, 325, 300, 150, 50, button_color) # start game button
	start_Button.Add_text()
	rule_Button = Menu_Button(rule, 325, 400, 150, 50, button_color)
	rule_Button.Add_text()
	quit_Button = Menu_Button(quit, 325, 500, 150, 50, button_color)
	quit_Button.Add_text()

	pygame.display.update()

	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = event.pos
		
		# 如果按start
		if start_Button.x + start_Button.w > mouse_pos[0] > start_Button.x and start_Button.y + start_Button.h > mouse_pos[1] > start_Button.y:
			# 畫面變成start
			global s 
			s = 1
		
		# 規則鍵
		elif rule_Button.x + rule_Button.w > mouse_pos[0] > rule_Button.x and rule_Button.y + rule_Button.h > mouse_pos[1] > rule_Button.y:
			s = 2 # 畫面變成rules
		
		elif quit_Button.x + quit_Button.w > mouse_pos[0] > quit_Button.x and quit_Button.y + quit_Button.h > mouse_pos[1] > quit_Button.y:
			exit()
	
	if event.type == pygame.QUIT:
		exit()
			
# 輸入玩家數(s=1)
def NumPlayer():

	# 返回鍵
	back_Button = Menu_Button("Back", 0, 0, 150, 50, button_color)
	back_Button.Add_text()
	
	rule_Button = Menu_Button("Rules", 650, 0, 150, 50, button_color)
	rule_Button.Add_text()
	
	# 輸入玩家數
	NumOfPlayer = Show_Text(50, "選擇玩家人數", WHITE)
	x_text = (800-NumOfPlayer.get_width()) / 2
	y_text = (300-NumOfPlayer.get_width()) / 2
	screen.blit(NumOfPlayer, (x_text, y_text))

	x_player = 225
	
	for p in range(4):
		player1 = Menu_Button(str(p+1), x_player, 300, 50, 50, button_color)
		player1.Add_text()
		x_player += 100

	pygame.display.update()

	global player_num

	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = event.pos

		# 返回
		if back_Button.x + back_Button.w > mouse_pos[0] > back_Button.x and back_Button.y + back_Button.h > mouse_pos[1] > back_Button.y:
			global s
			s = 0

		elif rule_Button.x + rule_Button.w > mouse_pos[0] > rule_Button.x and rule_Button.y + rule_Button.h > mouse_pos[1] > rule_Button.y:
			s = 2

		elif 225 < mouse_pos[0] < (225+50) and 300 < mouse_pos[1] < 350:
			player_num =  1
			s = 4
		
		elif 325 < mouse_pos[0] < (325+50) and 300 < mouse_pos[1] < 350:
			player_num =  2
			s = 4
				
		elif 425 < mouse_pos[0] < (425+50) and 300 < mouse_pos[1] < 350:
			player_num =  3
			s = 4
			
		elif 525 < mouse_pos[0] < (525+50) and 300 < mouse_pos[1] < 350:
			player_num =  4
			s = 4
			
	if event.type == pygame.QUIT:
		exit()
		
# 輸入回合數(s=1)
def NumRound():

	# 返回鍵
	back_Button = Menu_Button("Back", 0, 0, 150, 50, button_color)
	back_Button.Add_text()
	
	rule_Button = Menu_Button("Rules", 650, 0, 150, 50, button_color)
	rule_Button.Add_text()
	
	# 輸入玩家數
	NumOfRound = Show_Text(50, "選擇回合數", WHITE)
	x_text = (800-NumOfRound.get_width()) / 2
	y_text = (300-NumOfRound.get_width()) / 2
	screen.blit(NumOfRound, (x_text, y_text))

	x_round = 225
	
	for p in range(4):
		player1 = Menu_Button(str((p+1)*10), x_round, 300, 50, 50, button_color)
		player1.Add_text()
		x_round += 100

	pygame.display.update()

	global play_round

	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = event.pos

		# 返回
		if back_Button.x + back_Button.w > mouse_pos[0] > back_Button.x and back_Button.y + back_Button.h > mouse_pos[1] > back_Button.y:
			global s
			s = 0

		elif rule_Button.x + rule_Button.w > mouse_pos[0] > rule_Button.x and rule_Button.y + rule_Button.h > mouse_pos[1] > rule_Button.y:
			s = 2

		elif 225 < mouse_pos[0] < (225+50) and 300 < mouse_pos[1] < 350:
			play_round =  10
			s = 3
		
		elif 325 < mouse_pos[0] < (325+50) and 300 < mouse_pos[1] < 350:
			play_round =  20
			s = 3
				
		elif 425 < mouse_pos[0] < (425+50) and 300 < mouse_pos[1] < 350:
			play_round =  30
			s = 3
			
		elif 525 < mouse_pos[0] < (525+50) and 300 < mouse_pos[1] < 350:
			play_round =  40
			s = 3
			
	if event.type == pygame.QUIT:
		exit()

# 遊戲規則(s=2)
def Rules():
	
	# 遊戲標題
	title = Show_Text(50, "遊戲規則", WHITE)
	x_text = (800-title.get_width()) / 2
	screen.blit(title, (x_text, 100))

	# 規則內容
	rule_text = ["1. 玩家起始金額25萬", "2. 每回合骰子的顆數1顆", "3. 該回合走到空地可執行購買或放棄的指令",  "4. 該回合走到已購買地必須繳交罰金，現金可能為負值", "5. 若該回合剛好停留在起點，可獲得1萬現金", "6. 若第二次以上走到自己的領地可增建違章建築", "7. 勝利條件：給定回合內，剩餘金額（含資產）最高的人獲勝"]
	y_text = 200
	for sentence in rule_text:
		rule = Show_Text(20, sentence, WHITE)
		x_text = (800-rule.get_width()) / 2
		screen.blit(rule, (x_text, y_text))
		y_text += 25



	# 返回鍵
	back_Button = Menu_Button("Back", 200, 500, 150, 50, button_color)
	back_Button.Add_text()
	# 開始鍵
	play_Button = Menu_Button("Play", 450, 500, 150, 50, button_color)
	play_Button.Add_text()
	
	pygame.display.update()

	
	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = event.pos
		if back_Button.x + back_Button.w > mouse_pos[0] > back_Button.x and back_Button.y + back_Button.h > mouse_pos[1] > back_Button.y:
			global s
			s = 0
		elif play_Button.x + play_Button.w > mouse_pos[0] > play_Button.x and play_Button.y + play_Button.h > mouse_pos[1] > play_Button.y:
			s = 1
			
	if event.type == pygame.QUIT:
		exit()


# 遊戲結束畫面
def Game_over():
	screen.fill((0,0,0))
	# 遊戲標題
	title = Show_Text(50, "遊戲結束", WHITE)
	x_text = (800-title.get_width()) / 2
	screen.blit(title, (x_text, 100))


	# 玩家資產
	global player_num
	global player_list

	y_text = 250
	result_column = str('%10s %10s' % ("玩家", "總資產"))
	result = Menu_Button(result_column, 0, 200, 400, 50, information_color)
	result.Add_text()	
	for plr in (player_list):
		player1_result = Menu_Button(str('%10s %10d' % (plr.name, plr.Property())), 0, y_text, 400, 50, information_color)
		player1_result.Add_text()
		y_text += 50

	global winner
	global winnert
	global winner21

	# 第一名們
	str_winner = "書卷獎得主："
	for wn in winner:
		str_winner += wn + ", "

	str_winnert = "水源阿伯常客："
	for wnt in winnert:
		str_winnert += wnt + ", "

	str_winner21 = "黑卷獎（被21最多次）得主："
	for wn21 in winner21:
		str_winner21 += wn21 + ", "

	result2 = Menu_Button("紅人榜", 400, 200, 400, 50, information_color)
	result2.Add_text()
	y_winner = 250
	if winner != []:
		winner_result = Menu_Button(str_winner[:-2], 400, y_winner, 400, 50, information_color)
		winner_result.Add_text()
		y_winner += 50
	
	if winnert != []:
		winnert_result = Menu_Button(str_winnert[:-2], 400, y_winner, 400, 50, information_color)
		winnert_result.Add_text()
		y_winner += 50
	
	if winner21 != []:
		winner21_result = Menu_Button(str_winner21[:-2], 400, y_winner, 400, 50, information_color)
		winner21_result.Add_text()


	# 離開鍵和再來一次
	quit_when_Over_Button = Menu_Button("Quit", 325, 500, 150, 50, button_color)
	quit_when_Over_Button.Add_text()

	pygame.display.update()
	
	event = pygame.event.wait()

	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_pos = event.pos
		if quit_when_Over_Button.x + quit_when_Over_Button.w > mouse_pos[0] > quit_when_Over_Button.x and quit_when_Over_Button.y + quit_when_Over_Button.h > mouse_pos[1] > quit_when_Over_Button.y:
			exit()
			
	if event.type == pygame.QUIT:
		exit()
	

Land_dict = dict()

class Player():
	def __init__(self,name,color,type = True): #Type = True(player) Type = False(computer)
		self.name = name
		self.cash = 250000
		self.asset = dict()
		self.position = 0
		self.can_move = True
		self.type = type
		self.beTowed = 0
		self.one_half = 0
		
		self.color = color
	
	def __str__(self):
		return(str(self.name))
		
	def purchase_land(self,land): #傳入Land()
		land.owner = self
		self.cash -= land.price
		self.asset[land.name] = land.price
		land.was_bought = True
		
		map.change_label(land,self)
		return '%s 購買了 %s，還剩下 %d 元，我們恭喜他'%(self.name,land.name,self.cash)
		
	def purchase_house(self,land):
		self.cash -= land.house_cost
		land.house_num += 1
		self.asset[land.name] += land.house_cost
		return '%s 在 %s 加蓋了一棟違章建築，大家趕快告發他！'%(self.name,land.name)
		
	def pay_cash(self,cash): #type(cash) = int
		self.cash -= cash

	def receive_cash(self,cash):
		self.cash += cash
		
	def move(self,map = Land_dict):
		if self.can_move == True:
			num = random.randint(1,6)
			chance = random.randint(1,20)
			
			#移動
			if self.position + num > 27:
				self.position = (num - (27 - self.position)) - 1
			else:
				self.position += num
				
			#是否觸發事件
			if chance == 1:
				self.beTowed += 1
				word(self.bikeBeTowed())
			
			return '%s 骰到了 %d 點，走到 %s 的位置'%(self.name, num, Land_dict[self.position].name)

		else:
			self.can_move = True
			return '阿……我忘記你不能骰骰子了'
	
	def bikeBeTowed(self):
		self.pay_cash(5000)
		return '水源阿伯出沒囉！拿回車被罰款 5000 元，你還剩下 %d 元'%self.cash
		
	def Property(self):
		P = sum(self.asset.values()) + self.cash
		return int(P)

class Land():
	def __init__(self, position, name, price, type, showname, place): #type = True(可購買) type = False(不可購買)
																	  #如果此地不可購買直接將price設成0
		self.position = int(position)
		self.name = name
		self.price = int(price)
		self.house_cost = int(self.price*0.2)
		self.house_num = 0
		self.payment = int((self.price + int(self.house_cost)*self.house_num)*0.15)
		self.type = type
		self.was_bought = False
		self.owner = None
		
		#Show
		self.showname = showname
		self.place = place

		Land_dict[self.position] = self
	
	def event_text(self,lst): #lst = list['line1','line2']
		self.text = random.choice(lst)
	
	def event_text_call(self):
		return self.text


#顯示下方文字
def word(text):
	screen.fill((0,0,0))
	t = font_s.render(text,True,WHITE)
	screen.blit(t,(((display_width - 90 * 8) / (8+1)),500))
	main()
	sleep(len(text)*0.05+0.5)

#顯示中間文字+按鈕
def b_word(text, choose1 = '是', choose2 = '否'):
	screen.fill((0,0,0))
	player_label(4)
	map.land_label()
	B1.button_show(choose1, choose2)
	t = font_s.render(text,True,WHITE)
	textRect = t.get_rect()
	textRect.center = ((display_width/2), display_height/2 - 130)
	screen.blit(t, textRect)
	pygame.display.update()
			

colorlist = [RED, GREEN, BLUE, YELLOW]
font_s = pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\mingliu.ttc", 20) 
font_b = pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\mingliu.ttc", 60)
		

	
#PLAYER資料方塊，輸入玩家人數
def player_label(num):
		
		#方塊的寬跟中間空隙
		label_width = 180
		label_space = (display_width - label_width * num) / (num + 1)

		#確定方塊位置
		label_loc = label_space
		
		for i in range(num):
			#畫出方塊
			pygame.draw.rect(screen, colorlist[i], ((label_loc, 0), (label_width, 55)), 0)
			
			#秀出player name、cash
			text_playername = font_s.render(str(player_list[i]),True,BLACK)
			textRect1 = text_playername.get_rect()
			textRect1.center = ((label_loc + (label_width/2)), (55/4))
			screen.blit(text_playername, textRect1)
			
			text_playercash = font_s.render('Cash: $'+str(player_list[i].cash),True,BLACK)
			textRect2 = text_playercash.get_rect()
			textRect2.center = ((label_loc + (label_width/2)), (25+55/4))
			screen.blit(text_playercash, textRect2)

			
			#再確定方塊位置
			label_loc += (label_width + label_space)
			
class MAP():
	def __init__(self):

		#在matrix中，0為白色，1為玩家1土地，2為玩家2土地，3為玩家3土地，4為玩家4土地
		self.matrix = [[0,0,0,0,0,0,0,0],
					   [0,8,8,8,8,8,8,0],
					   [0,8,8,8,8,8,8,0],
					   [0,8,8,8,8,8,8,0],
					   [0,8,8,8,8,8,8,0],
					   [0,8,8,8,8,8,8,0],
					   [0,8,8,8,8,8,8,0],
					   [0,0,0,0,0,0,0,0]]

	#LAND方塊
	def land_label(self):
	
		#寬、高、空隙、寬的位置、長的位置
		land_width = 90
		land_space = (display_width - land_width * 8) / (8+1)
		land_height = 45
		land_wloc = land_space
		land_hloc = 55 + land_space
		
		#透過matrix設定每格LAND的顏色
		for i in range(8): 
			for j in range(8):
				if self.matrix[i][j] == 0:
					land_color = WHITE
				elif self.matrix[i][j] == 1:
					land_color = colorlist[0]
				elif self.matrix[i][j] == 2:
					land_color = colorlist[1]
				elif self.matrix[i][j] == 3:
					land_color = colorlist[2]
				elif self.matrix[i][j] == 4:
					land_color = colorlist[3]
				else:
					land_color = BLACK
				
				#畫方塊
				pygame.draw.rect(screen, land_color, ((land_wloc, land_hloc), (land_width, land_height)), 0)
				
				
				#顯示名稱
				for x in Land_dict.values():
					land = x.showname
					loc = x.place
					if loc == (i,j):
						text_landname = font_s.render(land,True,BLACK)
						textRect = text_landname.get_rect()
						textRect.center = ((land_wloc + (land_width/2)), (land_hloc+(land_height/2)))##
						screen.blit(text_landname, textRect)

						
				
				#確定寬的位置
				land_wloc += (land_width + land_space)
			
			#確定寬的位置
			land_wloc = land_space
			
			#確定高的位置
			land_hloc += (land_height + land_space)
	
	
	#改變LAND顏色，輸入土地名稱、第幾位玩家(?
	def change_label(self,land,player):
		place = land.place
		index = colorlist.index(player.color)
		self.matrix[place[0]][place[1]] = index + 1

		
class BUTTON():
	def __init__(self):
		
		#按鈕大小、空隙
		self.button_size = 80
		self.button_space = 10

		#按鈕方塊：寬的位置、高的位置
		self.ybutton_wloc = (display_width / 2 - self.button_size - self.button_space)
		self.ybutton_hloc = (display_height / 2 - self.button_size)
		self.nbutton_wloc = (display_width / 2 + self.button_space)
		self.nbutton_hloc = (display_height / 2 - self.button_size)

		#YES文字位置
		self.y_wloc = self.ybutton_wloc 
		self.y_hloc = self.ybutton_hloc
		
		#NO文字位置
		self.n_wloc = self.nbutton_wloc
		self.n_hloc = self.nbutton_hloc
		

	#顯示按鈕及按鈕上的文字
	def button_show(self, choose1 = '是', choose2 = '否'):
		pygame.draw.rect(screen,WHITE, ((self.ybutton_wloc, self.ybutton_hloc), (self.button_size, self.button_size)), 0)
		pygame.draw.rect(screen,WHITE, ((self.nbutton_wloc, self.nbutton_hloc), (self.button_size, self.button_size)), 0)

		#YES文字
		text_yes = font_b.render(choose1,True,BLACK)
		y_rec = text_yes.get_rect()
		y_rec.center = ((self.y_wloc+ self.button_size/2), self.y_hloc + self.button_size/2)
		screen.blit(text_yes, y_rec)

		
		#NO文字
		text_no = font_b.render(choose2,True,BLACK)
		n_rec = text_no.get_rect()
		n_rec.center = ((self.n_wloc+ self.button_size/2), self.n_hloc + self.button_size/2)
		screen.blit(text_no, n_rec)
		pygame.display.update()
		
				
	#按到按紐
	def click_question_button(self,ans):	
		if ans == 'Y':
			return True
		elif ans == 'N':
			return False


#按鈕的回答		
def answer():
	pygame.event.clear()
	while True:
		event = pygame.event.wait()
		if event.type == QUIT:
			exit()
		elif event.type == MOUSEBUTTONDOWN:

			mouse_pos = event.pos
			if B1.ybutton_wloc <= mouse_pos[0] <= (B1.ybutton_wloc + B1.button_size) and B1.ybutton_hloc <= mouse_pos[1] <= (B1.ybutton_hloc + B1.button_size):
				ans = B1.click_question_button('Y')
				return ans
			elif B1.nbutton_wloc <= mouse_pos[0] <= (B1.nbutton_wloc + B1.button_size) and B1.nbutton_hloc <= mouse_pos[1] <= (B1.nbutton_hloc + B1.button_size):
				ans = B1.click_question_button('N')
				return ans

#----------------------------主程式運行----------------------------
def GameRun():
	print('112 Monoploy')
	setting = 0
	
	#載入Land(position,name,price,type)
	l0 = Land( 0 , "大門" , 0 , False, '學校大門',(0,0))
	l1 = Land( 1 , "共同教學館" , 45000 , True, '共同館',(0,1))
	l2 = Land( 2 , "校史館" , 0 , False, '校史館',(0,2))
	l3 = Land( 3 , "普通教學館" , 25000 , True, '普通館',(0,3))
	l4 = Land( 4 , "博雅教學館" , 35000 , True, '博雅館', (0,4))
	l5 = Land( 5 , "管理學院" , 20000 , True, '管理學院', (0,5))
	l6 = Land( 6 , "文學院" , 40000 , True, '文學院',(0,6))
	l7 = Land( 7 , "醉月湖" , 0 , False, '醉月湖',(0,7))

	l8 = Land( 8 , "社會科學院" , 40000 , True, '社科院',(1,7))
	l9 = Land( 9 , "醫學院" , 40000 , True, '醫學院',(2,7))
	l10 = Land( 10 , "公共衛生學院" , 40000 , True, '公衛學院',(3,7))
	l11 = Land( 11 , "小福" , 30000 , True, '小福',(4,7))
	l12 = Land( 12 , "生農學院" , 40000 , True, '生農學院',(5,7))
	l13 = Land( 13 , "新生教學館" , 20000 , True, '新生館',(6,7))
	l14 = Land( 14 , "小木屋鬆餅" , 0 , False, '小木屋',(7,7))

	l15 = Land( 15 , "法律學院" , 40000 , True, '法律學院',(7,6))
	l16 = Land( 16 , "電機資訊學院" , 40000 , True, '電資學院',(7,5))
	l17 = Land( 17 , "活大" , 15000 , True, '活大',(7,4))
	l18 = Land( 18 , "生命科學院" , 40000 , True, '生科院',(7,3))
	l19 = Land( 19 , "理學院" , 40000 , True, '理學院',(7,2))
	l20 = Land( 20 , "工學院" , 40000 , True, '工學院',(7,1))

	l21 = Land( 21 , "志雄" , 0 , False, '志雄',(7,0))
	l22 = Land( 22 , "計算機中心" , 45000 , True, '計中',(6,0))
	l23 = Land( 23 , "台大農場" , 40000 , True, '台大農場',(5,0))
	l24 = Land( 24 , "大福" , 20000 , True, '大福',(4,0))
	l25 = Land( 25 , "體育館" , 50000 , True, '體育館',(3,0))
	l26 = Land( 26 , "總圖" , 80000 , True, '總圖',(2,0))
	l27 = Land( 27 , "傅鐘" , 0 , False, '傅鐘',(1,0))
		
	l1.event_text(['來去上二外！','下課去吃鬆餅吧'])
	l3.event_text(['普通的教學館','腳踏車要停哪裡啊'])
	l4.event_text(['通識課上好上滿！','要去教室睡覺囉'])
	l5.event_text(['你看～管院的小朋友在吃管草的草耶～','eliteeliteeliteeliteeliteelite'])
	l6.event_text(['這裡是文學院','你有文學院的朋友嗎？我有喔:)'])

	l8.event_text(['社科院？好遠喔','社科院？有演講？'])
	l9.event_text(['醫學院？在哪裡啊','這裡是醫學院','這裡不是醬料釀造場嗎？'])
	l10.event_text(['這裡是公共衛生學院','公共衛生很重要'])
	l11.event_text(['我們來量量看八方雲集的鍋貼是不是比較短吧！','所以我說那個漢堡王呢？'])

	l12.event_text(['這裡是生農學院','前往普通的捷徑'])
	l13.event_text(['一起愉快的修早八微積分吧','一起愉快的停修早八微積分吧','今天是哪個社團的說明會呢'])
	l15.event_text(['遙遠的法律學院','高大的法律學院'])
	l16.event_text(['到底有幾座系館呢？','高材生的聚集地'])
	l17.event_text(['這裡麥當勞的薯條484比較少','活～大～好～好～吃～^_^'])
	l18.event_text(['這裡是生命科學院','一起探索生命的奧秘吧'])
	l19.event_text(['理工潮潮們的聚集地','這裡是理學院'])
	l20.event_text(['想聯絡工學院，請撥打 33663273','這裡是工學院'])

	l22.event_text(['[print(資料) if your.money > 0 else: print(\'Get Out\')]','[print(講義) if yourclassmate.money > 0 else: print(FriendShipBreak)]'])
	l23.event_text(['來去看牛牛','來去種菜菜'])
	l24.event_text(['是可以吃的大福嗎？','疑？大福在哪裡啊？','難道這裡就是神祕的大福傳送點嗎'])
	l25.event_text(['不去健身的人不是潮潮','我不是來運動，是來聽演唱會的啦','我不是來運動，是來參加CWT的啦'])
	l26.event_text(['睡覺！補眠！','一起去4樓多媒體看電影囉!'])

	
	#玩家資訊
	'''
	while setting == 0:
		try:
			player_num = int(input('輸入玩家人數：'))
		except:
			print('不要亂輸入ㄛ')
		else:
			if player_num < 0 or player_num > 4:
				print('玩家人數輸入錯誤')
			else:
				setting += 1
				while setting == 1:
					try :
						play_round = int(input('輸入回合數：'))
					except:
						print('不要亂輸入ㄛ')
					else:
						if play_round <= 0:
							print('回合數輸入錯誤')
						else:
							setting += 1'''
	# player_num = 4
	# play_round = 5
	
	global player_list
	player_list = []
	colorlist = [RED, GREEN, BLUE, YELLOW]	
	for i in range(player_num):
		player = Player('Player'+str(i+1),color = colorlist[0])
		colorlist.remove(colorlist[0])
		player_list.append(player)
	
	'''
	global player_list
	player_list = []
	colorlist = [RED, GREEN, BLUE, YELLOW]	
	for i in range(player_num):
		x = input('輸入玩家姓名：')
		player = Player(x,color = colorlist[0])
		colorlist.remove(colorlist[0])
		player_list.append(player)
	'''
	
	if len(player_list) < 4:
		for i in range(4 - len(player_list)):
			a = Player('computer'+str(i+1),colorlist[0], type = False)
			colorlist.remove(colorlist[0])
			player_list.append(a)

	
	
	#遊戲進行
	sec = 1
	running = 0
	

	global B1
	B1 = BUTTON()
	
	main()
	b_word('快點開始遊戲吧', '好', '好')
	ans = answer()
	
	play_round=1
	while running != play_round:
			main()
		
			word('第 %d 回合'%(running+1))
		

		
			for each in player_list:
								
				word('現在是 %s 的回合'%(each.name))
				
				
				#玩家骰骰子
				if each.can_move == True:
				
					#computer
					if each.type == False:
						b_word('現在在 %s ，您是否要骰骰子'%(Land_dict[each.position].name))
						sleep(sec)
						word(str(each.move()))
						
					#player
					else:

						b_word('現在在 %s ，您是否要骰骰子'%(Land_dict[each.position].name))
						ct = 0						
						while True:
							ans = answer()
							if ans != True:
								ct += 1
								if ct <= 2:
									b_word('現在在 %s ，您是否要骰骰子'%(Land_dict[each.position].name))
								elif ct <= 9:
									b_word('再不骰骰子會被當掉喔，您是否要骰骰子')
								elif ct <= 19:
									b_word('我拿骰子丟你喔^^，您是否要骰骰子')
								else:
									each.pay_cash(1000)
									b_word('你惹電腦不開心，起始現金扣除1000，你是否要骰骰子')
							else:
								buttonon = False
								word(each.move())
								break
								
					theLand = Land_dict[each.position]
					
					#玩家執行動作
					if theLand.type == True:
						
						word('「'+theLand.event_text_call()+'」')
						
						if each.position == 5 and theLand.was_bought == False and each.cash >= theLand.price:
							#computer
							if each.type == False:								
								b_word("是非題：「and、or、not是邏輯運算元，不是邏輯運算子」")
								sleep(sec)
								ans = random.choice([True,False])
							#player
							elif each.type == True:
								b_word("是非題：「and、or、not是邏輯運算元，不是邏輯運算子」")
								ans = answer()

							if ans == False:
								each.purchase_land(theLand)
								word('恭喜你花 %d 元買到了管理學院'%(theLand.price))
							else:
								each.pay_cash(10000)
								word('同學該停修商管程設囉！扣除現金 10000 元')
						
						elif theLand.was_bought == False and each.cash >= theLand.price:
							#computer
							if each.type == False:
								b_word('%s 價值 %d 元，你是否要購買呢？'%(theLand.name,theLand.price))
								sleep(sec)
								ans = True
							#player
							elif each.type == True:
								b_word('%s 價值 %d 元，你是否要購買呢？'%(theLand.name,theLand.price))
								ans = answer()

							if ans == True:
								word(each.purchase_land(theLand))
							else:
								word('這些買地的機會不屬於你>_<')
						
						elif theLand.was_bought == False and each.cash < theLand.price:
							word('你這學期的學費繳了嗎？還差 %d 元哦'%(theLand.price-each.cash))
						
						elif theLand.was_bought == True and theLand.owner == each and each.cash >= theLand.house_cost:
							#computer
							if each.type == False:
								b_word('你是否要花費 %d 元蓋違章建築'%theLand.house_cost)
								sleep(sec)
								ans = True
							#player
							elif each.type == True:
								b_word('你是否要花費 %d 元蓋違章建築'%theLand.house_cost)
								ans = answer()

							if ans == True:
								word(each.purchase_house(theLand))
							else:
								word('您真是個守法的正義公民')
								
						elif theLand.was_bought == True and theLand.owner == each and each.cash < theLand.house_cost:
							word('再差 %d 元你就可以蓋違章建築囉:)'%(theLand.house_cost-each.cash))
			
						#活大
						elif theLand.was_bought == True and theLand.owner != each and each.position == 17:
							chance = random.randint(1,2)
							if chance == 1:
								each.pay_cash(theLand.payment)
								theLand.owner.receive_cash(theLand.payment)
								word('你需要付 %d 元學餐費給 %s '%(theLand.payment,theLand.owner.name))
							else:
								each.receive_cash(theLand.payment)
								theLand.owner.pay_cash(theLand.payment)
								word('你不幸吃到活大老鼠，得到 %s 的補償 %d 元'%(theLand.owner.name,theLand.payment))
						
						#小福 & 大福
						elif theLand.was_bought == True and theLand.owner != each and each.position in [24,11]:
							if Land_dict[11].owner == Land_dict[24].owner:
								each.pay_cash((theLand.payment)*1.5)
								theLand.owner.receive_cash((theLand.payment)*1.5)
								word('%s 大小福通吃，你必須付給他1.5倍的學餐費，共 %d 元'%(theLand.owner,(theLand.payment)*1.5))
							else:
								each.pay_cash(theLand.payment)
								theLand.owner.receive_cash(theLand.payment)
								word('你需要付 %d 元學餐費給 %s '%(theLand.payment,theLand.owner.name))
								
						#一般
						elif theLand.was_bought == True and theLand.owner != each:
							each.pay_cash(theLand.payment)
							theLand.owner.receive_cash(theLand.payment)
							word('你需要付 %d 元學分費給 %s '%(theLand.payment,theLand.owner.name))
					
					else:
						#大門
						if each.position == 0:
							each.receive_cash(10000)
							word('恭喜你回到我112大門口，學費 10000 元拿去花')
						
						#校史館
						elif each.position == 2:
							each.receive_cash(10000)
							word('發現傅斯年校長留下的財產！得到獎金 10000 元')
						
						#醉月湖
						elif each.position == 7:
							word('女鬼問你：「請問現在幾點了？」')
							now = datetime.datetime.now()
							delta = datetime.timedelta(hours = 12)
							n_days = now + delta
							option1 =  now.strftime('%H:%M:%S')
							option2 =  n_days.strftime('%H:%M:%S')
							b_word("option1: %s or option2: %s "%(option1, option2), '1', '2')
							#player
							if each.type == True:
								ans = answer()
							#computer
							elif each.type == False:
								ans = random.choice([True, False])
								sleep(sec)
							if ans == True:
								each.receive_cash(10000)
								word('「難道……你就是我的真命天子嗎？」獲得女鬼的愛，現金增加 10000 元')
							else:
								each.pay_cash(10000)
								word('「你怎麼可以騙我！」女鬼討厭你，要花 10000 元收驚')
						
						#小木屋鬆餅
						elif each.position == 14:
							each.can_move = False
							word('購買鬆餅的人潮太多了！被迫暫停一回')
						
						#志雄
						elif each.position == 21:
							each.pay_cash(5000)
							word('腳踏車壞掉囉！修理費共 5000 元')
						
						#傅鐘
						elif each.position == 27:
							each.cash /= 2
							each.one_half += 1
							word('聽到21次鐘聲！學期成績被21，現金剩一半')
				else:
				
					if each.type == True:
						b_word('您是否要骰骰子')
						ans = answer()
					else:
						b_word('您是否要骰骰子')
						sleep(sec)
						ans = True
					word(each.move())
					
						
			running += 1
	
	#贏家判斷
	# print('\n總資產合計：')
	winner_p = 0
	global winner
	winner = []
	for i in player_list:
		if int(i.Property()) > winner_p:
			winner = [i.name]
			winner_p = i.Property()
		elif int(i.Property()) == winner_p:
			winner.append(i.name)
		
	#拖吊王
	# print('腳踏車被拖吊總數：')
	winner_t = 1
	global winnert
	winnert = []
	for i in player_list:
		if i.beTowed > winner_t:
			winnert = [i.name]
			winner_t = i.beTowed
		elif i.beTowed == winner_t:
			winnert.append(i.name)


	#黑卷獎
	# print('被二一次數：')
	winner_21 = 1
	global winner21
	winner21 = []
	for i in player_list:
		if i.one_half > winner_21:
			winner21 = [i.name]
			winner_21 = i.one_half
		elif i.one_half == winner_21:
			winner21.append(i.name)


"""	
	#輸出
	print()

	print('書卷獎得主：', end = '')
	[print(i,end=' ') for i in winner]
	
	print()
	
	if winnert != []:
		print('水源阿伯常客：',end = '')
		[print(i,end = ' ') for i in winnert]

	print()
	
	if winner21 != []:
		print('黑卷獎（被21最多次）得主:',end = '')
		[print(i,end = ' ') for i in winner21]
"""


#主畫面模樣						
def main():
	player_label(4)
	map.land_label()
	pygame.display.update()


if __name__ == "__main__":
	
	run = True
	while run:
		
		screen = pygame.display.set_mode((display_width, display_height))
		pygame.display.set_caption(title)

		event = pygame.event.wait()

		if s == 0:
			Game_Menu()

		elif s == 1:
			NumPlayer()
			
		elif s == 3:
			break

		elif s == 4:
			NumRound()

		else:
			Rules()


	screen.fill((0,0,0))
	map = MAP()
	GameRun()

	over = True
	while over:
		Game_over()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
