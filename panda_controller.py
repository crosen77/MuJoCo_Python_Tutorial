import time
import mujoco as mj
import mujoco.viewer as mjv
import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

model = mj.MjModel.from_xml_path('mjx_single_cube.xml')
data = mj.MjData(model)

panda = rtb.models.ETS.Panda()
goalLocation = np.array([0.5, 0, 0.03])
goalPose = sm.SE3(goalLocation) * sm.SE3.Rx(np.pi)
q0 = panda.qr
qf = panda.ikine_LM(goalPose).q
traj = rtb.jtraj(q0, qf, 100)

with mjv.launch_passive(model, data) as viewer:
    
    for i in range(100):
        data.qpos[0:7] = traj.q[i]
        mj.mj_step(model, data)
        time.sleep(0.02)
        viewer.sync()
        if i == 0:
            time.sleep(5)
        if i == 99:
            time.sleep(2)