import math

#inputs

k=2
number_of_coordinates=2
inputs =[(1.0, 1.0), (2.0, 3.0), (2.0, 4.0)]

def calculate_kmeans_clusters(k , number_of_coordinates, inputs):
    final_cluster ={}
    if k > len(inputs):
        print("Wont work!!")
    else:
        intervals = math.floor(len(inputs) / k)
        centers = []
        new_centers = []

        # finding centers
        for i in range(k):
            centers.append(inputs[intervals * (i)])



        a = True
        while a:

            # Creating empty cluster
            cluster = {j: [] for j in centers}
            for i in inputs:
                # min_distance= eucledian dist if (x, y)
                min_distance = float("inf")
                distance_with = 0
                # finding distance with all centers
                for j in centers:
                    distance = math.sqrt(sum([(i[r] - j[r]) ** 2 for r in range(number_of_coordinates)]))
                    if distance < min_distance:
                        min_distance = distance
                        distance_with = j

                # adding min distance with respective center as a key in cluster
                cluster[distance_with].append(i)



            # computing new centers
            new_centers = [
                tuple(
                    [sum([y[r] for y in x]) / len(x) for r in range(number_of_coordinates)]  # r= 0,1
                )
                for x in cluster.values()]

            if new_centers == centers:

                final_cluster= cluster
                a = False

            else:
                centers = new_centers


    return  final_cluster







