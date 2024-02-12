# to select the folder/file path depending on the development environment(Win/Mac)

import os
import platform


def select_path(env_name):

    current_path = os.getcwd()
    os_name = platform.system()
    # depending on the environment, algorithm, OS(Win/Mac)

    tmp_path = "trained_agent" + "/" + env_name
    print(tmp_path)

    if os_name == "Windows":
        current_path = current_path.replace("pythonProject", "")
        current_path = current_path.replace("\\", "/")
        checkpoint_path = current_path + tmp_path
    else:
        current_path = current_path.replace("practice_ray", "")
        current_path = current_path.replace("\\", "/")

        checkpoint_path = current_path + tmp_path

    return checkpoint_path
