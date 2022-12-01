import numpy as np
from numpy.typing import ArrayLike


def part_one() -> np.ndarray:
    """
    Builds a list of total calorie counts for each elf, then picks out the max.

    Could do this more efficiently by not storing the whole list and just updating
        a max_calorie counter, at the cost of some flexibility for later analysis.
    """

    elf_contents = []

    counter = 0
    with open("input_data", "r") as inf:

        for line in inf.readlines():
            line = line.strip("\n")

            if line == "":
                elf_contents.append(counter)
                counter = 0

            else:
                counter += int(line)

    print(max(elf_contents))

    return elf_contents


def part_two(elf_contents: ArrayLike) -> np.ndarray:
    """
    Take the array of elf calorie counts, pick the 3 highest, and then sum those.
    """

    top_3 = np.sort(elf_contents)[-3:]

    print(top_3.sum())


if __name__ == "__main__":

    elf_contents = part_one()

    part_two(elf_contents)
