import pyrealsense2 as rs
import numpy as np

# Initialize the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

pipeline.start(config)

try:
    while True:
        # Wait for a new frame
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()

        if not depth_frame:
            continue

        # Convert depth frame to a Numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Calculate the distance to the object in the center of the frame
        height, width = depth_image.shape
        center_x, center_y = width // 2, height // 2
        depth = depth_image[center_y, center_x]  # Depth in millimeters

        # Convert depth to meters
        depth_meters = depth / 1000.0

        # Calculate the size of the object
        # You may need to specify the size calculation based on your application

        # Print distance and size information
        print(f"Distance to object at center: {depth_meters} meters")

except KeyboardInterrupt:
    pass
finally:
    pipeline.stop()
