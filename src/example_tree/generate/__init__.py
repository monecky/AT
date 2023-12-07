from src.example_tree.generate.generateAT import generateAT

import os


def main(amount: int, no_multi_parent: int, max_no_bas: int, max_weight: int):
    folder_path = "generate" +str(amount) +str(no_multi_parent) + str(max_no_bas) + str(max_weight)
    file_name = "/tree"
    # Created path if not already there
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for i in range(amount):
        at = generateAT(no_multi_parent, max_no_bas, max_weight)
        file_name = "/tree" + str(i) + ".at"
        if not os.path.exists(folder_path + file_name):
            with open(folder_path + file_name, 'w') as file:
                file.write(at)
        else:
            print(f"The file {folder_path + file_name} already exists.")


if __name__ == "__main__":
    main(100,100,100,100)
