import pigpio
import time


class EngineDriver():
	
	engines_ready = False
	frequency = 500
	startup_time = 5
	stop = 192
	
	old_min = -1
	old_max = 1
	new_max = 255
	new_min = 128
	engines_dict = {"fl" : 12, "fr" : 3, "bl" : 4, "br" : 5,"vl" : 6,"vr" : 7,"vb" : 8}
	set_dict = {"fl" : False, "fr" : False, "bl" : False, "br" : False,"vl" : False,"vr" : False,"vb" : False}
	old_dict = {"fl" : 192, "fr" : 192, "bl" : 192, "br" : 192,"vl" : 192,"vr" : 192,"vb" : 192}
	def __init__(self):
		self.pi = pigpio.pi()
		print("Ustawianie silników")
		for val in self.engines_dict.values():
			self.pi.set_PWM_dutycycle(val,self.stop)
			self.pi.set_PWM_frequency(val,self.frequency)
		time.sleep(5)
		self.engines_ready = True
		print("Silniki gotowe")
		#aby sterownik się zainicjował poprawnie, trzeba kila sekund dawać sygnał o wypełnieniu 75%
		# i okresie 2000us
	
	def __del__(self):
		for val in self.dictionary.values():
			self.pi.set_PWM_dutycycle(val,stop)
		self.pi.stop()
	
	def set_engines(self,dictionary):
		for key, val in dictionary.items():
			dictionary[key] = (((val - self.old_min) * (self.new_max - self.new_min)) / (self.old_max - self.old_min)) + self.new_min
		while True:
			for key, val in dictionary.items():
				if int(dictionary[key]) == int(self.old_dict[key]):
					self.set_dict[key] = True
				elif dictionary[str(key)] < self.old_dict[str(key)]:
					self.old_dict[key] = self.old_dict[key]-1
				elif dictionary[str(key)] > self.old_dict[str(key)]:
					self.old_dict[key] = self.old_dict[key]+1
				self.pi.set_PWM_dutycycle(self.engines_dict[key],self.old_dict[key])
				#print(self.old_dict[key], dictionary[key])
				if all(is_set is True for is_set in self.set_dict.values()):
                                    #print("all set")
                                    for key in self.set_dict.keys():
                                        self.set_dict[key] = False
                                    return




