# self-healing-container-platform
* This project is a replica of a real production my goal is to heal the containers, and check for GPU usage

* Local production enviroment is Ubuntu

* As someone who hopes to be a DevOps engineer one day, my idea was to implement a self-healing system

* As for the app, i will create an Python notes API with Postgres. The focus is on the infrastructure

* How it heals:
  - Kubernetes restarts crashed pods and replaces unhealthy ones (probes)
  - The autoscaler adds pods under load
  - Argo CD reverts manual changes back to what's in Git
  - Rollbacks are a git revert, not manual fixes
  - Monitoring and alerts catch what auto-healing can't


**Network drills:**
  - I checked behind my script to make sure the URLS returned 000 and an exit code 1
  - I scheduled a cron job that fetches the network/URLS status

**Phase 1 complete**

**Phase 2 started**

* Phase 2 is where i containerize the app

* I chose to run fastapi and postgres with docker compose

**Run:**
  - cp .env.example to .env, don't forget to change the password
  - use docker compose up -d
  - call it using curl localhost:your_port/health, /ready and also /notes

* It's built to be ran by non root users and also comes with a healthcheck

* /health is to know the app is functioning

* /ready is connection to the db or it'll return a 503 error

**Phase 2 complete**

**Phase 3 started**
