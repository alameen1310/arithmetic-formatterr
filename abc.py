def arithmetic_arranger(problems, compute=False):
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for i in problems:
        first, ops, second = i.split()
        if not first.isnumeric() or not second.isnumeric():
            return 'Error: Numbers must only contain digits.'
        elif len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif (ops == '+' or ops == '-'):
            if ops == "+":
                total = int(first) + int(second)
            else:
                total = int(first) - int(second)
            width = max(len(first), len(second)) + 2
            l1 = str(first).rjust(width)
            l2 = ops + str(second).rjust(width -1)
            l3 = "-" * width
            l4 = str(total).rjust(width)
            
            if i == problems[:-1]:
                line1 += l1
                line2 += l2
                line3 += l3
                line4 += l4
            else:
                line1 += l1 + '    '
                line2 += l2 + '    '
                line3 += l3 + '    '
                line4 += l4 + '    '
        else:
            return "Error: Operator must be '+' or '-'."
    
    if compute:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3
    
    return arranged_problems