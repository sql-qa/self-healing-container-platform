# self-healing-container-platform
* This project is a replica of a real production. My goal is to heal the containers, and check for CPU/GPU usage.

* Local production enviroment is Ubuntu.

* As someone who hopes to be a DevOps engineer one day, my idea was to implement a self-healing system.

* As for the app, i will create an Python notes API with Postgres. The focus is on the infrastructure.

* How it heals:
               Kubernetes restarts crashed pods and replaces unhealthy ones (probes)
               The autoscaler adds pods under load
               Argo CD reverts manual changes back to what’s in Git
               Rollbacks are a git revert, not manual fixes
               Monitoring and alerts catch what auto-healing can’t
