
class ForexDataModel:
	def __init__(self, strDescriptor):
		sections = strDescriptor.split(',')
		self.Symbol = sections[0]
		self.Name = sections[1]
		self.Ask = sections[2]
		self.Bid = sections[3]
		self.Open = sections[4]
		self.PreviousClose = sections[5]
		self.LastTradeWithTime = sections[6]
