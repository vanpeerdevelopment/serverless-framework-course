import time

def hello(event, context):
    print("Hi!")
    time.sleep(4)
    return "hello-world"
