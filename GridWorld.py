import numpy as np
import random

AU = 0
AR = 1
AD = 2
AL = 3

class GridWorld:
    """
    Class containing the GridWorld 687 Environment
    
    """
    
    def __init__(self, gamma = 0.9, delta = 0.0001) -> None:
        
        # Grid Size
        self.nrows = 5
        self.ncols = 5
        
        # Discount rate = 0.9 by default   
        self.gamma = gamma
        
        # Defining all states as 'NORMAL' type first
        self.states_type = [["N" for i in range(self.ncols)] for j in range(self.nrows)]
        
        # Initializing Value State Function to 0
        self.states_value = [[0. for i in range(self.ncols)] for j in range(self.nrows)]
        
        # Initializing Rewards 
        self.rewards = [[0. for i in range(self.ncols)] for j in range(self.nrows)]
        
        # Goal State
        self.states_type[4][4] = "G"        # Set type to GOAL
        self.rewards[4][4] = 10.             # Goal State with 10 reward
        
        # Obstacle States
        self.states_type[2][2] = "O"        # Set type to OBSTACLE
        self.states_type[3][2] = "O"        # Set type to OBSTACLE
        
        # Water State 
        self.states_type[4][2] = "W"        # Set type to WATER
        self.rewards[4][2] = -10.            # WATER State with -10 reward
    
           
    def DisplayStateValues(self):
        for row in self.states_value:
            for i in row:
                print("{0:0.4f}".format(i), end = "  ")
            print()
            # print(["{0:0.4f}".format(i) for i in row])
            # print(row) 
    
    
    def DisplayPolicy(self, policy):
        for irow, row in enumerate(policy):
            for icol, action in enumerate(row):       
                charac = action
                if action == AU:
                    charac = u"\u2191"
                elif action == AR:
                    charac = u"\u2192"
                elif action == AD:
                    charac = u"\u2193"
                elif action == AL:
                    charac = u"\u2190"
                
                if self.states_type[irow][icol] == "G":
                    charac = "G"
                if self.states_type[irow][icol] == "O":
                    charac = "O"                        
                print(charac, end = "  ")
            print()
                
    def DisplayStateRewards(self):
        for row in self.rewards:
            print(row)


    def DisplayStateTypes(self):
        for row in self.states_type:
            print(row)
    

    def isEnterableState(self, row, col):
        # Wall
        if(row < 0 or row >= self.nrows or col<0 or col>=self.ncols):
            return False
        
        # Obstacle
        if(self.states_type[row][col] == 'O'):
            return False
        
        return True
        
    
    def getNextStatesAndProbabilities(self, action, row, col ):
        next_states = []
        probabilities = []
        
        # Attempt Up
        if(action == AU):
            # print("AU")
            
            # Up 80%            
            # Valid next state
            if(self.isEnterableState(row-1, col)):
                next_states.append((row-1,col))
                probabilities.append(0.8)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.8)
                   
            # Right of AU 5%:
            if(self.isEnterableState(row, col+1)):
                next_states.append((row,col+1))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)
                    
            # Left of AU 5%:
            if(self.isEnterableState(row, col-1)):
                next_states.append((row,col-1))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)  
                
            # Broken and same state 10%
            next_states.append((row,col))
            probabilities.append(0.1)
 
            
        elif(action == AR):
            # print("AR")
            
            # Right 80%            
            # Valid next state
            if(self.isEnterableState(row, col+1)):
                next_states.append((row,col+1))
                probabilities.append(0.8)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.8)
                
            # Right of AR is down 5%:
            if(self.isEnterableState(row+1, col)):
                next_states.append((row+1,col))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)
               
            # Left of AR is up 5%:
            if(self.isEnterableState(row-1, col)):
                next_states.append((row-1,col))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)  
                
            # Broken and same state 10%
            next_states.append((row,col))
            probabilities.append(0.1)
            
            
        elif(action == AD):
            # print("AD")
            # Down 80%            
            # Valid next state
            if(self.isEnterableState(row+1, col)):
                next_states.append((row+1,col))
                probabilities.append(0.8)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.8)
                
            # Right of AD is left 5%:
            if(self.isEnterableState(row, col-1)):
                next_states.append((row,col-1))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)
              
            # Left of AD is right 5%:
            if(self.isEnterableState(row, col+1)):
                next_states.append((row,col+1))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)  
            
            # Broken and same state 10%
            next_states.append((row,col))
            probabilities.append(0.1)
            
            
        elif(action == AL):
            # print("AL")
            # Left 80%            
            # Valid next state
            if(self.isEnterableState(row, col-1)):
                next_states.append((row,col-1))
                probabilities.append(0.8)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.8)
                
            # Right of AL is up 5%:
            if(self.isEnterableState(row-1, col)):
                next_states.append((row-1,col))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)
               
            # Left of AL is down 5%:
            if(self.isEnterableState(row+1, col)):
                next_states.append((row+1,col))
                probabilities.append(0.05)    
            else:   # Bounced back into same state
                next_states.append((row,col))
                probabilities.append(0.05)  
                
            # Broken and same state 10%
            next_states.append((row,col))
            probabilities.append(0.1)
        
        return next_states, probabilities
    
            
    def getValueForAction(self, action, row, col):
        """
        Return expected Value when an action a is taken at state (row,col)
        """
        if(self.states_type[row][col] == 'G' or self.states_type[row][col] == 'O'):
            # print("Obstacle/Goal state. No need to calculate ValueforActions as unreachable state. Returning 0")
            return 0.
        
        if(not self.isEnterableState(row, col)):
            print("Called notEnterable function. Need to DEBUG. returning 0 value")
            return 0.        
         
        neighbours, probabilities = self.getNextStatesAndProbabilities(action, row, col)
        value_sum = 0.
        
        for (s_dash_row, s_dash_col), p in zip(neighbours,probabilities):
            # print(s_dash_row, s_dash_col, p, self.rewards[s_dash_row][s_dash_col], self.states_value[s_dash_row][s_dash_col]) 
            value_sum += p * (self.rewards[s_dash_row][s_dash_col] + (self.gamma * self.states_value[s_dash_row][s_dash_col]))
            
        return value_sum
        
    def inf_norm(self, v1, v2):
        diff_v = (np.array(v1) - np.array(v2)).flatten()
        diff = np.linalg.norm(diff_v, np.inf)
        return diff
        
    
    def ValueIteration(self, delta = 0.0001):
        # V_{t+1}
        v = [[0. for i in range(self.ncols)] for j in range(self.nrows)]
        policy = [[AU for i in range(self.ncols)] for j in range(self.nrows)]
        diff = 0
        
        niter = 0
        while(True):
            niter+=1
            print(f"N iter = {niter}")
            for row in range(self.nrows):
                for col in range(self.ncols):
                    actions = [AU, AR, AD, AL]
                    action_values_dict = {}
                    for action in actions:
                        action_values_dict[action] = self.getValueForAction(action=action, row=row, col=col)
                    
                    (best_action, best_value) = max(action_values_dict.items(), key=lambda x: x[1])
                    # print(f"Best action is ; {best_action}")
                    # Value Update
                    v[row][col] = best_value
                    
                    # Policy Improvement
                    policy[row][col] = best_action

            # print("Self States Values = ")
            # for row in self.states_value:
            #     print(row)
                
            # print("v = ")
            # for row in v:
            #     print(row)
                
            diff = self.inf_norm(self.states_value, v)
            # Copying Manually
            for row in range(self.nrows):
                for col in range(self.ncols):
                    self.states_value[row][col] = v[row][col]
            
            
            # diff = max()
            print(f"Diff is: {diff}")
            
            if(diff<delta):
                break
            self.DisplayStateValues()
            self.DisplayPolicy(policy=policy)
            print()
        
        self.DisplayStateValues()
        self.DisplayPolicy(policy=policy)
        return v, policy
           
        
