def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    room_assignment = []
    for i, name in enumerate(names):
        room_number = i + 1
        room_assignment.append("Hello, {}! You'll be assigned to room {}!".format(name, room_number))
    return room_assignment

def printer(names):
    badges = batch_badge_creator(names)
    room_assignment = assign_rooms(names)
    for badge in badges:
        print(badge)
    for assignment in room_assignment:
        print(assignment)

