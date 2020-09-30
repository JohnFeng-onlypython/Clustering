
# In[1]:


'''
algorithmthinking II week 2 cluster gathering
'''


# In[2]:


import math
import random
# import urllib.request
# import poc_simpletest      # http://www.codeskulptor.org/#poc_simpletest.py
import alg_cluster
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
                    
                    
    


# In[3]:


# slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)]) 


# In[4]:


def fast_closest_pair(cluster_list):
    '''
    using the recursions to find the smallest distance between 2 point
    '''
    cluster_list.sort(key = lambda cluster:cluster.horiz_center())
    length = len(cluster_list)
    if length <= 3:
        (dis, idx_i, idx_j) = slow_closest_pair(cluster_list)
    else:
        mid = int(math.floor(length / 2))
        (d_l, i_l, j_l) = fast_closest_pair(cluster_list[0: mid])
        (d_r, i_r, j_r) = fast_closest_pair(cluster_list[mid : ])
        if d_l < d_r:
            (dis, idx_i, idx_j) = (d_l, i_l, j_l)
        else:
            (dis, idx_i, idx_j) = (d_r, i_r + mid , j_r + mid)
        
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


# In[5]:


#fast_closest_pair([alg_cluster.Cluster(set([]), 1.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 5.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 7.0, 0.0, 1, 0)])


# In[6]:


