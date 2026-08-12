# Install Jenkins via Docker on Amazon Linux 2023

This guide installs Docker on the EC2 host and runs Jenkins inside an official LTS container. This shows how quickly you can get Jenkins running without a native package install.

> **Prerequisite:** Complete [EC2 setup](00-prerequisites.md) first.

> **Note:** If you already installed Jenkins natively, stop it first to free port 8080:
> `sudo systemctl stop jenkins && sudo systemctl disable jenkins`

## 1. Update the system

```bash
sudo dnf update -y
```

## 2. Install Docker

```bash
sudo dnf install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
```

## 3. Allow your user to run Docker

```bash
sudo usermod -aG docker ec2-user
```

Log out and SSH back in for the group change to take effect:

```bash
exit
# then reconnect:
ssh -i <key.pem> ec2-user@<EC2_PUBLIC_IP>
```

Verify Docker works without sudo:

```bash
docker run hello-world
```

## 4. Install Python 3 on the host

Workshop builds run Python on the **host**, not inside the Jenkins container. Install it now:

```bash
sudo dnf install -y python3 python3-pip
python3 --version
```

Pipeline `sh` steps will call `/usr/bin/python3` explicitly so builds use the host interpreter.

## 5. Run Jenkins in Docker

Create a persistent volume and start the Jenkins LTS container:

```bash
docker volume create jenkins_home

docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /usr/bin/python3:/usr/bin/python3:ro \
  -v /usr/bin/pip3:/usr/bin/pip3:ro \
  jenkins/jenkins:lts
```

The read-only volume mounts expose the host's Python and pip to the container.

Check that the container is running:

```bash
docker ps
```

## 6. Unlock Jenkins

1. Open `http://<EC2_PUBLIC_IP>:8080` in your browser.
2. Get the initial admin password from the container logs:

```bash
docker logs jenkins 2>&1 | grep -A2 "Please use the following password"
```

Or read it from the volume:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

3. Paste the password into the unlock screen and click **Continue**.

## 7. Complete the setup wizard

1. Click **Install suggested plugins** and wait for installation to finish.
2. Create your admin user.
3. Confirm the Jenkins URL is `http://<EC2_PUBLIC_IP>:8080`.
4. Click **Save and Finish**, then **Start using Jenkins**.

## 8. Verify Python from a Jenkins build

1. Create a Freestyle job named `python-test`.
2. Add an **Execute shell** build step:

```bash
/usr/bin/python3 --version
/usr/bin/pip3 --version
```

3. Build and check **Console Output** for version strings.

## Managing the Jenkins container

| Task | Command |
|------|---------|
| Stop Jenkins | `docker stop jenkins` |
| Start Jenkins | `docker start jenkins` |
| View logs | `docker logs -f jenkins` |
| Restart Jenkins | `docker restart jenkins` |

Jenkins data persists in the `jenkins_home` Docker volume across container restarts.

## Native vs Docker

| | Native install | Docker |
|---|----------------|--------|
| Install time | Moderate (Java + repo + package) | Fast (pull image + run) |
| Persistence | `/var/lib/jenkins` on disk | Docker volume `jenkins_home` |
| Upgrades | `sudo dnf update jenkins` | Pull new image, recreate container |
| Python for builds | Installed on host | Installed on host, mounted into container |
| Best for | Production-like, long-running servers | Quick setup, easy teardown, workshops |

## Troubleshooting

**Port 8080 already in use:** Another process (e.g. native Jenkins) is using the port. Stop it or pick a different host port: `-p 9090:8080`.

**Python not found in pipeline:** Use the absolute path `/usr/bin/python3` in `sh` steps, as shown in the demo Jenkinsfiles.

**Permission denied on Docker socket:** Make sure you logged out and back in after `usermod -aG docker`.

## Next step

[Connect Jenkins to GitHub](03-connect-github.md) and run your first job from this repository.
