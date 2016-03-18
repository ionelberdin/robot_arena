import numpy as np


def get_collision_with_circles(position, target, radius, circles):
    """
    """
    A = np.array(position)
    B = np.array(target)
    AB = B - A
    ABn = np.linalg.norm(AB)
    collisions = []

    for C, r in circles:
        C = np.array(C)
        AC = C - A
        ACn = np.linalg.norm(AC)
        projection = AC.dot(AB) / ABn
        dist = np.sqrt(ACn**2 - projection**2)
        radii_sum = r + radius
        is_between_AB = (projection * AB.dot(B - C) > 0)
        is_close_to_B = np.linalg.norm(C - B) < radii_sum

        if radii_sum < dist and (is_between_AB or is_close_to_B):
            # save collision location
            correction = np.sqrt(radii_sum**2 - dist**2)
            distance_b4_collision = projection - correction
            position_b4_collision = A + AB / ABn * distance_b4_collision
            collisions.append((position_b4_collision, (C, r)))

    return collisions


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

    critical_pit_tuple = dangerous_pits.sort(key=lambda item: item[2])[0]
    return critical_pit_tuple


def simulate_move(game_state, target):
    """
    Given a game_state and a desired target,
    returns the possible outcome as a potential game_state
    """

    # don't die when the movement finishes
    die = False

    # create caravan (robots identified by their turn number: 0, 1, 2 & 3)
    caravan = [game_state["turn"] % 4]
    pushed = [[], ]
    pusher = [None]

    # check for pits in pusher way
    critical_pit = get_critical_pit()

    if critical_pit is not None:
        # update target
        die = True
        target = critical_pit[3]

    check_again = True
    while check_again:
        check_again = False
        for robot_id in caravan:
            pass

    # check for adversaries in the way

    # check wall collision

    #


if __name__ == "__main__":
    # test and debug
    pass
