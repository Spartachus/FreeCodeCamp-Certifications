def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_part = []
    second_part = []
    operators = []

    for problem in problems:
        pieces = problem.split()
        first_part.append(pieces[0])
        operators.append(pieces[1])
        second_part.append(pieces[2])

    # Check for * or /
    if "*" in operators or "/" in operators:
        return "Error: Operator must be '+' or '-'."

    for i in range(len(first_part)):
        if not (first_part[i].isdigit() and second_part[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(first_part)):
        if len(first_part[i]) > 4 or len(second_part[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    line_one = []
    line_two = []
    dashes_line = []
    answer_line = []
    for i in range(len(first_part)):
        dashes_line.append(
            "-"*(max(len(first_part[i]), len(second_part[i])) + 2))
    for i in range(len(first_part)):
        if len(first_part[i]) > len(second_part[i]):
            line_one.append(" "*2 + first_part[i])
        else:
            line_one.append(
                " "*(len(second_part[i]) - len(first_part[i]) + 2) + first_part[i])

    for i in range(len(second_part)):
        if len(second_part[i]) > len(first_part[i]):
            line_two.append(operators[i] + " " + second_part[i])
        else:
            line_two.append(
                operators[i] + " "*(len(first_part[i]) - len(second_part[i]) + 1) + second_part[i])

    if answer:
        for i in range(len(first_part)):
            if operators[i] == "+":
                ans = str(int(first_part[i]) + int(second_part[i]))
            else:
                ans = str(int(first_part[i]) - int(second_part[i]))

            if len(ans) > max(len(first_part[i]), len(second_part[i])):
                answer_line.append(" " + ans)
            else:
                answer_line.append(
                    " "*(max(len(first_part[i]), len(second_part[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(line_one) + "\n" + "    ".join(
            line_two) + "\n" + "    ".join(dashes_line) + "\n" + "    ".join(answer_line)
    else:
        arranged_problems = "    ".join(
            line_one) + "\n" + "    ".join(line_two) + "\n" + "    ".join(dashes_line)
    return arranged_problems
