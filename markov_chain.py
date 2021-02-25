
import numpy as np
from numpy.core.defchararray import index

class MarkovChain(object):
    def __init__(self, transition_matrix, states):
        self.transition_matrix = transition_matrix
        self.states = states
        self.index_dict = {}
        for i in range(len(states)):
            self.index_dict[states[i]] = i
        self.state_dict = {}
        for i in range(len(states)):
            self.state_dict[i] = states[i]

    def next_state(self, current_state):
        '''Generates the next state given the current state'''
        current_state_index = self.index_dict[current_state]
        probability_matrix = self.transition_matrix[current_state_index]
        return np.random.choice(self.states, p=probability_matrix)

    def generate_states(self, current_state, num):
        '''Generates the next num states given a current state'''
        future_states = []
        for i in range(num):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states





if __name__ == "__main__":
    print('hello')
    chain = MarkovChain([[0.8,0.2],[0.6,0.4]],['A','B'])
    print(chain.generate_states('A',10))