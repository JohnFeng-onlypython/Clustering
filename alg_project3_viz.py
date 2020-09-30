"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import urllib.request
import alg_cluster

# conditional imports
if DESKTOP:
    import at_rice_w2_15     # desktop project solution
    import alg_clusters_matplotlib
else:
    #import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
    import alg_clusters_simplegui
    import codeskulptor
    codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

import random
import urllib.request
import poc_simpletest      # http://www.codeskulptor.org/#poc_simpletest.py
import alg_cluster
DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
DATA_24_URL = DIRECTORY + "data_clustering/unifiedCancerData_24.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib.request.urlopen(data_url)
    data = data_file.read()
    data_lines = data.decode().split('\n')
    print("Loaded", len(data_lines), "data points")
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering
    
    Note that method may return num_clusters or num_clusters + 1 final clusters
    """
    
    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters
    
    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)
            
    return cluster_list
                

#####################################################################
# Code to load cancer data, compute a clustering and 
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_896_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    def compute_distortion(cluster_list):
        error = 0
        for cluster in cluster_list:
            error += cluster.cluster_error(data_table)
        return error
    error = []
    for cluster_num in range(6, 21):
        cluster_list = hierarchical_clustering(singleton_list, cluster_num)
        error.append(compute_distortion(cluster_list))
        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    return error
    #cluster_list = sequential_clustering(singleton_list, 9)
    #print("Displaying", len(cluster_list), "hierarchical clusters")


    print("Displaying", len(cluster_list), "hierarchical clusters")

    #cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 5)	
    #print "Displaying", len(cluster_list), "k-means clusters"

            
    # draw the clusters using matplotlib or simplegui
    if DESKTOP:
        #alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)   # use toggle in GUI to add cluster centers
    
#run_example()

def run_kmeans_example():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """



    data_table = load_data_table(DATA_896_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    def compute_distortion(cluster_list):
        error = 0
        for cluster in cluster_list:
            error += cluster.cluster_error(data_table)
        return error
    error = []
    for cluster_num in range(6, 21):
        cluster_list = kmeans_clustering(singleton_list, cluster_num, 5)
        error.append(compute_distortion(cluster_list))
        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    return error

    print("Displaying", len(cluster_list), "kmeans clusters")

    # cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)
    # print "Displaying", len(cluster_list), "hierarchical clusters"

    # cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 5)
    # print "Displaying", len(cluster_list), "k-means clusters"

    # draw the clusters using matplotlib or simplegui
    if DESKTOP:
        # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  # add cluster centers
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)  # use toggle in GUI to add cluster centers

#run_kmeans_example()



def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    cluster_list = list(cluster_list)
    length = len(cluster_list)
    center = []
    cluster_list.sort(key=lambda cluster: cluster.total_population())
    center = cluster_list[-num_clusters:]

    for dummy_itr in range(num_iterations):
        cluster = []
        for num in range(num_clusters):
            cluster.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0))
        for time in range(length):
            distance = float('inf')
            clos = -1
            for center_idx in range(num_clusters):
                dis = cluster_list[time].distance(center[center_idx])
                if dis < distance:
                    distance = dis
                    clos = center_idx
            cluster[clos].merge_clusters(cluster_list[time])
        center = list(cluster)
    return center


def hierarchical_clustering(cluster_list, num_clusters):
    length = len(cluster_list)
    while length > num_clusters:
        distance, idx_i, idx_j = fast_closest_pair(cluster_list)
        if idx_i >= 0 and idx_j >= 0:
            pair = cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
            f_remove = cluster_list[idx_i]
            s_remove = cluster_list[idx_j]
            cluster_list.append(pair)
            cluster_list.remove(f_remove)
            cluster_list.remove(s_remove)
        length = len(cluster_list)

    return cluster_list


def closest_pair_strip(cluster_list, horiz_center, half_width):
    '''
    find out whether there are points one for each side, around the midline that are omitted but has the smallest distance
    '''
    select_list = []
    for point in cluster_list:
        if math.fabs(point.horiz_center() - horiz_center) < half_width:
            select_list.append(point)
    select_list.sort(key=lambda cluster: cluster.vert_center())
    #     print(select_list)
    length = len(select_list)
    dis = float('inf')
    idx_i = -1
    idx_j = -1
    if length < 2:
        return dis, idx_i, idx_j
    for idx_1 in range(length - 1):
        for idx_2 in range(idx_1 + 1, min([idx_1 + 4, length])):
            distance_p = select_list[idx_1].distance(select_list[idx_2])
            if dis >= distance_p:
                dis = distance_p
                idx_i = idx_1
                idx_j = idx_2

    for num in range(len(cluster_list)):
        if cluster_list[num] == select_list[idx_i]:
            idx_a = num
        elif cluster_list[num] == select_list[idx_j]:
            idx_b = num
    if idx_a < idx_b:
        return (dis, idx_a, idx_b)
    else:
        return (dis, idx_b, idx_a)


def fast_closest_pair(cluster_list):
    '''
    using the recursions to find the smallest distance between 2 point
    '''
    cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    length = len(cluster_list)
    if length <= 3:
        (dis, idx_i, idx_j) = slow_closest_pair(cluster_list)
    else:
        mid = int(math.floor(length / 2))
        (d_l, i_l, j_l) = fast_closest_pair(cluster_list[0: mid])
        (d_r, i_r, j_r) = fast_closest_pair(cluster_list[mid:])
        if d_l < d_r:
            (dis, idx_i, idx_j) = (d_l, i_l, j_l)
        else:
            (dis, idx_i, idx_j) = (d_r, i_r + mid, j_r + mid)

        mid = (cluster_list[mid - 1].horiz_center() + cluster_list[mid].horiz_center()) * 0.5
        (d_c, i_c, j_c) = closest_pair_strip(cluster_list, mid, dis)
        if d_c < dis:
            dis = d_c
            idx_i = i_c
            idx_j = j_c
    if idx_i < idx_j:
        return (dis, idx_i, idx_j)
    else:
        return (dis, idx_j, idx_i)

def slow_closest_pair(cluster_list):
    '''
    using the brute force to find the smallest distance between 2 point
    '''
    distance = float('inf')
    idx_1 = -1
    idx_2 = -1
    for idx_f in range(len(cluster_list)):
        for idx_s in range(len(cluster_list)):
            if idx_f != idx_s:
                distance_cluster = cluster_list[idx_f].distance(cluster_list[idx_s])
                if distance_cluster < distance:
                    distance = distance_cluster
                    idx_1 = idx_f
                    idx_2 = idx_s
    if idx_1 < idx_2:
        return distance, idx_1, idx_2
    else:
        return distance, idx_2, idx_1


        






        




