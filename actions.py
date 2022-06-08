import random


class Job_Market:
	def __init__(self, fomo):
		# dict of potential jobs keyyed with earnings/10
		# TODO create a collection of jobs that include qualifications
		self.job_list = {"Carpet Cleaner": 4, "Dog Walker": 2, "Cashier": 3, "Event Planner": 5, "Garbage Person": 4, "Dictator": 10, "Barista": 3}
	
	def find_job(self, fomo):
		# get random job
		job, pay = random.choice(list(self.job_list.items()))
		print(job, pay)
		will_accept = input("Will you accept? 0 or 1\n")
		if will_accept == "1":
			fomo.job = job

# jobs
class Barista:
	def __init__(self, fomo, wage, rep, skill):
		# stats about job
		self.wage = wage # 12
		self.rep = rep # 20 # x/100
		self.skill = skill # 0
	
	#def encounter(self, fomo):
		# encounter and skill check
	def message(self):
		day_report = ["It was a normal day. ", "I was a great day. ", "It was a bad day. "]
		messages = {
		"messed up an order and a customer through their coffee in your face. You handled their reaction well." : (-4, 4),
		"made latte art of a tree." : (2, 2),
		"cleaned up vomit. The coworkers were releived." : (7, 1)
		}
		


"""
TODO actions:
casino
lottery
gym
therapy
read
run
study

big expacs:
crime
long term education
"""
