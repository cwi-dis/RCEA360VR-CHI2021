## CHI 2021 paper: RCEA-360VR

Source code for our CHI 2021 paper:
>*RCEA-360VR: Real-time, Continuous Emotion Annotation in 360° VR Videos for Collecting Precise Viewport-dependent Ground Truth Labels*

Repository contains:

1. [Viewport-dependent annotation fusion method](source)
2. [Viewport-based fine-grained V-A video overlay generator + example videos](video_results)

Example results for our viewport-dependent label fusion method:
![Example viewport-dependent V-A overlay videos](video_results/video_examples/example_VD_labelled_vids.gif)

*[Explanation of source code will be finalized soon]*

## Preprint + Video Preview

Preprint (.pdf) here: [chi2021_rcea360VR_preprint](preprint/chi2021_rcea360VR_preprint.pdf)

30s video preview (on YouTube):

[![30s video preview](https://abdoelali.com/assets/rcea360vr_thumbnail.png)](https://www.youtube.com/watch?v=dSeCyH6OuIc "CHI 2021 RCEA-360VR")


## Citing this paper or code

**Please cite our paper in any published work that uses any of these resources.**

BiBTeX:
```
@inproceedings{Xue2021,
  title = {RCEA-360VR: Real-time, Continuous Emotion Annotation in 360° VR Videos for Collecting Precise Viewport-dependent Ground Truth Labels},
  author = {Tong Xue and Abdallah El Ali and Tianyi Zhang and Gangyi Ding and Pablo Cesar},
  booktitle = {Proceedings of the International Conference on Human Factors in Computing Systems 2021},
  series = {CHI '21},
  year = {2021},
  location = {Yokohama, Japan},
  pages = {1-15},
  keywords = {Emotion, annotation, 360°, virtual reality, ground truth, labels, viewport-dependent, real-time, continuous},
  url = {https://doi.org/10.1145/3411764.3445487},
  abstract = {Precise emotion ground truth labels for 360° virtual reality (VR) video watching are essential for fine-grained predictions under varying viewing behavior. However, current annotation techniques either rely on post-stimulus discrete self-reports, or real-time, continuous emotion annotations (RCEA) but only for desktop/mobile settings. We present RCEA for 360° VR videos (RCEA-360VR), where we evaluate in a controlled study (N=32) the usability of two peripheral visualization techniques: HaloLight and DotSize. We furthermore develop a method that considers head movements when fusing labels. Using physiological, behavioral, and subjective measures, we show that (1) both techniques do not increase users' workload, sickness, nor break presence (2) our continuous valence and arousal annotations are consistent with discrete within-VR and original stimuli ratings (3) users exhibit high similarity in viewing behavior, where fused ratings perfectly align with intended labels. Our work contributes usable and effective techniques for collecting fine-grained viewport-dependent emotion labels in 360° VR.},
  }
  ```

ACM Ref Citation:

*Tong Xue, Abdallah El Ali, Tianyi Zhang, Gangyi Ding, and Pablo Cesar (2021). RCEA-360VR: Real-time, Continuous Emotion Annotation in 360° VR Videos for Collecting Precise Viewport-dependent Ground Truth Labels. In CHI Conference on Human Factors in Computing Systems (CHI ’21), May 8–13, 2021, Yokohama, Japan. ACM, New York, NY, USA, 15 pages. https://doi.org/10.1145/3411764.3445487*


## Licenses

Code in this repo is released under [Mozilla Public
License 2.0](https://github.com/ayman/hubs-research-2021/blob/main/LICENSE).
