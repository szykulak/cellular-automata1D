class CellularAutomata1D(object):

    def __init__(self, iteration_amount, grid_size, init_state, rule):
        self.iteration_amount = iteration_amount
        self.init_space = init_state
        self.grid_size = grid_size
        self.rule = rule
        self.rule_binary = format(rule, '08b')  # so there are 8 bits
        self.ruleset = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)]

    def calculate_next_state(self):
        next_states = []
        for i in range(0, len(self.init_space)):
            if i == 0:
                previous_neighbor = len(self.init_space) - 1  # periodic boundary condition
            else:
                previous_neighbor = i - 1

            if i == len(self.init_space) - 1:  # same as above
                next_neighbor = 0
            else:
                next_neighbor = i + 1

            neighborhood = [self.init_space[previous_neighbor], self.init_space[i], self.init_space[next_neighbor]]
            for j in range(0, len(self.ruleset)):
                if tuple(neighborhood) == self.ruleset[j]:
                    next_states.append(int(self.rule_binary[j]))
        self.init_space = next_states
        return self.init_space

    def generate_automaton(self):
        state_array = [[0 for x in range(len(self.init_space))] for y in range(self.iteration_amount)]
        state_array[0] = self.init_space
        for i in range(1, self.iteration_amount):
            state_array[i] = self.calculate_next_state()
        return state_array