def main():

    # # Q1
    # gw = GridWorld(gamma=0.9)
    # v, policy = gw.ValueIteration()
    
    # # Q2
    # gw = GridWorld(gamma=.25)
    # v, policy = gw.ValueIteration()
    
    # # Q3
    # gw = GridWorld(gamma=0.9)
    # gw.rewards[0][2] = 5.           # Added gold at (0,2)
    # v, policy = gw.ValueIteration()
    
    # # Q4a
    # gw = GridWorld(gamma=0.9)
    # gw.rewards[0][2] = 5.           # Added gold at (0,2)
    # gw.states_type[0][2] = "G"    
    # v, policy = gw.ValueIteration()
    
    # # Q4b
    # # gw = GridWorld(gamma=0.9)
    # # gw = GridWorld(gamma=0.9133)
    # # gw = GridWorld(gamma=0.935)
    # gw = GridWorld(gamma=0.95)
    # gw.rewards[0][2] = 5.           # Added gold at (0,2)
    # gw.states_type[0][2] = "G"
    # v, policy = gw.ValueIteration()
    
    # Q5
    gw = GridWorld(gamma=0.9)
    gw.rewards[0][2] = 4.483           # Added gold at (0,2)
    gw.states_type[0][2] = "G"    
    v, policy = gw.ValueIteration()
    
    
    
if __name__ == "__main__":
    main()
        
        
    
    
    