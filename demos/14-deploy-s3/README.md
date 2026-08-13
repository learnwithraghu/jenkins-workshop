# Demo 14: Deploy index.html to Amazon S3

## What this teaches

- A **Deploy** stage that uploads `index.html` to an S3 bucket
- Passing the **bucket name** with **Build with Parameters** (`S3_BUCKET`)
- Storing AWS keys in the **Jenkins Credentials** store — never in Git or the Jenkinsfile
- Opening the site on the S3 static website endpoint

## Instructor talking points

1. **The bucket is an input, not a secret** — students type `S3_BUCKET` at build time; the same job can deploy to different workshop buckets.
2. **Keys live in Jenkins Credentials** — show **Manage Jenkins → Credentials**. The Jenkinsfile only has the ID `aws-s3-workshop`. Console output masks the secret.
3. **This is a real deploy** — after a green build, open the S3 website URL; change `SITE_TITLE` and rebuild to prove the pipeline updated the page.

## Where to store Access Key and Secret Key

**Do not** put keys in the Jenkinsfile, in this repo, in job environment variables, or in Build Parameters.

1. In Jenkins: **Manage Jenkins** → **Credentials**.
2. Under **Stores scoped to Jenkins**, click **System**.
3. Click **Global credentials (unrestricted)** → **Add Credentials**.
4. Fill in:

| Field | Value |
|-------|--------|
| Kind | **Username with password** |
| Scope | Global |
| Username | AWS **Access Key ID** (`AKIA...`) |
| Password | AWS **Secret Access Key** |
| ID | `aws-s3-workshop` (must match the Jenkinsfile) |
| Description | Workshop S3 deploy (IAM user with s3:PutObject) |

5. Click **Create**.

The pipeline binds those values only inside the Deploy stage via `withCredentials` (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`). Students should never see the secret in the console.

> **Alternative (no access keys):** if Jenkins runs on EC2 with an instance profile that can `s3:PutObject`, you can skip Jenkins credentials and remove the `withCredentials` block so the AWS CLI uses the role — same pattern as [demo 10](../10-docker-ecr/README.md). Do **not** mix both unless you intend to override the role.

## AWS setup (once)

On the Jenkins agent: **AWS CLI v2** (`aws --version`).

In AWS:

1. Create an S3 bucket (name is globally unique). Note the **region**.
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

4. The IAM user whose keys you stored needs at least:

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

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-14-deploy-s3` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/14-deploy-s3/Jenkinsfile` |

> After the first build, Jenkins discovers the parameters. Use **Build with Parameters** and enter `S3_BUCKET`. The first **Build Now** fails on purpose if the bucket name is empty.

## How to test

1. Add credential `aws-s3-workshop` (steps above).
2. Create the job and click **Build Now** once (parameters register; this run may fail if `S3_BUCKET` is blank).
3. Click **Build with Parameters**.
4. Set `S3_BUCKET` to your bucket, `AWS_REGION` to the bucket’s region, optionally change `SITE_TITLE`.
5. **Build**.
6. Open the website URL from the console (hyphen vs dot depends on region):

```
http://<S3_BUCKET>.s3-website-<AWS_REGION>.amazonaws.com
http://<S3_BUCKET>.s3-website.<AWS_REGION>.amazonaws.com
```

You should see **Deployed to Amazon S3** and your title.

## Expected console highlights

```
Wrote .../site/index.html
Uploaded s3://your-bucket/index.html
Try: http://your-bucket.s3-website-us-east-1.amazonaws.com
```

The Access Key / Secret must **not** appear in the log (Jenkins prints `****`).

## Files

| File | Purpose |
|------|---------|
| `index.html` | Page template |
| `generate_site.py` | Writes `site/index.html` with title, bucket, build number |
| `Jenkinsfile` | Generate → Deploy (`aws s3 cp` + `withCredentials`) |

## Try it

Rebuild with a different `SITE_TITLE` and refresh the S3 URL. The heading should change.

## Next

Back to the [demos index](../README.md), or continue with any remaining challenges.
