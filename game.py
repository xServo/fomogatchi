import os	
import random
import math
from actions import *

class Fomo:
	def __init__(self, name, lk):
		self.name = name	
		
		# stats
		self.lk = lk
		self.hp = 100
		self.cash = 0
		self.happiness = 30 
		self.job = "Unemployed"
	
	def lk_roll(bonus):
		lk = random.randrange(0, self.lk)
		roll = lk + bonus
		print("You rolled a:", lk, "\nWith a bonus of:", bonus, "\n Your total check is:", roll)
def stat_out(fomo):
	print("hp:", fomo.hp)
	print("cash:", fomo.cash)
	print("happiness:", fomo.happiness)
	print("job:", fomo.job)

def game_over(fomo):
	sys.exit()

def suicide_check(fomo):
	if fomo.happiness < 1:
		print(fomo.name, "has commited suicide due to reaching a hapiness level of 0.")
		game_over()

def get_date(days):
	day = days % 31
	# months start on the first
	if day == 0:
		days = days + 1
		day = days % 31

	months = math.floor(days / 31)
	if months == 0:
		month = "Winter"
	elif months == 1:
		month = "Spring"
	elif months == 2:
		month = "Summer"
	elif months == 3:
		month = "Fall"
	return month, day

# prep fomo loop
name = input("What is your Fomo's name?\n") # get name
starting_luck = 30 # get luck ? more stats ?
fomo = Fomo(name, starting_luck) # init fomo class
days = 1 # get days in

# day loop
while 1:
	# day begin
	os.system("clear")

	print("A new day for:", fomo.name)
	suicide_check(fomo)	
	stat_out(fomo)
	print(get_date(days))
	input()
	
	# action phase
	action = input("What will you do today?\n")

	# jobs
	if action == "job":
		job_market = Job_Market(fomo)
		# print(job_market.job_list)
		job_market.find_job(fomo)
		
	action = ""
	# day end
	days = days + 1 
