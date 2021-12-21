
class Route:
	def __init__(self, ap1, ap2) -> None:
		self.ICAO_1 = ap1
		self.ICAO_2 = ap2
		self.distance = 0
		self.duration = 0

	def __repr__(self) -> str:
		return self.ICAO_1 + ' - ' + self.ICAO_2