# 🖥️ Backend Setup: PostgreSQL + pgAdmin + FastAPI

This guide sets up a development environment with PostgreSQL, pgAdmin, and a FastAPI backend using Uvicorn.

---

## 📦 Install PostgreSQL

```bash
sudo apt install -y postgresql postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

# Add PostgreSQL GPG key and repository
sudo apt install -y curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

# Detect OS version and add PostgreSQL APT repo
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"

# Update and install PostgreSQL
sudo apt update
sudo apt -y install postgresql



# Install dependencies
sudo apt install -y curl ca-certificates gnupg

# Add pgAdmin GPG key and repo
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pgadmin.gpg
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

# Install pgAdmin web version
sudo apt install -y pgadmin4-web

# Run pgAdmin web setup
sudo /usr/pgadmin4/bin/setup-web.sh
---
pip install psycopg2

```bash
uvicorn app.main:app --reload

sudo systemctl enable postgresql




username 
password
Sequrity : Hashing Password 

