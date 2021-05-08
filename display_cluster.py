from matplotlib import pyplot as plt
def display_cluster(data):
    data_lis = list(data[0].values())
    for i in data_lis:
        plt.scatter([x[0] for x in i],[x[1] for x in i])
    plt.show()



