import numpy as np
from collections import Counter
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib import pyplot as plt


def hierarchy_clustering(samples, p, _vid, _segID):
    # p is the percentage of view points for the largest cluster
    Z = linkage(samples, 'ward')
    n = samples.shape[0]
    max_d = int(max(Z[:, 2]))
    min_d = int(min(Z[:, 2]))
    t = min_d
    c = 0

    plt.figure(figsize=(10, 6), dpi=80)
    plt.title('Hierarchy Cluster for V' +  str(_vid+1) + ' Seg' + str(_segID+1), fontsize=30)
    plt.xlabel('Cluster Size', fontsize=20)
    plt.ylabel('Distance', fontsize=20)
    plt.tick_params(labelsize=15)

    dendrogram(Z, truncate_mode='lastp', p=4, leaf_font_size=24., show_contracted=True)
    plt.tick_params(labelsize=24)
    plt.yticks(np.arange(0, 9, 2))
    plt.savefig('V' + str(_vid+1) + '_Seg' + str(_segID+1) + '.png')
    plt.close()

    while t <= max_d and c < p:
        clusters = fcluster(Z, t, criterion='distance')
        c = Counter(clusters).most_common(1)[0][1] / n
        t = t + 1
    return clusters, Counter(clusters).most_common(1)[0][0]
    # return the label of cluster and the cluster index of the largest cluster


def clustering_users(samples):
    data = samples.groupby("VID")
    cluster_videos = []
    for i in range(8):  # for 8 videos
        clustering_data = np.array(data.get_group(i + 1))
        cluster_video_1s = []
        for j in range(60):  # for 60s
            n = 30
            if i == 0: n = 25
            clustering_data_all = clustering_data[np.where((clustering_data[:, 2] >= (j * n + 1)) &
                                                           (clustering_data[:, 2] < ((j + 1) * n + 1)))]
            clustering_data_s = clustering_data_all[:, 5:8]
            # the index of the biggest cluster
            # clusters, c =kmeans_clustering(clustering_data_s,3)
            clusters, c = hierarchy_clustering(clustering_data_s, 0.8, i, j)
            fuse_data = clustering_data_all[np.where(clusters == c)]
            cluster_video_1s.append(fuse_data)
        cluster_videos.append(cluster_video_1s)
        print("Finish video %s" % (i + 1))
    return cluster_videos
