import random


class Job_Market:
	def __init__(self, fomo):
		# dict of potential jobs keyyed with earnings/10
		# TODO create a collection of jobs that include qualifications
		self.job_list = {"Carpet Cleaner": 4, "Dog Walker": 2, "Cashier": 3, "Event Planner": 5, "Garbage Person": 4, "Dictator": 10}
	
	def find_job(self, fomo):
		# get random job
		job, pay = random.choice(list(self.job_list.items()))
		print(job, pay)
		will_accept = input("Will you accept? 0 or 1\n")
		if will_accept == "1":
			fomo.job = job


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
