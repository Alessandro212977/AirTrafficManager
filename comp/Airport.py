
class Airport:
	def __init__(self) -> None:
		self.ICAO = ''
		self.city = ''
		self.country = ''
		self.latitude = ''
		self.longitude = ''

		self.terminals = []
		self.runways = []

		self.destinations = []

	def __eq__(self, o: object) -> bool:
		pass

	def __repr__(self) -> str:
		pass

	def update(self) -> None:
		pass


class Terminal:
	def __init__(self, ICAO, ID) -> None:
		self.ICAO = ICAO
		self.id = ID

		self.gates = []
		self.capacity = 0


class Gate:
	def __init__(self, terminal_id) -> None:
		self.terminal_id = terminal_id
		self.id = ''
		self.status = 'empty'


class Runway:
	def __init__(self, ICAO, ID) -> None:
		self.ICAO = ICAO
		self.id = ID

		self.status = 'empty'