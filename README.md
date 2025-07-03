# Orange County Lettings App

Orange County Lettings is a web app for a startup in the property rentals industry expanding across the U.S.

## LOCAL DEVELOPMENT

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed the command `python` in 
your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings.git`

### Create the virtual environment

#### macOS / Linux

- `cd /path/to/Python-OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (If previous step errors with package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm the command `python` now runs the Python interpreter in the virtual environment,
`which python`
- Confirm the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm the command `pip` runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Windows

Using PowerShell, as above except:

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 


### Run the site

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm the site is running and can be navigated (you should see several profiles and lettings).

### Admin panel

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`


## PRODUCTION DEPLOYEMENT

### Deployment Overview
This project uses a GitHub Actions CI/CD pipeline to automate testing, containerization, and deployment of the Django app to an AWS EC2 instance.

Changes pushed to the master branch trigger the full pipeline: tests → build Docker image → push to Docker Hub → deploy to EC2.

Changes to other branches only trigger tests to ensure code quality without deploying or building images.

The app runs inside a Docker container on the EC2 instance, ensuring consistency between local development and production environments.

### Configuration
To get the deployment working correctly, the following configurations are required:

#### GitHub Secrets:

- DOCKER_USERNAME and DOCKER_TOKEN — Docker Hub credentials for pushing images.

- EC2_SSH_KEY — Private SSH key to SSH into your EC2 instance securely.

- EC2_HOST — Public IP or DNS of your EC2 instance.

#### EC2 Instance Setup:

- Docker installed and running on the EC2 instance.

- Security group configured to allow inbound traffic on port 8000 (or your app port).

- .env file placed in /home/ubuntu/.env with necessary environment variables for Django.

#### AWS Setup:

- EC2 instance running and accessible from the internet.

- Elastic IP assigned for a static public IP to avoid changing IP issues.

### Deployment Steps

1. Push changes to master branch. This automatically triggers the GitHub Actions workflow which starts pipeline.

2. Pipeline has following stages:
    - Build and Test: Tests to verify code quality.

    - Containerize: Starts only after success of previous stage. Builds and tag the Docker image using the current commit hash. Pushes the Docker image to Docker Hub.

    - Deploy-Production: Starts only after success of previous stage. SSH into the EC2 instance and pull the new Docker image.

3. Stop any running container and start a new container with the updated image.

**Note**: If EC2 instance is stopped or deleted, start a new EC2 instance.
Make sure Docker and .env are set up as per configuration above.
Push a commit to master to trigger deployment. The new instance will automatically pull and run the app container.
If any issues arise, check the GitHub Actions logs in the Actions tab of the repository and the EC2 instance logs.

