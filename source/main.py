import pandas as pd
import numpy as np
import VA_aligment
import VA_clusters
import VA_fusion

if __name__ == "__main__":
    samples = pd.read_csv("../data/VA_HM_FrameData.csv")
    samples_vf = pd.read_csv("../Video_VF_Data.csv")
    '''
    time aligment
    '''
    shift_v, shift_a = VA_aligment.annotation_alignment(samples, samples_vf)
    samples_shift = VA_aligment.alignment_users(samples, shift_v, shift_a)
    '''
    clustering
    '''
    cluster_videos = VA_clusters.clustering_users(samples_shift)
    '''
    annotation fusion
    '''
    valence, arousal = VA_fusion.annotation_fusion(cluster_videos)
    pitch, yaw, box = VA_fusion.bounding_box_fusion(cluster_videos)
    '''
    save data
    '''
    np.savez("../results/fusion_result.npz", valence=valence, arousal=arousal,
             pitch=pitch, yaw=yaw, box=box)
    np.savez("../results/shift.npz", shift_v=shift_v, shift_a=shift_a)
