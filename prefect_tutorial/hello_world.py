"""
This is hello world tutorial of `prefect` library in python
for workflow management.
"""
from prefect import task, Flow


@task
def hello_world():
    """first task"""
    print("Hello World!")
    return "Hello Prefect!"

@task
def prefect_say(s: str):
    """second task."""
    print(s)


with Flow("My First Flow") as flow:
    r = hello_world()
    s2 = prefect_say(r)

flow.run()
# flow.visualize()
