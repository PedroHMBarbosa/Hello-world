import numpy as np
from math import sqrt 

# classe contendo todos os subcomportamentos
class Behavior():
    def moving_to_goal(self): 
    #{
        # coordenadas do Goal
        X_t = 8
        Y_t = 7
        
        # coordenadas do robô
        X_i = 3
        Y_i = 1
        
        # distância entre o robô e o Goal
        dm = sqrt(pow((X_t - X_i),2) + pow((Y_t - Y_i),2))

        V_move_to_goal = (1/dm) * np.array([[X_t - X_i],[Y_t - Y_i]])
        
        # a variável de controle f1 precisa da distância "dm"
        f1 = ControlParameters.f1(self,dm) 
        
        print('dm = {}'.format(dm))
        print('f1 = {}'.format(f1))
        print('vetor = {}'.format(V_move_to_goal)) 
        return f1,V_move_to_goal
    #}
    '''
    def avoiding_obstacles(self): 
    #{
        # coordenadas do robô
        X_i = 
        Y_i = 
       
        # coordenadas do obstáculo mais próximo
        X_0 = 
        Y_0 = 
        
        # distância entre o robô e o obstáculo
        d0 = sqrt(pow((X_0 - X_i),2) + pow((Y_0 - Y_i),2))
        
        if (obstáculo à esquerda):
            V_avoid_obstacle = (1/d0) * np.array([[(Y_0 - Y_i)],[(X_0 - X_i)]])
        else: 
            V_avoid_obstacle = (1/d0) * np.array([[-1*(Y_0 - Y_i)],[-1*(X_0 - X_i)]])

        # a variável de controle f2 precisa da distância "d0"
        f2 = ControlParameters.f2(self,d0)

        print('f2 = {}'.format(f2))
        return V_avoid_obstacle
    #}
    '''
    def wall_following(self): 
    #{
        V_follow_wall = np.array([])
    #}
    
    def avoiding_robot(self): 
    #{
        V_avoid_robot = np.array([])
    #}

    def keep_formation(self):
    #{
        V_keep_formation = np.array([])
    #}

# {f1,f2,f3,f4,f5}
class ControlParameters():
    
    def f1(self,dm):
    #{
        # recebe "dm" de moving_to_goal()
        dm = dm
        
        # parâmetros ajustáveis (como ajustá-los?)
        am = 1
        bm = 5
        
        # dm pertence à (bm,+oo)
        if dm > bm:
            f1 = am
        # dm pertence à [0,bm]
        else:
            f1 = am*(dm/bm)
        
        return f1
    #}
    
    def f2(self,d0):
    #{
        # recebe "d0" de avoiding_obstacles()
        d0 = d0
        
        # parâmetros ajustáveis (como ajustá-los?)
        a0 = 1
        b0 = 5
        bf = 2

        # se d0 pertence ao intervalo [bf,b0]
        if d0 >= bf and d0 <= b0:
            f2 = a0*((d0/(bf-b0)) + (b0/(b0-bf)))
        # d0 pertence não ao intervalo [bf,b0]
        else:
            f2 = 0

        return f2
    #}
    
    def f3(self):
        #{
            d
        #}
    
    def f4(self):
        #{
            d
        #}
    
    def f5(self):
        #{
            d
        #}

x = Behavior()

f1,vetor = x.moving_to_goal() 



