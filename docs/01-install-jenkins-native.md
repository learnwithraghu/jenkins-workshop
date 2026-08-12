# Install Jenkins (Native) on Amazon Linux 2023

This guide installs Jenkins directly on the EC2 host as a systemd service. Use this path if you want a traditional, persistent Jenkins installation.

> **Prerequisite:** Complete [EC2 setup](00-prerequisites.md) first.

## 1. Update the system

```bash
sudo dnf update -y
```

## 2. Install Java 17

Jenkins requires Java. Amazon Corretto 17 is the recommended choice on AL2023:

```bash
sudo dnf install -y java-17-amazon-corretto
java -version
```

You should see output mentioning `openjdk version "17"`.

## 3. Add the Jenkins repository

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
  https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
```

## 4. Install Jenkins

```bash
sudo dnf install -y jenkins
```

## 5. Start and enable Jenkins

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

The status should show `active (running)`.

## 6. Unlock Jenkins

1. Open `http://<EC2_PUBLIC_IP>:8080` in your browser.
2. Retrieve the initial admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

3. Paste the password into the unlock screen and click **Continue**.

## 7. Complete the setup wizard

1. Click **Install suggested plugins** and wait for installation to finish.
2. Create your admin user (username, password, full name, email).
3. On the instance configuration page, confirm the Jenkins URL is `http://<EC2_PUBLIC_IP>:8080`.
4. Click **Save and Finish**, then **Start using Jenkins**.

## 8. Install Python 3 for workshop builds

The workshop demos run simple Python scripts on the Jenkins host:

```bash
sudo dnf install -y python3 python3-pip
python3 --version
pip3 --version
```

## 9. Verify Jenkins can run Python

Create a quick test to confirm the Jenkins user can execute Python:

1. In Jenkins, click **New Item** → name it `python-test` → select **Freestyle project** → **OK**.
2. Under **Build Steps**, add **Execute shell**:

```bash
python3 --version
pip3 --version
```

3. Click **Save**, then **Build Now**.
4. Open the build → **Console Output**. You should see Python and pip version strings.

You can delete the `python-test` job after verifying.

## When to use native install

| Advantage | Description |
|-----------|-------------|
| Persistent service | Jenkins survives reboots via systemd |
| Familiar ops model | Standard package install, logs via `journalctl -u jenkins` |
| Direct host access | Python and tools installed directly on the OS |

## Troubleshooting

**Port 8080 not reachable:** Check your EC2 security group allows inbound TCP on port 8080.

**Jenkins won't start:** Check logs with:

```bash
sudo journalctl -u jenkins -e
```

**Permission denied running builds:** Jenkins runs as the `jenkins` user. Host-installed `python3` at `/usr/bin/python3` is accessible to all users by default.

## Next step

[Connect Jenkins to GitHub](03-connect-github.md) and run your first job from this repository.
