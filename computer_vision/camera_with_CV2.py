import mujoco as mj
import mujoco.viewer as mjv
import cv2
import numpy as np

model = mj.MjModel.from_xml_path('block_with_camera.xml')
data = mj.MjData(model)
cam_id = model.camera("robot_camera").id
renderer = mj.Renderer(model, height=480, width=640)

while True:
    # Step simulation
    mj.mj_step(model, data)

    # Render from the specified camera
    renderer.update_scene(data, camera=cam_id)
    image = renderer.render()

    # Convert RGB to BGR for OpenCV
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Show the image
    cv2.imshow("MuJoCo Camera View", image_bgr)

    # Exit on keypress
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

###Currently not working due to an issue on macOS with cv2.imshow and something with the main thread idk.