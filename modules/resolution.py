STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def change_res(cam, res="720p"):
    dim = STD_DIMENSIONS[res]
    cam.set(3, dim[0])
    cam.set(4, dim[1])

