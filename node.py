import pydot


class Node:
    goal_state = [0, 0, 0]
    num_of_instances = 0

    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        if self.is_killed():
            color = "red"
        elif self.goal_test():
            color = "green"
        else:
            color = "orange"
        self.graph_node = pydot.Node(str(self), style="filled", fillcolor=color)
        Node.num_of_instances += 1

    def __str__(self):
        return str(self.state)

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    def is_valid(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        boat = self.state[2]
        if missionaries < 0 or missionaries > 3:
            return False
        if cannibals < 0 or cannibals > 3:
            return False
        if boat > 1 or boat < 0:
            return False
        return True

    def is_killed(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if cannibals > missionaries > 0:
            return True
        # Check for the other side
        # if cannibals < missionaries < 3:
        #     return True

    def generate_child(self):
        # children = []
        # depth = self.depth + 1
        # op = -1  # Subtract
        # if self.state[2] == 0:
        #     op = 1  # Add
        # for x in range(3):
        #     for y in range(3):
        #         # by_move = "Move %s missionaries and %s cannibals %s" % (x, y, boat_move)
        #         new_state = self.state.copy()
        #         new_state[0], new_state[1], new_state[2] = new_state[0] + op * x, new_state[1] + op * y, new_state[
        #             2] + op * 1
        #         action = [x, y, op]
        #         new_node = Node(new_state, self, action, depth)
        #         if 1 <= x + y <= 2:
        #             children.append(new_node)
        # return children

        children = []
        depth = self.depth + 1

        missionary = self.state[0]
        cannibal = self.state[1]
        boat_position = self.state[2]

        if boat_position == 1:
            """0M 1C"""
            if 1 <= cannibal <= 3:
                action = [0, 1]
                new_state_0, new_state_1, new_state_2 = missionary - action[0], cannibal - action[1], 0
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """0M 2C"""
            if 2 <= cannibal <= 3:
                action = [0, 2]
                new_state_0, new_state_1, new_state_2 = missionary - action[0], cannibal - action[1], 0
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """1M 0C"""
            if 1 <= missionary <= 3:
                action = [1, 0]
                new_state_0, new_state_1, new_state_2 = missionary - action[0], cannibal - action[1], 0
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """1M 1C"""
            if 1 <= missionary <= 3 and 1 <= cannibal <= 3:
                action = [1, 1]
                new_state_0, new_state_1, new_state_2 = missionary - action[0], cannibal - action[1], 0
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """2M OC"""
            if 2 <= missionary <= 3:
                action = [2, 0]
                new_state_0, new_state_1, new_state_2 = missionary - action[0], cannibal - action[1], 0
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

        if boat_position == 0:

            missionaryR = 3 - missionary
            cannibalR = 3 - cannibal

            """0M 1C"""
            if 1 <= cannibalR <= 3:
                action = [0, 1]
                new_state_0, new_state_1, new_state_2 = missionary + action[0], cannibal + action[1], 1
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """0M 2C"""
            if 2 <= cannibalR <= 3:
                action = [0, 2]
                new_state_0, new_state_1, new_state_2 = missionary + action[0], cannibal + action[1], 1
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """1M 0C"""
            if 1 <= missionaryR <= 3:
                action = [1, 0]
                new_state_0, new_state_1, new_state_2 = missionary + action[0], cannibal + action[1], 1
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """1M 1C"""
            if 1 <= missionaryR <= 3 and 1 <= cannibalR <= 3:
                action = [1, 1]
                new_state_0, new_state_1, new_state_2 = missionary + action[0], cannibal + action[1], 1
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

            """2M 0C"""
            if 2 <= missionaryR <= 3:
                action = [2, 0]
                new_state_0, new_state_1, new_state_2 = missionary + action[0], cannibal + action[1], 1
                new_state = [new_state_0, new_state_1, new_state_2]
                new_node = Node(new_state, self, action, depth)
                # if check_validity(new_state):
                children.append(new_node)

        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.action)
        # solution = solution[:-1]
        solution.reverse()
        return solution
