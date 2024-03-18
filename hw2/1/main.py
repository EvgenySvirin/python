from hw2.lib.src.utils import create_tex_content_from_table


if __name__ == "__main__":
    table1 = []
    table2 = [[1, 2, 3]]
    table3 = [[1, 2, 3],
              [4, 5, 6]]

    with open("../artifacts/1/table1.tex", "w") as file:
        file.write(create_tex_content_from_table(table1))

    with open("../artifacts/1/table2.tex", "w") as file:
        file.write(create_tex_content_from_table(table2))

    with open("../artifacts/1/table3.tex", "w") as file:
        file.write(create_tex_content_from_table(table3))