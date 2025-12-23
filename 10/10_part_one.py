import re

INPUT_FILENAME = 'input'


def press_button(state, button):
    result = list(state)
    for index in button:
        result[int(index)] = '#' if result[int(index)] == '.' else '.'
    return tuple(result)


def shortest_path_bfs(desired_state, buttons):
    initial_state = tuple('.' * len(desired_state))

    states_to_check = {initial_state}
    states_seen = {initial_state}
    depth = 0

    while states_to_check:
        depth += 1
        new_unseen_states = set()
        for state in states_to_check:
            for button in buttons:
                resulting_state = press_button(state, button)
                if resulting_state == desired_state:
                    return depth
                if resulting_state not in states_seen:
                    states_seen.add(resulting_state)
                    new_unseen_states.add(resulting_state)
        states_to_check = new_unseen_states
    return depth


with open(INPUT_FILENAME) as file:
    lines = [line.strip() for line in file]
    results = []

    for line in lines:
        desired_state = tuple(re.findall(r"\[(.*?)]", line)[0])
        buttons = [tuple(button.split(',')) for button in re.findall("\\((.*?)\\)", line)]
        results.append(shortest_path_bfs(desired_state, buttons))

    print(sum(results))
