import json
from locust import HttpUser, task, between


class PerformanceTests(HttpUser):
   # wait_time = between(1, 3)

    @task(1)
    def testFastApi(self):
        sample = {
  "X": [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/api/v1/", data=json.dumps(sample), headers=headers)