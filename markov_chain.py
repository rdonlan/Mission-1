
import numpy as np
from numpy.core.defchararray import index
from drawing_functions import *

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
    states =                ['H2', 'H3', 'H4', 'P1', 'P2', 'P3', 'F1', 'F2', 'F3']
    transition_matrix = [   [0.05, 0.1 , 0.15, 0.2 , 0.1 , 0.05, 0.15, 0.15, 0.05],
                            [0.05, 0.1 , 0.2 , 0.05, 0.2 , 0.15, 0.05, 0.15, 0.05],
                            [0   , 0.1 , 0.15, 0.05, 0.15, 0.25, 0.05, 0.1 , 0.15],
                            [0.2 , 0.1 , 0.05, 0.1 , 0.05, 0.05, 0.1 , 0.15, 0.2 ],
                            [0.1 , 0.15, 0.1 , 0.05, 0.1 , 0.05, 0.15, 0.2 , 0.1 ],
                            [0.05, 0.1 , 0.1 , 0.1 , 0.05, 0.15, 0.25, 0.15, 0.05],
                            [0.05, 0.1 , 0.15, 0.05, 0.1 , 0.15, 0.1 , 0.2 , 0.1 ],
                            [0.1 , 0.1 , 0.05, 0.1 , 0.1 , 0.05, 0.1 , 0.2 , 0.2 ],
                            [0.15, 0.1 , 0.05, 0.2 , 0.15, 0   , 0.05, 0.1 , 0.2 ]
    ]

    # You have to have at least 1 modest house in a neighborhood!
    initial_state = 'H2'

    markov_chain = MarkovChain(transition_matrix, states)

    next_num_states = markov_chain.generate_states(initial_state, 16)

    # Setting up the screen and turtle settings
    screen = turtle.Screen()
    screen.setup(900, 900)
    turtle.speed(speed='fastest')
    turtle.penup()
    draw_road_system()

    coords_to_draw_at = [   [-450,337.5],[-450,112.5],[-450,-112.5],[-450,-337.5],
                            [-225,337.5],[-225,112.5],[-225,-112.5],[-225,-337.5],
                            [0,337.5],[0,112.5],[0,-112.5],[0,-337.5],
                            [225,337.5],[225,112.5],[225,-112.5],[225,-337.5]
    ]                            

    for i in range(len(next_num_states)):
        drawing_type = next_num_states[i][0]
        drawing_quantity = int(next_num_states[i][1])

        if drawing_type == 'P':
            draw_people(drawing_quantity, coords_to_draw_at[i][0] + (10*(i%3)), coords_to_draw_at[i][1])

        elif drawing_type == 'H':
            draw_house(drawing_quantity, coords_to_draw_at[i][0] + (10*(i%3)), coords_to_draw_at[i][1])

        elif drawing_type == 'F':
            draw_forest(drawing_quantity, coords_to_draw_at[i][0] + (10*(i%3)), coords_to_draw_at[i][1])




    turtle.done()