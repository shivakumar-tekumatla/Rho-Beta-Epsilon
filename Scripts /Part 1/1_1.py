import numpy as np 
import matplotlib.pyplot as plt 
class MotorSpecs:
    def __init__(self) -> None:
        self.W0 = 4610 # No load speed in RPM 
        self.W0 = self.W0*2*np.pi/60 # in radin per second 
        self.Ts = 2.05  # Stall torque ft-lb
        self.Ts = self.Ts *1.356 # in N-m 
        self.V = 12    # Voltage V
        self.If = 2.4  # Free current A  
        self.Is = 97   # Stall Current A
        self.Ra  = 0.12 # Armature resistance Ohm 
        self.Kv = self.W0 / self. V 
        self.Kt = 1/self.Kv 
        # self.Kt =  60/(2*np.pi*self.Kv) # Motor Constant  #self.R*self.Ts/self.V# Motor Constant
        self.T = np.arange(0,self.Ts,0.001)
        pass

    def speed(self,T): #self.Kv*T #
        return  -self.W0*T/self.Ts+self.W0  # self.V/self.Kt - self.R*T/(self.Kt**2)

    def current(self,T):
        return self.Is *T /self.Ts#self.Is T/ self.Kt #

    def power(self,T):
        W = self.speed(T)
        return T*W
    def efficiency(self,T):
        PM = self.power(T)#Mechanical power 
        PE = self.V*self.current(T) 
        losses = self.If**2 *self.Ra 
        return (PM)*100/(PE+losses) 
def main():
    motor = MotorSpecs()
    W = np.array(list(map(motor.speed,motor.T)))
    I = np.array(list(map(motor.current,motor.T)))
    P = np.array(list(map(motor.power,motor.T)))
    eff = np.array(list(map(motor.efficiency,motor.T)))
    
    plt.plot(motor.T,W) 
    plt.plot(motor.T,I) 
    plt.plot(motor.T,P) 
    plt.plot(motor.T,eff) 
    plt.ylabel("Speed, Current,Power, Efficiency")
    plt.xlabel("Torque")
    plt.legend(['Speed', 'Current','Power','Efficiency'], loc='upper left')
    plt.show()

if __name__ == "__main__":
    main()

