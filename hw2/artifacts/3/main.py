from latex_somethingsomething import utils as tex

if __name__ == "__main__":
    table1 = []
    table2 = [[1, 2, 3]]
    table3 = [[1, 2, 3],
            [4, 5, 6]]

    image = "mug.png"
    filename = "image_table.tex"
    with open(filename, "w") as file:
        tex_elements = tex.create_tex_table(table3)
        tex_elements += tex.create_tex_image(image)
        file_content = tex.wrap_with_tex_document(tex_elements)
        file.write(file_content)
        file.close()
    tex.create_pdf_file(filename, "image_table")

