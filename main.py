from future.moves import tkinter as T
from tkinter.filedialog import askopenfilename
import Controller
import display_cluster

def main_screen():
    # Create class obj
    root = T.Tk()
    root.title("BIL TOOL")
    path_str = T.StringVar()
    column1 = T.StringVar()
    column2 = T.StringVar()
    root.resizable(False, False)
    csv_controller = Controller.Controller()

    def upload_file():
        T.Tk().withdraw()
        filename = askopenfilename()
        path_str.set(filename)
        txt_path.insert(0, filename)
        # Check weather file is csv

        # Set file path in object
        csv_controller.set_path(path_str.get())

        # Get numeric row names
        numeric_columns = csv_controller.get_numeric_rows()

        # Set two option menus
        column1.set("Select first argument")
        column2.set("Select second argument")
        column1_option = T.OptionMenu(root, column1, *numeric_columns)
        column2_option = T.OptionMenu(root, column2, *numeric_columns)


        # Set text box for cluster
        lbl_cluster = T.Label(root, text="Clusters")
        clusters = T.Entry(root)

        # Add calculate button
        calculate = T.Button(text='Calculate', command= lambda : display_cluster.display_cluster(csv_controller.get_clusters(column1.get(), column2.get(), int(clusters.get()))))
        # Add everything to grid
        clusters.grid(row=4, column=4)
        lbl_cluster.grid(row=4, column=3)

        column1_option.grid(row=5, column=4)
        column2_option.grid(row=6, column=4)

        calculate.grid(row=8, column=4)

        # Pass clusters, first column, second column to get_page

    # Upload file
    txt_path = T.Entry(root)
    btn_add = T.Button(root, text='Browse', command=lambda: upload_file())
    lbl_file = T.Label(root, text="Upload csv")
    lbl_file.grid(row=3, column=3)
    txt_path.grid(row=3, column=4)
    btn_add.grid(row=3, column=5)

    root.geometry("300x300")
    root.mainloop()


if __name__ == '__main__':
    main_screen()