#fast_closest_pair([alg_cluster.Cluster(set(['06081']), 52.6171444847, 262.707477827, 707161, 5.6e-05), alg_cluster.Cluster(set(['06075']), 52.7404001225, 254.517429395, 776733, 8.4e-05), alg_cluster.Cluster(set(['06001']), 61.782098866, 259.312457296, 1443741, 7e-05), alg_cluster.Cluster(set(['06085']), 63.1509653633, 270.516712105, 1682585, 6.3e-05), alg_cluster.Cluster(set(['06021']), 65.2043358182, 213.245337355, 26453, 6.9e-05), alg_cluster.Cluster(set(['06113']), 68.2602083189, 236.862609218, 168660, 5.9e-05), alg_cluster.Cluster(set(['06101']), 74.2003718491, 229.646592975, 78930, 5.6e-05), alg_cluster.Cluster(set(['06067']), 74.3547338322, 245.49501455, 1223499, 6.1e-05), alg_cluster.Cluster(set(['06083']), 76.0382837186, 340.420376302, 399347, 6.4e-05), alg_cluster.Cluster(set(['06089']), 77.359494209, 188.945068958, 163256, 5.7e-05), alg_cluster.Cluster(set(['41067']), 92.2254623376, 76.2593957841, 445342, 7.3e-05), alg_cluster.Cluster(set(['06111']), 93.4973310868, 344.590570899, 753197, 5.8e-05), alg_cluster.Cluster(set(['06019']), 95.6093812211, 290.162708843, 799407, 6.4e-05), alg_cluster.Cluster(set(['06039']), 97.2145136451, 278.975077449, 123109, 6e-05), alg_cluster.Cluster(set(['41051']), 103.293707198, 79.5194104381, 660486, 9.3e-05), alg_cluster.Cluster(set(['41005']), 103.421444616, 88.318590492, 338391, 6.6e-05), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['53011']), 104.00046468, 74.0182527309, 345238, 6.4e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06107']), 108.085024898, 306.351832438, 368021, 5.8e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['53033']), 125.27486023, 39.1497730391, 1737034, 5.8e-05), alg_cluster.Cluster(set(['06073']), 129.2075529, 387.064888184, 2813833, 6.6e-05), alg_cluster.Cluster(set(['06065']), 146.410389633, 374.21707964, 1545387, 6.1e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05), alg_cluster.Cluster(set(['06025']), 156.397958859, 393.161127277, 142361, 5.6e-05), alg_cluster.Cluster(set(['04013']), 214.128077618, 396.893960776, 3072149, 6.8e-05), alg_cluster.Cluster(set(['08031']), 371.038986573, 266.847932979, 554636, 7.9e-05), alg_cluster.Cluster(set(['08001']), 379.950978294, 265.078784954, 363857, 6.6e-05), alg_cluster.Cluster(set(['08005']), 380.281283151, 270.268826873, 487967, 5.9e-05), alg_cluster.Cluster(set(['31109']), 516.78216337, 250.188023316, 250291, 6.1e-05), alg_cluster.Cluster(set(['31055']), 525.799353573, 238.14275337, 463585, 6.2e-05), alg_cluster.Cluster(set(['48201']), 540.54731652, 504.62993865, 3400578, 6e-05), alg_cluster.Cluster(set(['48245']), 565.746895809, 504.541799993, 252051, 5.7e-05), alg_cluster.Cluster(set(['27053']), 570.131597541, 151.403325043, 1116200, 5.8e-05), alg_cluster.Cluster(set(['22017']), 570.826412839, 442.202574191, 252161, 6.2e-05), alg_cluster.Cluster(set(['27123']), 576.516685202, 151.219277482, 511035, 5.6e-05), alg_cluster.Cluster(set(['19163']), 621.490118929, 227.666851619, 158668, 5.6e-05), alg_cluster.Cluster(set(['29189']), 629.170659449, 297.571839563, 1016315, 6e-05), alg_cluster.Cluster(set(['28027']), 631.700027283, 400.68741948, 30622, 6e-05), alg_cluster.Cluster(set(['29510']), 632.327321169, 297.184524592, 348189, 6.9e-05), alg_cluster.Cluster(set(['28049']), 638.051593606, 445.785870317, 250800, 6e-05), alg_cluster.Cluster(set(['22071']), 651.338581076, 496.465402252, 484674, 6.4e-05), alg_cluster.Cluster(set(['28159']), 663.514261498, 425.274137823, 20160, 5.9e-05), alg_cluster.Cluster(set(['55079']), 664.855000617, 192.484141264, 940164, 7.4e-05), alg_cluster.Cluster(set(['17031']), 668.978975824, 219.400257219, 5376741, 6.1e-05), alg_cluster.Cluster(set(['47037']), 700.009323976, 350.107265446, 569891, 6.1e-05), alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['01117']), 709.193528999, 417.394467797, 143293, 5.6e-05), alg_cluster.Cluster(set(['21111']), 715.347723878, 301.167740487, 693604, 5.9e-05), alg_cluster.Cluster(set(['01101']), 720.281573781, 440.436162917, 223510, 5.7e-05), alg_cluster.Cluster(set(['01015']), 723.907941153, 403.837487318, 112249, 5.6e-05), alg_cluster.Cluster(set(['47065']), 732.643747577, 370.017730905, 307896, 6.1e-05), alg_cluster.Cluster(set(['13313']), 737.308367745, 378.040993858, 83525, 5.6e-05), alg_cluster.Cluster(set(['01113']), 740.385154867, 436.939588695, 49756, 5.6e-05), alg_cluster.Cluster(set(['26125']), 743.036942153, 192.129690868, 1194156, 5.7e-05), alg_cluster.Cluster(set(['13215']), 745.265661102, 430.987078939, 186291, 5.9e-05), alg_cluster.Cluster(set(['26163']), 746.37046732, 200.570021537, 2061162, 6.4e-05), alg_cluster.Cluster(set(['13067']), 747.238620236, 397.293799252, 607751, 6.4e-05), alg_cluster.Cluster(set(['13121']), 750.160287596, 399.907752014, 816006, 7e-05), alg_cluster.Cluster(set(['13063']), 752.853876848, 406.722877803, 236517, 6.6e-05), alg_cluster.Cluster(set(['47093']), 753.012743594, 348.235180569, 382032, 5.6e-05), alg_cluster.Cluster(set(['13089']), 754.465443436, 400.059456026, 665865, 6.8e-05), alg_cluster.Cluster(set(['13151']), 756.589546538, 407.288873768, 119341, 5.6e-05), alg_cluster.Cluster(set(['13135']), 758.038826857, 395.110327675, 588448, 6.3e-05), alg_cluster.Cluster(set(['13247']), 758.37864157, 402.49780372, 70111, 5.6e-05), alg_cluster.Cluster(set(['12073']), 762.463896365, 477.365342219, 239452, 6.1e-05), alg_cluster.Cluster(set(['21019']), 768.726553092, 290.270551648, 49752, 5.8e-05), alg_cluster.Cluster(set(['39035']), 776.351457758, 216.558042612, 1393978, 5.8e-05), alg_cluster.Cluster(set(['51520']), 784.05333332, 328.847863787, 17367, 5.6e-05), alg_cluster.Cluster(set(['13245']), 796.799727342, 404.391349655, 199775, 5.9e-05), alg_cluster.Cluster(set(['54009']), 799.221537984, 240.153315109, 25447, 7.7e-05), alg_cluster.Cluster(set(['42003']), 809.003419092, 233.899638663, 1281666, 6.1e-05), alg_cluster.Cluster(set(['37119']), 813.724315147, 356.853362811, 695454, 5.6e-05), alg_cluster.Cluster(set(['51775']), 820.111751617, 307.695502162, 24747, 5.8e-05), alg_cluster.Cluster(set(['51770']), 821.912162221, 307.548990323, 94911, 6.5e-05), alg_cluster.Cluster(set(['51680']), 835.264653899, 302.326633095, 65269, 5.8e-05), alg_cluster.Cluster(set(['51820']), 837.346467474, 285.851438947, 19520, 5.8e-05), alg_cluster.Cluster(set(['51840']), 845.843602685, 258.214178983, 23585, 7.1e-05), alg_cluster.Cluster(set(['51059']), 863.064397845, 262.414412378, 969749, 5.7e-05), alg_cluster.Cluster(set(['24031']), 863.180208628, 255.65657011, 873341, 6.5e-05), alg_cluster.Cluster(set(['51610']), 864.078108667, 261.655667801, 10377, 6.9e-05), alg_cluster.Cluster(set(['51760']), 865.424050159, 293.735963553, 197790, 8.6e-05), alg_cluster.Cluster(set(['51013']), 865.681962839, 261.222875114, 189453, 7.7e-05), alg_cluster.Cluster(set(['51087']), 866.389610525, 292.780704494, 262300, 6.3e-05), alg_cluster.Cluster(set(['51510']), 866.572477724, 262.734686855, 128283, 6.8e-05), alg_cluster.Cluster(set(['24027']), 867.127763298, 252.141340019, 247842, 6e-05), alg_cluster.Cluster(set(['11001']), 867.470401202, 260.460974222, 572059, 7.7e-05), alg_cluster.Cluster(set(['51570']), 868.048530719, 299.360459202, 16897, 5.6e-05), alg_cluster.Cluster(set(['24033']), 870.786325575, 261.829970016, 801515, 6.4e-05), alg_cluster.Cluster(set(['24005']), 871.921241442, 246.932531615, 754292, 6.1e-05), alg_cluster.Cluster(set(['24510']), 872.946822486, 249.834427518, 651154, 7.4e-05), alg_cluster.Cluster(set(['42101']), 894.72914873, 227.900547575, 1517550, 5.8e-05), alg_cluster.Cluster(set(['34007']), 899.061431482, 232.054232622, 508932, 5.7e-05), alg_cluster.Cluster(set(['34031']), 904.161746346, 201.712206531, 489049, 6.3e-05), alg_cluster.Cluster(set(['34023']), 904.976453741, 215.001458637, 750162, 5.9e-05), alg_cluster.Cluster(set(['34039']), 905.587082153, 210.045085725, 522541, 7.3e-05), alg_cluster.Cluster(set(['34013']), 906.236730753, 206.977429459, 793633, 7.1e-05), alg_cluster.Cluster(set(['34003']), 907.896066895, 202.302470427, 884118, 6.9e-05), alg_cluster.Cluster(set(['36085']), 908.749199508, 211.307161341, 443728, 7e-05), alg_cluster.Cluster(set(['34017']), 909.08042421, 207.462937763, 608975, 9.1e-05), alg_cluster.Cluster(set(['36061']), 911.072622034, 205.783086757, 1537195, 0.00015), alg_cluster.Cluster(set(['36047']), 911.595580089, 208.928374072, 2465326, 9.8e-05), alg_cluster.Cluster(set(['36119']), 912.141547823, 196.592589736, 923459, 6.5e-05), alg_cluster.Cluster(set(['36005']), 912.315497328, 203.674106811, 1332650, 0.00011), alg_cluster.Cluster(set(['36081']), 913.462051588, 207.615750359, 2229379, 8.9e-05), alg_cluster.Cluster(set(['36059']), 917.384980291, 205.43647538, 1334544, 7.6e-05), alg_cluster.Cluster(set(['09003']), 925.917212741, 177.152290276, 857183, 5.7e-05), alg_cluster.Cluster(set(['36103']), 929.241649488, 199.278463003, 1419369, 6.3e-05), alg_cluster.Cluster(set(['25017']), 943.405755498, 156.504310828, 1465396, 5.6e-05), alg_cluster.Cluster(set(['25025']), 950.299079197, 158.007070966, 689807, 7e-05)])


