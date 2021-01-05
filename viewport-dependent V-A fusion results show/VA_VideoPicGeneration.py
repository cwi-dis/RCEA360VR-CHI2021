# this script is used to
# 1) Plot heatmap for clustered viewport each segment
# (20200920 created by Tong Xue)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# plot viewport data by video and segment
def Plot_ViewPort_HeatmapByVideo(_data):
    sample_number = 1000
    m_participantEyeGazeDataArr = np.zeros((8, 3, sample_number, 60), dtype=np.float64)
    m_participantEyeGazeDataArr[:] = np.nan

    # get eye gaze data list
    for _vid in range(0, 1):
        for _seg in range(0, 60):

            m_pitchData = _data['pitch'][_vid][_seg]
            m_yawData = _data['yaw'][_vid][_seg]

            for _sample in range(len(m_pitchData)):
                m_participantEyeGazeDataArr[_vid, 0, _sample, _seg] = m_pitchData[_sample][0]
                m_participantEyeGazeDataArr[_vid, 1, _sample, _seg] = m_yawData[_sample][0]
                m_participantEyeGazeDataArr[_vid, 2, _sample, _seg] = _seg + 1

    V = np.load("../source/fusion_result.npz")["valence"]
    A = np.load("../source/fusion_result.npz")["arousal"]

    for _vid in range(0, 1):

        for _seg in range(0, 60):

            m_yawValueList = []
            m_pitchValueList = []
            try:
                for _sample in range(0, sample_number):

                    _pitchValue = m_participantEyeGazeDataArr[_vid, 0, _sample, _seg]
                    _yawValue = m_participantEyeGazeDataArr[_vid, 1, _sample, _seg]
                    if np.isnan(_pitchValue) or np.isnan(_yawValue):
                        None
                    else:
                        m_pitchValueList.append(_pitchValue)
                        m_yawValueList.append(_yawValue)
            except IndexError:
                None

            _heatmap, xedges, yedges = np.histogram2d(m_yawValueList, m_pitchValueList, bins=20,
                                                      range=[[-180, 180], [-90, 90]])
            # Modify axis ticks depending on definition of pitch and yaw

            extent = [xedges[0], xedges[-1], yedges[-1], yedges[0]]

            x_min = 20
            x_max = 0
            y_min = 20
            y_max = 0
            for _row in range(20):
                _temp = np.arange(len(_heatmap.T[_row]))
                _tempList = _temp[_heatmap.T[_row] > 30]
                if len(_tempList):
                    if np.min(_tempList) < x_min:
                        x_min = np.min(_tempList)
                    if np.max(_tempList) > x_max:
                        x_max = np.max(_tempList)
            for _col in range(20):
                _temp = np.arange(len(_heatmap.T[:, _col]))
                _tempList = _temp[_heatmap.T[:, _col] > 20]
                if len(_tempList):
                    if np.min(_tempList) < y_min:
                        y_min = np.min(_tempList)
                    if np.max(_tempList) > y_max:
                        y_max = np.max(_tempList)
            x_min = x_min * 18 - 180
            x_max = (x_max + 1) * 18 - 180
            y_min = 90 - y_min * 9
            y_max = 90 - (y_max + 1) * 9
            showText = 'V=' + str(round(V[_vid][_seg], 2)) + ', A=' + str(round(A[_vid][_seg], 2))

            for i in range(1, 31):
                plt.close("all")
                plt.tight_layout()
                plt.figure(figsize=(6.4, 3.6), dpi=300)

                _thumbNailImg = plt.imread("../V" + str(_vid + 1) + "_FramePic/%s.jpg" % str(_seg*25+i))

                plt.axis('off')
                plt.imshow(_thumbNailImg, extent=extent)
                plt.imshow(_heatmap.T, extent=extent, origin='lower', alpha=.5, interpolation='bilinear')

                currentAxis = plt.gca()
                rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, linewidth=1, edgecolor='yellow',
                                         facecolor='none')
                currentAxis.add_patch(rect)

                plt.text(x_min, y_min + 10, showText, fontdict={'size': 8, 'color': 'yellow'})
                plt.savefig("../V" + str(_vid + 1) + "_HeatmapPic/Viewport_%s.png" % str(_seg*25+i))


data = np.load('clustering_result.npz', allow_pickle=True, encoding='latin1')
Plot_ViewPort_HeatmapByVideo(data)
