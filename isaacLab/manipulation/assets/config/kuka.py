# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Kinova Robotics arms.

The following configuration parameters are available:

* :obj:`KINOVA_JACO2_N7S300_CFG`: The Kinova JACO2 (7-Dof) arm with a 3-finger gripper.
* :obj:`KINOVA_JACO2_N6S300_CFG`: The Kinova JACO2 (6-Dof) arm with a 3-finger gripper.
* :obj:`KINOVA_GEN3_N7_CFG`: The Kinova Gen3 (7-Dof) arm with no gripper.

Reference: https://github.com/Kinovarobotics/kinova-ros
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
usd_dir_path = os.path.join(BASE_DIR, "../usd/")

robot_usd = "iiwa7.usd"

##
# Configuration
##

KUKA_ROBOTIQ = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=usd_dir_path + robot_usd,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0,
            fix_root_link = True
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "A1": 0.0,
            "A2": -0.569,
            "A3": 0.0,
            "A4": -2.810,
            "A5": 0.0,
            "A6": 3.037,
            "A7": 0.741,
            "hande_joint_finger": 0.0,
            "robotiq_hande_base_to_hande_right_finger": 0.0,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["A[1-7]"],
            velocity_limit=100.0,
            effort_limit=100.0,
            stiffness=1000000.0,
            damping=40.0,
        ),
        "hand": ImplicitActuatorCfg(
            joint_names_expr=["hande_joint_finger","robotiq_hande_base_to_hande_right_finger"],
            effort_limit=150.0,
            velocity_limit=2.24,
            stiffness=5.0,
            damping=5.0,
        ),
    },
)

"""Configuration of robot with stiffer PD control."""
KUKA_HPD = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=usd_dir_path + robot_usd,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0,
            fix_root_link = True
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "A1": 0.0,
            "A2": -0.569,
            "A3": 0.0,
            "A4": -2.810,
            "A5": 0.0,
            "A6": 3.037,
            "A7": 0.741,
            "hande_joint_finger": 0.0,
            "robotiq_hande_base_to_hande_right_finger": 0.0,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["A[1-7]"],
            velocity_limit=2.0,
            effort_limit={
                "A[1-4]": 39.0,
                "A[5-7]": 9.0,
            },
            stiffness={
                "A[1-4]": 600.0,  #100
                "A[5-7]": 450.0,   # 15
            },
            damping={
                "A[1-4]": 30.0,    # 1.0
                "A[5-7]": 15.0,    #0.5
            },
        ),
        "hand": ImplicitActuatorCfg(
            joint_names_expr=["hande_joint_finger","robotiq_hande_base_to_hande_right_finger"],
            effort_limit=150.0,
            velocity_limit=2.24,
            stiffness=5.0,
            damping=5.0,
        ),
    },
)
