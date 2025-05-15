import numpy as np
from legged_gym.utils.third_party.amp_utils import AMP_UTILS_DIR

VISUALIZE_RETARGETING = True

URDF_FILENAME = f"{AMP_UTILS_DIR}/models/h1/h1_custom_collision.urdf"
OUTPUT_DIR = f"{AMP_UTILS_DIR}/motion_files/mocap_motions_h1/"

REF_POS_SCALE = 1.4 # 缩放系数,如果遇到关节限位异常，尝试将此数变小
INIT_POS = np.array([0, 0, 1.5]) # h1
# INIT_ROT = np.array([0, 0, 0, 1.0])
INIT_ROT = np.array([0, 0.70710678, 0, 0.70710678])

SIM_TOE_JOINT_IDS = [25, 32, 8, 17]
SIM_HIP_JOINT_IDS = [19, 26, 0, 9]
# SIM_TOE_JOINT_IDS = [32, 25, 17, 8]
# SIM_HIP_JOINT_IDS = [26, 19, 9, 0]
SIM_ROOT_OFFSET = np.array([0, 0, 0.2])
SIM_TOE_OFFSET_LOCAL = [
    np.array([0.0, 0.08, 0.2]),
    np.array([0.0, -0.08, 0.2]),
    np.array([0.08, 0.08, -0.2]),
    np.array([0.08, -0.08, -0.2])
]
TOE_HEIGHT_OFFSET = 0.15

DEFAULT_JOINT_POSE = np.array([0., 0., -0.4, 
                               0.8, -0.1, 
                               0., 0., -0.4, 
                               0.8, -0.1, 
                               0.0, 
                               0., 0., 0., 0.,
                               0., 0., 0., 0.])
JOINT_DAMPING = [0.01, 0.01, 0.01,
                 0.01, 0.01, 0.01,
                 0.01, 0.01, 0.01,
                 0.01, 0.01, 0.01,
                 0.01, 0.01, 0.01,
                 0.01, 0.01, 0.01, 0.01]

FORWARD_DIR_OFFSET = np.array([0, 0, 0])

FR_FOOT_NAME = "right_elbow_link"
FL_FOOT_NAME = "left_elbow_link"
HR_FOOT_NAME = "right_ankle_link"
HL_FOOT_NAME = "left_ankle_link"
TORSO_NAME = "torso_link"

MOCAP_MOTIONS = [
    # Output motion name, input file, frame start, frame end, motion weight.
    ["pace0", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk00_joint_pos.txt", 162, 201, 1],
    ["pace1", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk00_joint_pos.txt", 201, 400, 1],
    # ["pace2", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk00_joint_pos.txt", 400, 600, 1],
    # ["trot0", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk03_joint_pos.txt", 448, 481, 1],
    # ["trot1", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk03_joint_pos.txt", 400, 600, 1],
    # ["trot2", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_run04_joint_pos.txt", 480, 663, 1],
    # ["canter0", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_run00_joint_pos.txt", 430, 480, 1],
    # ["canter1", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_run00_joint_pos.txt", 380, 430, 1],
    # ["canter2", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_run00_joint_pos.txt", 480, 566, 1],
    ["right_turn0", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk09_joint_pos.txt", 1085, 1124, 1.5],
    ["right_turn1", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk09_joint_pos.txt", 560, 670, 1.5],
    ["left_turn0", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk09_joint_pos.txt", 2404, 2450, 1.5],
    ["left_turn1", f"{AMP_UTILS_DIR}/datasets/keypoint_datasets/ai4animation/dog_walk09_joint_pos.txt", 120, 220, 1.5]
]
