import os
import tempfile
from datetime import datetime
from ray.tune.logger import UnifiedLogger

'''
to create a folder path for the training result and the policy
for the training result, it's working
for the policy, it's not implemented yet
'''
def custom_log_creator(custom_path, custom_str):
    timestr = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    logdir_prefix = "{}_{}".format(custom_str, timestr)

    def logger_creator(config):
        logdir = tempfile.mkdtemp(prefix=logdir_prefix, dir=custom_path)
        if not os.path.exists(custom_path):
            os.makedirs(custom_path)
        return UnifiedLogger(config, logdir, loggers=None)

    return logger_creator
