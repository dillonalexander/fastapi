from fastapi import FastAPI

app = FastAPI()

class ViewerCounter:
    def __init__(self):
        self.total_viewers = 0
    def increment(self):
        self.total_viewers += 1
        return self.total_viewers
    
viewer_counter = ViewerCounter()

@app.get("/")
async def health_check():
    return "The health check is successful!"


@app.get("/hello")
async def hello_creator():
    viewers_count = viewer_counter.increment()
    return f"Hey, you are viewer number {viewers_count}!"

@app.get("/new-feature")
async def new_feature_test():
    list_test = []
    for n in range(10000):
        list_test.append(n)
    return list_test
