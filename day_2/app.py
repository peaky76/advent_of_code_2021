import operator


class Position:
    
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        
    def apply_part_one_command(self, command):
        if command.direction == 'forward':
            self.horizontal += command.amount
        elif command.direction == 'down':
            self.depth += command.amount
        elif command.direction == 'up':
            self.depth -= command.amount
        else:
            pass
        
    def apply_part_two_command(self, command):
        if command.direction == 'forward':
            self.horizontal += command.amount
            self.depth += (command.amount * self.aim)
        elif command.direction == 'down':
            self.aim += command.amount
        elif command.direction == 'up':
            self.aim -= command.amount
        else:
            pass
       
    @property 
    def output(self):
        return self.horizontal * self.depth   
     
            
class Command:

    def __init__(self, direction, amount):
        self.direction = direction
        self.amount = int(amount)


file = open("puzzle_input.txt", "r")
raw_commands = [line.rstrip('\n').split(' ') for line in file]
commands = [Command(*raw_command) for raw_command in raw_commands]

# PART ONE
position = Position()
for command in commands:
    position.apply_part_one_command(command)
    
print(position.output) #1507611

#PART TWO
position = Position()
for command in commands:
    position.apply_part_two_command(command)
    
print(position.output) #1880593125

