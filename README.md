# Store Inventory API
 
A REST API for managing store inventory, built with FastAPI and PostgreSQL, deployed on AWS EC2.
 
## Tech Stack
 
- **Language:** Python 3.13
- **Framework:** FastAPI
- **Database:** PostgreSQL 18
- **Server:** AWS EC2 (Ubuntu 24.04, t2.micro)
- **Version Control:** Git & GitHub

## Project Structure
 
```
store-inventory-api/
├── venv/          # Virtual environment (not tracked)
├── .env           # Database credentials (not tracked)
├── db.py          # Database connection
└── main.py        # FastAPI application
```
 
## Database Schema
 
```
categories
  └── products (category_id → categories.id)
        └── suppliers (supplier_id → suppliers.id)
```
 
## API Endpoints
 
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/low-stock?threshold=100` | Get products below stock threshold |
| GET | `/docs` | Interactive API documentation (Swagger UI) |
 
## Local Setup
 
### Prerequisites
- Python 3.10+
- PostgreSQL
- Git

### Steps
 
```bash
# Clone the repo
git clone https://github.com/your-username/store-inventory-api.git
cd store-inventory-api
 
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
 
# Install dependencies
pip install fastapi uvicorn psycopg2-binary python-dotenv
 
# Create .env file
touch .env
```
 
Add the following to `.env`:
 
```
DB_HOST=localhost
DB_NAME=store_inventory
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_PORT=5432
```
 
```bash
# Run the server
uvicorn main:app --reload
```
 
API will be available at `http://localhost:8000`
 
## AWS Deployment
 
Deployed on AWS EC2 (t3.micro, free tier) running Ubuntu 24.04.
 
### Server Setup
 
```bash
# Update packages
sudo apt update && sudo apt upgrade -y
 
# Install dependencies
sudo apt install python3 python3-pip python3-venv postgresql postgresql-contrib -y
 
# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql
 
# Clone repo and set up
git clone https://github.com/your-username/store-inventory-api.git
cd store-inventory-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn psycopg2-binary python-dotenv
 
# Run
uvicorn main:app --host 0.0.0.0 --port 8000
```
 
### Security Group (Inbound Rules)
 
| Port | Protocol | Purpose |
|------|----------|---------|
| 22 | TCP | SSH |
| 80 | TCP | HTTP |
| 8000 | TCP | FastAPI |
 
## What I Learned
 
- Relational database design (primary keys, foreign keys, normalization)
- SQL — DDL (CREATE, ALTER) and DML (INSERT, SELECT)
- JOINs (INNER JOIN, LEFT JOIN), GROUP BY, aggregates
- Views and indexes
- Connecting Python to PostgreSQL with psycopg2
- Parameterized queries and SQL injection prevention
- Building REST APIs with FastAPI
- Virtual environments and dependency management
- Linux server setup and PostgreSQL configuration on Ubuntu
- Deploying a Python API to AWS EC2

## Author
 
Subhojit
 