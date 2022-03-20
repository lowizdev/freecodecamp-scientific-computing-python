def arithmetic_arranger(problems, isAnswersDisplayable = False):
    if(len(problems) > 5):
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    tabs_line = ""
    result_line = ""

    for problem in problems:
        splitted_problem = problem.split()

        operator = splitted_problem[1]

        first_operand = splitted_problem[0]
        second_operand = splitted_problem[2]

        if(not first_operand.isdigit() or not second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        maximum_length = len(first_operand)
        if(len(second_operand) > maximum_length):
            maximum_length = len(second_operand)
        
        if(maximum_length > 4):
            return "Error: Numbers cannot be more than four digits."
        current_result = ""
        
        if(operator == "+"):
            current_result = str(int(first_operand) + int(second_operand))
        elif(operator == "-"):
            current_result = str(int(first_operand) - int(second_operand))
        else:
            return "Error: Operator must be '+' or '-'."

        tabs_length = maximum_length + 2
        first_line += " " * (tabs_length - len(first_operand)) + first_operand + 4 * " "
        second_line += operator + " " * (tabs_length - 1 - len(second_operand)) + second_operand + 4 * " "
        tabs_line += ("-" * tabs_length) + 4 * " "
        result_line += " " * (tabs_length - len(current_result)) + current_result + 4 * " "
      
      
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    tabs_line = tabs_line.rstrip()
    result_line = result_line.rstrip()
    
    arranged_problems = first_line + "\n" + second_line + "\n" + tabs_line
    
    if(isAnswersDisplayable):
        arranged_problems += "\n" + result_line
  
    return arranged_problems