# In[7]:


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
                


# In[8]:


#closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0) 


# In[9]:


def hierarchical_clustering(cluster_list, num_clusters):
    length = len(cluster_list)
    while length > num_clusters:
        distance, idx_i, idx_j = fast_closest_pair(cluster_list)
        if idx_i >=0 and idx_j >= 0:
            pair = cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
            f_remove = cluster_list[idx_i]
            s_remove = cluster_list[idx_j]
            cluster_list.append(pair)           
            cluster_list.remove(f_remove)
            cluster_list.remove(s_remove)
        length = len(cluster_list)
    
    return cluster_list    
    
        


# In[10]:


#hierarchical_clustering([alg_cluster.Cluster(set(['123']), 1.0, 0.0, 1, 0), alg_cluster.Cluster(set(['124']), 4.0, 0.0, 1, 0), alg_cluster.Cluster(set(['334']), 5.0, 0.0, 1, 0), alg_cluster.Cluster(set(['443']), 7.0, 0.0, 1, 0)], 2)


# In[11]:


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    cluster_list = list(cluster_list)
    length = len(cluster_list)
    center = []
    cluster_list.sort(key = lambda cluster:cluster.total_population())
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
                
        


# In[12]:


# kmeans_clustering([alg_cluster.Cluster(set(['123']), 1.0, 0.0, 1, 0), alg_cluster.Cluster(set(['124']), 4.0, 0.0, 1, 0), alg_cluster.Cluster(set(['334']), 5.0, 0.0, 1, 0), alg_cluster.Cluster(set(['443']), 7.0, 0.0, 1, 0)], 2,1)
#
#
# # In[13]:
#
#
# import random
# import urllib.request
# import poc_simpletest      # http://www.codeskulptor.org/#poc_simpletest.py
# import alg_cluster
# DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
# DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
# DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
# DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
# DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
# DATA_24_URL = DIRECTORY + "data_clustering/unifiedCancerData_24.csv"
#
#
# def load_data_table(data_url):
#     """
#     Import a table of county-based cancer risk data
#     from a csv format file
#     """
#     data_file = urllib.request.urlopen(data_url)
#     data = data_file.read()
#     data_lines = data.decode().split('\n')
#     print("Loaded", len(data_lines), "data points")
#     data_tokens = [line.split(',') for line in data_lines]
#     return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
#             for tokens in data_tokens]
# #
#
#
# #########################################################################
# # Helper function for converting list of clusters to set of county tuples
#
# def set_of_county_tuples(cluster_list):
#     """
#     Input: A list of Cluster objects
#     Output: Set of sorted tuple of counties corresponds to counties in each cluster
#     """
#     set_of_clusters = set([])
#     for cluster in cluster_list:
#         counties_in_cluster = cluster.fips_codes()
#
#         # convert to immutable representation before adding to set
#         county_tuple = tuple(sorted(list(counties_in_cluster)))
#         set_of_clusters.add(county_tuple)
#     return set_of_clusters
#
#
# #############################################################################
# # Testing code
#
# def test_hierarchical24():
#     """
#     Test for hierarchical clustering
#     Note that hierarchical_clustering mutates cluster_list
#     """
#
#     # load small data table
#     print
#     print("Testing hierarchical_clustering on 24 county set")
#     data_24_table = load_data_table(DATA_24_URL)
#
#     # test data of the form [size of output cluster, sets of county tuples]
#     hierdata_24 = [[23, set([('11001', '51013'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34013',), ('34039',), ('34017',), ('36061',), ('36005',), ('36047',), ('36059',), ('36081',), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [22, set([('11001', '51013'), ('36047', '36081'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34013',), ('34039',), ('34017',), ('36061',), ('36005',), ('36059',), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [21, set([('11001', '51013'), ('36005', '36061'), ('36047', '36081'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34013',), ('34039',), ('34017',), ('36059',), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [20, set([('11001', '51013'), ('36005', '36061'), ('36047', '36081'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34039',), ('34013', '34017'), ('36059',), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [19, set([('34013', '34017', '34039'), ('11001', '51013'), ('36005', '36061'), ('36047', '36081'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('36059',), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [18, set([('34013', '34017', '34039'), ('11001', '51013'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('36059',), ('36005', '36047', '36061', '36081'), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [17, set([('11001', '51013'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('36059',), ('34013', '34017', '34039', '36005', '36047', '36061', '36081'), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [16, set([('11001', '51013'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051',), ('41067',), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [15, set([('11001', '51013'), ('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('24510',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('51840',), ('51760',), ('55079',), ('54009',)])],
#                    [14, set([('01073',), ('06059',), ('06037',), ('06029',), ('06071',), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('51840',), ('51760',), ('55079',), ('54009',), ('11001', '24510', '51013')])],
#                    [13, set([('06037', '06059'), ('01073',), ('06029',), ('06071',), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('51840',), ('51760',), ('55079',), ('54009',), ('11001', '24510', '51013')])],
#                    [12, set([('06037', '06059'), ('01073',), ('06029',), ('06071',), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('51760',), ('55079',), ('54009',), ('11001', '24510', '51013', '51840')])],
#                    [11, set([('06029', '06037', '06059'), ('01073',), ('06071',), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('51760',), ('55079',), ('54009',), ('11001', '24510', '51013', '51840')])],
#                    [10, set([('06029', '06037', '06059'), ('01073',), ('06071',), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('55079',), ('54009',), ('11001', '24510', '51013', '51760', '51840')])],
#                    [9, set([('01073',), ('06029', '06037', '06059', '06071'), ('06075',), ('08031',), ('34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081'), ('41051', '41067'), ('55079',), ('54009',), ('11001', '24510', '51013', '51760', '51840')])],
#                    [8, set([('01073',), ('06029', '06037', '06059', '06071'), ('06075',), ('08031',), ('41051', '41067'), ('55079',), ('54009',), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840')])],
#                    [7, set([('01073',), ('06029', '06037', '06059', '06071'), ('06075',), ('08031',), ('41051', '41067'), ('55079',), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009')])],
#                    [6, set([('06029', '06037', '06059', '06071', '06075'), ('01073',), ('08031',), ('41051', '41067'), ('55079',), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009')])],
#                    [5, set([('06029', '06037', '06059', '06071', '06075'), ('08031',), ('41051', '41067'), ('01073', '55079'), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009')])],
#                    [4, set([('06029', '06037', '06059', '06071', '06075'), ('01073', '11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009', '55079'), ('08031',), ('41051', '41067')])],
#                    [3, set([('06029', '06037', '06059', '06071', '06075', '41051', '41067'), ('01073', '11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009', '55079'), ('08031',)])],
#                    [2, set([('01073', '11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009', '55079'), ('06029', '06037', '06059', '06071', '06075', '08031', '41051', '41067')])],
#                    ]
#
#
#     suite = poc_simpletest.TestSuite()
#
#     for num_clusters, expected_county_tuple in hierdata_24:
#
#         # build initial list of clusters for each test since mutation is allowed
#         cluster_list = []
#         for idx in range(len(data_24_table)):
#             line = data_24_table[idx]
#             cluster_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
#
#         # compute student answer
#         student_clustering = hierarchical_clustering(cluster_list, num_clusters)
#         student_county_tuple = set_of_county_tuples(student_clustering)
#
#         # Prepare test
#         error_message = "Testing hierarchical_clustering on 24 county table, num_clusters = " + str(num_clusters)
#         error_message += "\nStudent county tuples: " + str(student_county_tuple)
#         error_message += "\nExpected county tuples: " + str(expected_county_tuple)
#         suite.run_test(student_county_tuple == expected_county_tuple, True, error_message)
#
#     suite.report_results()
#
# #test_hierarchical24()
#
#
#
# def test_kmeans():
#     """
#     Test for k-means clustering
#     kmeans_clustering should not mutate cluster_list, but make a new copy of each test anyways
#     """
#
#     # load small data table
#     print
#     print ("Testing kmeans_clustering on 24 county set")
#     data_24_table = load_data_table(DATA_24_URL)
#
#     kmeansdata_24 = [[15, 1, set([('34017', '36061'), ('06037',), ('06059',), ('36047',), ('36081',), ('06071', '08031'), ('36059',), ('36005',), ('55079',), ('34013', '34039'), ('06075',), ('01073',), ('06029',), ('41051', '41067'), ('11001', '24510', '51013', '51760', '51840', '54009')])],
#                      [15, 3, set([('34017', '36061'), ('06037', '06059'), ('06071',), ('36047',), ('36081',), ('08031',), ('36059',), ('36005',), ('55079',), ('34013', '34039'), ('06075',), ('01073',), ('06029',), ('41051', '41067'), ('11001', '24510', '51013', '51760', '51840', '54009')])],
#                      [15, 5, set([('34017', '36061'), ('06037', '06059'), ('06071',), ('36047',), ('36081',), ('08031',), ('36059',), ('36005',), ('55079',), ('34013', '34039'), ('06075',), ('01073',), ('06029',), ('41051', '41067'), ('11001', '24510', '51013', '51760', '51840', '54009')])],
#                      [10, 1, set([('34017', '36061'), ('06029', '06037', '06075'), ('11001', '24510', '34013', '34039', '51013', '51760', '51840', '54009'), ('06059',), ('36047',), ('36081',), ('06071', '08031', '41051', '41067'), ('36059',), ('36005',), ('01073', '55079')])],
#                      [10, 3, set([('34013', '34017', '36061'), ('06029', '06037', '06075'), ('08031', '41051', '41067'), ('06059', '06071'), ('34039', '36047'), ('36081',), ('36059',), ('36005',), ('01073', '55079'), ('11001', '24510', '51013', '51760', '51840', '54009')])],
#                      [10, 5, set([('34013', '34017', '36061'), ('06029', '06037', '06075'), ('08031', '41051', '41067'), ('06059', '06071'), ('34039', '36047'), ('36081',), ('36059',), ('36005',), ('01073', '55079'), ('11001', '24510', '51013', '51760', '51840', '54009')])],
#                      [5, 1, set([('06029', '06037', '06075'), ('01073', '11001', '24510', '34013', '34017', '34039', '36047', '51013', '51760', '51840', '54009', '55079'), ('06059',), ('36005', '36059', '36061', '36081'), ('06071', '08031', '41051', '41067')])],
#                      [5, 3, set([('06029', '06037', '06075'), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013'), ('08031', '41051', '41067'), ('06059', '06071'), ('01073', '51760', '51840', '54009', '55079')])],
#                      [5, 5, set([('06029', '06037', '06075'), ('08031', '41051', '41067'), ('06059', '06071'), ('01073', '55079'), ('11001', '24510', '34013', '34017', '34039', '36005', '36047', '36059', '36061', '36081', '51013', '51760', '51840', '54009')])]]
#
#     suite = poc_simpletest.TestSuite()
#
#     for num_clusters, num_iterations, expected_county_tuple in kmeansdata_24:
#
#         # build initial list of clusters for each test since mutation is allowed
#         cluster_list = []
#         for idx in range(len(data_24_table)):
#             line = data_24_table[idx]
#             cluster_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
#
#         # compute student answer
#         student_clustering = kmeans_clustering(cluster_list, num_clusters, num_iterations)
#         student_county_tuple = set_of_county_tuples(student_clustering)
#
#         # Prepare test
#         error_message = "Testing kmeans_custering on 24 county table, num_clusters = " + str(num_clusters)
#         error_message += " num_iterations = " + str(num_iterations)
#         error_message += "\nStudent county tuples: " + str(student_county_tuple)
#         error_message += "\nExpected county tuples: " + str(expected_county_tuple)
#         suite.run_test(student_county_tuple == expected_county_tuple, True, error_message)
#
#     suite.report_results()
#
# test_kmeans()
#


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




