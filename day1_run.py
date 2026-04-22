import mujoco
import mujoco.viewer
import numpy as np

model = mujoco.MjModel.from_xml_path('day1_robot.xml')
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        # 1. READ OBSERVATIONS (Day 11)
        hand_pos = data.site('pinch_point').xpos
        eraser_pos = data.body('eraser').xpos
        
        # 2. CALCULATE DISTANCE (Day 12 Reward Logic)
        dist = np.linalg.norm(hand_pos - eraser_pos)
        
        # 3. APPLY CONTROL
        # Logic: If far, stay open. If close, pinch!
        mujoco.mj_step(model, data)
        viewer.sync()