import threading
from communication.communication import Communication
"""
from sensors.distance.distance import DistanceSensor

from sensors.hydrophone.hydrophones import HydrophonesPair

"""
#from sensors.ahrs.ahrs import AHRS
from control.movements.movements import Movements
from logpy.LogPy import Logger
from sensors.depth.depth import DepthSensor
'''
Main object (thread) provides all sensors objects
and passes them to new thread Communication.
Communication thread is responsible of handling
Pyro4 server and requests to it.

Communication class has its own methods to all features it handles.
It is backed by easier use of Communication class from Xavier level.
(You don't have to know key of each sensor in sensor references dictionary)

'''

class Main():
    '''
    Creates object of all sensor types, packs their references into
    a list. Creates Communication thread.
    '''
    def __init__(self):
        '''
        Creates and stores references of all slave objects.
        '''
        self.logger = Logger(filename='main',directory='',logtype='info',timestamp='%Y-%m-%d | %H:%M:%S.%f',logformat='[{timestamp}] {logtype}:    {message}',prefix='',postfix='',title='Main Logger',logexists='append',console=False)
        #self.ahrs = AHRS(main_logger = self.logger, local_log = True)
        #self.depth = DepthSensor(main_logger = self.logger, local_log = True)
        #self.depth.run()
        self.logger.start()
        #self.ahrs.run()
        self.sensors_refs = {
            'Movements':Movements()
        }
        #Here you can add more feature classes
        #Remeber then to provide proper Communication class methods

        self.comm = Communication(self.sensors_refs,'192.168.0.190',
        main_logger = self.logger)
        '''
        Communication class parameters are: sensors_refs, rpi_address,
        main_logger, local_logger, log_directory (last three are optional)
        '''



if __name__== "__main__":
    main = Main()
    main.comm.start()
    main.comm.join()
    #Starting and waiting for infinite thread Communication to finish
