


class Point:
	def __init__(self, x, y, z, pitch, roll, point_type="Absolute"):
		self.x: float = x
		self.y: float = y
		self.z: float = z
		self.pitch: float = pitch
		self.roll: float = roll
		self.point_type: str = point_type
		
	def __repr__(self):
		return f"X={self.x} Y={self.y} Z={self.z} PITCH={self.pitch} ROLL={self.roll} TYPE={self.point_type}"
		
		