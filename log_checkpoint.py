from datetime import datetime


def custom_log_checkpoint(custom_path, custom_str):
    timestr = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    logdir_prefix = "{}_{}".format(custom_str, timestr)

    return logdir_prefix