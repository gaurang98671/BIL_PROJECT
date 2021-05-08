import csv
import kmeans

class Controller:
    _path = None
    list_csv = []

    def set_path(self, path):
        self._path = path
        with open(path, 'r') as file:
            reader = csv.reader(file)
            self.list_csv = list(reader)
            file.close()

    def get_path(self):
        return self._path

    # Fetch numeric rows
    def get_numeric_rows(self):
        if self._path is None:
            return []
        else:
            col_names = []

            for i in range(len(self.list_csv[0])):
                if self.list_csv[1][i].replace('.','',1).isdigit():


                    col_names.append(self.list_csv[0][i])

            return  col_names

    # Get clusters
    def get_clusters(self, column1, column2, k):
        max_x = 0
        max_y = 0
        #get lists indexes
        #Loop through file and make list of all tuples
        #Call calculate_kmeans function
        first_index = self.list_csv[0].index(column1)
        second_index = self.list_csv[0].index(column2)

        coordinates =[]

        for i in self.list_csv[1:]:
            
            first_coord = i[first_index].strip()
            second_coord = i[second_index].strip()
            if first_coord == '':
                first_coord = 0
            if second_coord == '':
                second_coord = 0

            #Set max_x and max_y
            if float(first_coord) > max_x:
                max_x = float(first_coord)

            if float(second_coord) > max_y:
                max_y = float(second_coord)


            coordinate = (float(first_coord), float(second_coord))
            coordinates.append(coordinate)

        return kmeans.calculate_kmeans_clusters(k, 2, coordinates), max_x, max_y

