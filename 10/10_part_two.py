import re
import numpy
import pulp

INPUT_FILENAME = 'input'

# over-commented because this is me learning about pulp and linear programming in real time
def solve(operations, desired_state):
    lpProblem = pulp.LpProblem()
    n_operations = len(operations)
    n_state = len(desired_state)

    # matrix defining whether each operation affects each index in the state (1) or not (0, default)
    state_ops_matrix = numpy.zeros((n_state, n_operations))
    for operation_index, operation in enumerate(operations):
        for state_index in operation:
            state_ops_matrix[state_index, operation_index] = 1

    # define the decision variables. each op gets a variable containing the number of applications of that op
    max_applications = max(desired_state)
    operation_variables = [
        pulp.LpVariable(f"x{operation}", lowBound=0, upBound=max_applications, cat='Integer')
        for operation
        in range(n_operations)
    ]

    # define the objective. we are using lpMinimize, so pulp now knows to minimize for the sum of the vars defined above
    lpProblem += pulp.lpSum(operation_variables)

    # define the constraints per index of the state.
    # basically, we are multiplying a 0 or a 1 (from the matrix) by the amount of times the operation is applied, and
    # the sum of the amount of times EACH op is applied should evaluate to the desired state for each of its indices
    # (nb: pulp creates an lpConstraint when __eq__ is called (via == ). the comparison is not immediately evaluated!)
    for state_index in range(n_state):
        constraint = pulp.lpSum(
            state_ops_matrix[state_index, operation_index] * operation_variables[operation_index]
            for operation_index
            in range(n_operations)
        ) == desired_state[state_index]
        lpProblem += constraint

    # solve
    lpProblem.solve()
    return pulp.value(lpProblem.objective)


with open(INPUT_FILENAME) as file:
    lines = [line.strip() for line in file]
    tally = 0

    for line in lines:
        desired_state = [
            int(value)
            for value
            in re.findall(r"{(.*?)}", line)[0].split(',')
        ]
        operations = [
            [int(value) for value in operation.split(',')]
            for operation
            in re.findall("\\((.*?)\\)", line)
        ]
        tally += solve(operations, desired_state)

    print(tally)
