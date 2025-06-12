import mujoco as mj
import mujoco.viewer as mjv
import cv2
import numpy as np
import time

model = mj.MjModel.from_xml_path('block_with_camera.xml')
data = mj.MjData(model)

with mjv.launch_passive(model, data) as viewer:
    viewer.cam.type = mj.mjtCamera.mjCAMERA_FIXED
    viewer.cam.fixedcamid = model.camera("robot_camera").id
    time.sleep(10)