# Prerequisites: EC2 Setup

Before installing Jenkins, launch an Amazon Linux 2023 EC2 instance and open the ports Jenkins needs.

## Launch an EC2 instance

1. Sign in to the [AWS Console](https://console.aws.amazon.com/) and open **EC2**.
2. Click **Launch instance**.
3. Configure the instance:

| Setting | Recommended value |
|---------|-------------------|
| Name | `jenkins-workshop` |
| AMI | Amazon Linux 2023 |
| Instance type | `t3.small` (2 vCPU, 2 GB RAM) |
| Key pair | Create or select an existing SSH key pair |
| Storage | 20 GB gp3 |

4. Under **Network settings**, create or select a security group with these inbound rules:

| Type | Port | Source | Purpose |
|------|------|--------|---------|
| SSH | 22 | Your IP | SSH access |
| Custom TCP | 8080 | Your IP (or `0.0.0.0/0` for a classroom) | Jenkins web UI |

5. Launch the instance and wait until the status is **Running**.

## Connect via SSH

Replace `<key.pem>` and `<EC2_PUBLIC_IP>` with your values:

```bash
ssh -i <key.pem> ec2-user@<EC2_PUBLIC_IP>
```

The default user on Amazon Linux 2023 is `ec2-user`.

## Optional: Elastic IP

If you stop and start your instance, the public IP may change. For a stable Jenkins URL during the workshop:

1. In EC2, go to **Elastic IPs** → **Allocate Elastic IP address**.
2. Select the new address → **Actions** → **Associate Elastic IP address** → choose your instance.

Use the Elastic IP everywhere this guide says `<EC2_PUBLIC_IP>`.

## What you need before continuing

- [ ] EC2 instance running Amazon Linux 2023
- [ ] SSH access working
- [ ] Port 8080 open in the security group
- [ ] Public IP (or Elastic IP) noted for later

## Next step

Choose one Jenkins installation path:

- [Install Jenkins natively](01-install-jenkins-native.md) — traditional RPM install, runs as a systemd service
- [Install Jenkins via Docker](02-install-docker-jenkins.md) — Docker on the host, Jenkins in a container

Both paths work for the rest of this workshop.
