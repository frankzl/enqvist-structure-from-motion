# enqvist-structure-from-motion
Non-Sequential  structure from motion following the paper by [Enqvist et al](http://www1.maths.lth.se/matematiklth/vision/publdb/reports/pdf/enqvist-kahl-etal-wovcnnc-11.pdf)

## Pipeline Outline (taken from Enqvist et al)
1. Feature extraction using SIFT and matching between pairs of views
2. Estimation of relative orientation for pairs of views. (5-point solver used in RANSAC combination with bundle adjustment)
3. Detection and removal of large errors among relative rotations.
4. Estimation of camera orientation using remaining relative rotations.
5. 3D reconstruction using the estimated camera orientations.
6. Bundje Adjustment to improve the 3D reconstruction.
