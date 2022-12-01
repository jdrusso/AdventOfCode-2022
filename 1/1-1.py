import numpy as np

if __name__ == "__main__":
    """
    Builds a list of total calorie counts for each elf, then picks out the max.

    Could do this more efficiently by not storing the whole list and just updating 
        a max_calorie counter, at the cost of some flexibility for later analysis.
    """

    elf_contents = []

    counter = 0
    with open('input_data', 'r') as inf:

        for line in inf.readlines():
            line = line.strip('\n')

            if line == '':
                elf_contents.append(counter)
                counter = 0
                
            else:
                counter += int(line)

    print(max(elf_contents))