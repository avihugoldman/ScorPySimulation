from typing import List


class Point:
	def __init__(self, x, y, z, pitch, roll, point_type="Absolute", motors_position = None):
		self.x: float = x
		self.y: float = y
		self.z: float = z
		self.pitch: float = pitch
		self.roll: float = roll
		self.point_type: str = point_type
		self.motors_position: List[float] = motors_position
		print(self.motors_position)
		
	def __repr__(self):
		return f"X={self.x} Y={self.y} Z={self.z} PITCH={self.pitch} ROLL={self.roll} TYPE={self.point_type}"
		
		