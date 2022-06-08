# first premise
class Premise_Studio:
	def __init__(self, fomo):
		self.job = "Barista"
		self.residence = "Studio Apartment"
		self.cash = 500
		self.lk = 20

# premise selector
def premise_selector(premise, fomo): 
	fomo.job = premise.job
	fomo.residence = premise.residence
	fomo.cash = premise.cash
	fomo.lk = premise.lk
