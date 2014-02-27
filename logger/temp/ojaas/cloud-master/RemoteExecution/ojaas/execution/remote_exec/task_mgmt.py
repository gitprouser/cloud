
class TaskMgmt:
    def __init__(self):
        raise RuntimeError("Not implemented yet")

    """
        Adding a task for execution in the VM.
            - read three args task_id, databag_dict and scriptlet
            - Create a directory structure under /u01/tasks/task_taskID
    """
    def add_task(self, task_1, task_2, task_3):
        raise RuntimeError("Not implemented yet")


    """ Execute task based on task_id """
    def execute_task(self, taskID):
        raise RuntimeError("Not implemented yet")

    """ Post the job task back to SM. """
    def post_task(self, taskID):
        raise RuntimeError("Not implemented yet")

    """ Delete the directories created for the job task"""
    def delete_task(self, taskId):
        raise RuntimeError("Not implemented yet")
