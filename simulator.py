import numpy as np


def get_collision_with_circles(position, target, radius, circles):
    """
    """
    pass


def get_critical_pit(position, target, robot_width, pits_and_widths):
    """
    Input:
        position: starting point
        target: final point
        robot_width: diameter of the robot
        pits_and_widths: list of tuples that contain (pit_position, pit_width)

    Output:
        Tuple with information about critical pit or None.
        (pit_position,
         pit_width,  # diameter actually
         travelled_distance_before_falling,
         final_point_before_falling)
    """

    A = np.array(position)
    B = np.array(target)
    AB = B - A
    AB_norm = np.linalg.norm(AB)
    AB_unit = AB / AB_norm
    r = robot_width / 2.

    dangerous_pits = []

    for pit_pos, pit_width in pits_and_widths:
        P = np.array(pit_pos)
        rp = pit_width / 2.
        AP = P - A
        tan_dist = np.dot(AB, AP)
        norm_dist = np.sqrt(np.dot(AP, AP) - tan_dist)

        cond1 = norm_dist < r + rp and 0 < tan_dist < AB_norm
        cond2 = np.linalg.norm(P - B) < r + rp
        if cond1 or cond2:
            correction = np.sqrt((r + rp)**2 - norm_dist**2)
            travelled = tan_dist - correction
            last_point = A + AB_unit * travelled
            dangerous_pits.append((pit_pos, pit_width, travelled, last_point))

    if len(dangerous_pits) == 0:
        return None

    dangerous_pits.sort(key=lambda item: item[2])
    return dangerous_pits[0]


def simulate_move(game_state, target):
    """
    Given a game_state and a desired target,
    returns the possible outcome as a potential game_state
    """

    # check for pits in the way
    critical_pit = get_critical_pit()

    # check for adversaries in the way

    # check wall collision

    #


if __name__ == "__main__":
    # test and debug
    pass
