import copy
import random
# Consider using the modules imported above.
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        keyvalues = [([k] * v) for k, v in kwargs.items()]

        self.contents = [i for sublist in keyvalues for i in sublist ]
      #print(self.contents)
    def draw(self, quantity_to_draw):
        if quantity_to_draw > len(self.contents):
            return self.contents
        
        '''random.shuffle(self.contents)
        result = []
        for i in range(quantity_to_draw):
            result.append(self.contents.pop())
        #print(result)
        return result''' #SOMEHOW, THIS DOESNT MATCH THE TESTES (SPECIFICATION FAILURE?)

        drawn = random.sample(self.contents, k=quantity_to_draw)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn
          
        
      


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #keyvalues = [([k] * v) for k, v in expected_balls.items()]
  
    #arr_expected_balls = [i for sublist in keyvalues for i in sublist ]
    #arr_expected_balls.sort()
    #print(arr_expected_balls)
    #print("Esperados")
    print( expected_balls)
  
    matching_result_count = 0
    for _ in range(num_experiments):

        current_hat_copy = copy.deepcopy(hat)
        current_experiment_result = current_hat_copy.draw(num_balls_drawn)
      
        current_experiment_result.sort()
        #print(current_experiment_result)

        dict_current_experiment_result = Counter(current_experiment_result)

        #print(dict_current_experiment_result)
      
        #if(dict_current_experiment_result == expected_balls):
            #matching_result_count += 1

        to_add = True
        for k, v in expected_balls.items():
            if v > dict_current_experiment_result.get(k, -99):
                to_add = False
                #print(dict_current_experiment_result)
        '''for k, v in dict_current_experiment_result.items():
            if k in expected_balls and v < expected_balls.get(k, -99):
                to_add = False'''
                #print("N")
                #print(dict_current_experiment_result)
              
        if(to_add):
            #print(dict_current_experiment_result)
            matching_result_count += 1
    #print(matching_result_count)
    return (matching_result_count) / num_experiments
