* Typo in requirements.txt broke the build, found by reading pip’s error

* Compose file was named docker-composer.yml, so Compose couldn’t find it

* Port 8000 was taken by an earlier test container, found with docker ps

* Containers ran but weren’t reachable because the port mapping was missing, fixed with down / up -d
