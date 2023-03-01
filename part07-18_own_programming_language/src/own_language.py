from string import ascii_uppercase, ascii_lowercase, digits


def run(program: list) -> list:
    variables = {variable: 0 for variable in ascii_uppercase}

    prints = []
    i = 0
    while i < len(program):
        # PRINTING
        if program[i].startswith("PRINT"):
            value = program[i].replace("PRINT ", "")
            if value in variables.keys():
                prints.append(variables[value])
            else:
                prints.append(int(value))
            i += 1
        # VARIABLE ASSIGNMENT
        elif program[i].startswith("MOV"):
            variable, value = program[i].replace("MOV ", "").split()
            if value in variables.keys():
                variables[variable] = variables[value]
            else:
                variables[variable] = int(value)
            i += 1
        # ADDITION
        elif program[i].startswith("ADD"):
            variable, value = program[i].replace("ADD ", "").split()
            if value in variables.keys():
                variables[variable] += variables[value]
            else:
                variables[variable] += int(value)
            i += 1
        # SUBTRACT
        elif program[i].startswith("SUB"):
            variable, value = program[i].replace("SUB ", "").split()
            if value in variables.keys():
                variables[variable] -= variables[value]
            else:
                variables[variable] -= int(value)
            i += 1
        # MULTIPLICATION
        elif program[i].startswith("MUL"):
            variable, value = program[i].replace("MUL ", "").split()
            if value in variables.keys():
                variables[variable] *= variables[value]
            else:
                variables[variable] *= int(value)
            i += 1
        # JUMP POINT
        elif program[i].endswith(":"):
            i += 1
        # JUMP
        elif program[i].startswith("JUMP"):
            location = program[i].replace("JUMP ", "")
            i = program.index(location + ":")
        # CONDITIONS
        elif program[i].startswith("IF"):
            conditional, location = program[i].replace("IF ", "").split(" JUMP ")
            value1, operator, value2 = conditional.split()

            if value1 in variables.keys():
                value1 = variables[value1]
            else:
                value1 = int(value1)
            if value2 in variables.keys():
                value2 = variables[value2]
            else:
                value2 = int(value2)

            if operator == "==":
                if value1 == value2:
                    i = program.index(location + ":")
                    continue
            elif operator == "!=":
                if value1 != value2:
                    i = program.index(location + ":")
                    continue
            elif operator == "<":
                if value1 < value2:
                    i = program.index(location + ":")
                    continue
            elif operator == "<=":
                if value1 <= value2:
                    i = program.index(location + ":")
                    continue
            elif operator == ">":
                if value1 > value2:
                    i = program.index(location + ":")
                    continue
            elif operator == ">=":
                if value1 >= value2:
                    i = program.index(location + ":")
                    continue
            i += 1

        elif program[i] == "END":
            return prints
    return prints


if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
