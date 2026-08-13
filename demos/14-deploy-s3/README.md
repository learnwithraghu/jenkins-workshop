# Demo 14: Deploy index.html to Amazon S3

## What this teaches

- A **Deploy** stage that uploads `index.html` to an S3 bucket in **us-east-1 (N. Virginia)**
- Passing **bucket name, Access Key, and Secret Key** with **Build with Parameters**
- Installing **AWS CLI v2** on the agent if it is missing
- Opening the site on the S3 static website endpoint

## Instructor talking points

1. **Everything for this run is typed at build time** — `S3_BUCKET`, `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY` are parameters. The Jenkinsfile never contains keys.
2. **`password` hides the secret in the form** — students still must not paste keys into Git or the Jenkinsfile. For a real team, prefer Jenkins Credentials or an EC2 instance role (demo 10).
3. **Region is Virginia** — `AWS_DEFAULT_REGION=us-east-1`. The workshop bucket must be created in **US East (N. Virginia)**.

## AWS setup (once)

Create the bucket in **US East (N. Virginia) / us-east-1**.

1. S3 → Create bucket → region **US East (N. Virginia)**.
2. Bucket → **Properties** → **Static website hosting** → Enable. Index document: `index.html`.
3. Allow public website reads (workshop-only). Turn off **Block public access** for this bucket if needed, then add a bucket policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

4. The IAM user whose keys you enter needs at least:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

Replace `YOUR_BUCKET_NAME` with the real bucket.

The **Install AWS CLI** stage installs AWS CLI v2 under `$HOME/.local` if `aws` is not already on the PATH. No `sudo` required.

## Jenkins job setup

Create the job first. You enter keys on the next step, after Jenkins has loaded the parameters.

| Setting | Value |
|---------|-------|
| Job name | `demo-14-deploy-s3` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/14-deploy-s3/Jenkinsfile` |

1. **New Item** → name `demo-14-deploy-s3` → **Pipeline**.
2. Set **Pipeline script from SCM** with the values above.
3. **Save**.
4. Click **Build Now** once so Jenkins reads the Jenkinsfile and registers the parameters. This first run is expected to fail if `S3_BUCKET` and the keys are still empty.

## Where to enter Access Key and Secret Key

After the job exists and the first **Build Now** has finished, use **Build with Parameters**. The keys are **not** stored in this repo.

1. Open `demo-14-deploy-s3`.
2. Click **Build with Parameters**.
3. Fill in:

| Parameter | What to enter |
|-----------|----------------|
| `S3_BUCKET` | Your bucket name (must exist in **us-east-1**) |
| `AWS_ACCESS_KEY_ID` | IAM Access Key ID (`AKIA...`) |
| `AWS_SECRET_ACCESS_KEY` | IAM Secret Access Key (password field) |

4. Click **Build**.

Jenkins masks password parameters in the UI. Do not `echo` them in the pipeline.

> **Safer for production:** **Manage Jenkins → Credentials** (Username with password) or an EC2 **instance IAM role**. Parameters are fine for a short workshop; they can still appear in build history on the controller.

## How to test

After a green Deploy stage, open:

```
http://<S3_BUCKET>.s3-website-us-east-1.amazonaws.com
```

You should see **Deployed to Amazon S3** and **Jenkins Workshop Site**.

## Expected console highlights

```
AWS CLI already installed
...
Wrote .../site/index.html
Uploaded s3://your-bucket/index.html
Open: http://your-bucket.s3-website-us-east-1.amazonaws.com
```

The Secret Key must **not** appear in the log.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Page template |
| `generate_site.py` | Writes `site/index.html` with bucket, build number, and time |
| `Jenkinsfile` | Generate → Install AWS CLI → Deploy (`aws s3 cp` to us-east-1) |

## Try it

Rebuild and refresh the S3 URL. The **Build number** on the page should match the Jenkins build.

## Next

Back to the [demos index](../README.md), or continue with any remaining challenges.
