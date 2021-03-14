import numpy as np

p_Tail = 1/2
p_Head = 1/2
prob = 1/2
n_flips = 5
flipResults = np.arange(n_flips)
flipResults_Strings = []

def SuccesiveTosses(*args):
    p_H = 1/2
    p_T = 1/2
    p_HAndT = 1/4
    p_HGivT = p_HAndT / p_T
    p_TAndH = 1/4
    p_TGivH = p_TAndH / p_T
    print(p_HGivT)
    print(p_TGivH)

def flip_coin():
    flip = np.random.binomial(1, 1/2, 1)
    if flip[0] == 1:
        side = "H"
    else:
        side = "T"
    return side

def flip_condition(stop_condition=['H', 'T'], print_opt=False):
    flip_list = []
    
    current_index = 0
    current_condition = None
    while current_condition != stop_condition:
        flip_list.append(flip_coin())
        if len(flip_list) >= len(stop_condition):
            current_condition = [flip_list[i] for i in range(current_index - len(stop_condition) +1 , current_index + 1)]
        else:
            pass
        current_index +=1
        
    if print_opt:
        print(flip_list)
    return current_index 

#a = np.mean([flip_condition(['H', 'H','H', 'H','H']) for i in range(10000)])
#b = np.mean([flip_condition(['T','T','H', 'H','H', 'H','H']) for i in range(10000)])
#c = np.mean([flip_condition(['T','T','H', 'H','H', 'H','H','T','T']) for i in range(10000)])

#print("Average # of flips to achieve HHHHH: {}".format(a))
#print("Average # of flips to achieve TTHHHHH: {}".format(b))
#print("Average # of flips to achieve TTHHHHHTT: {}".format(c))