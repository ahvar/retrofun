# PostgreSQL Setup Guide

## Prerequisites
- Docker Desktop installed
- [docker-compose.yml](docker-compose.yml) configured
- [.env](.env) file with passwords (not tracked in git)

## Initial Setup

### 1. Configure Environment Variables
Create [.env](.env) in project root:
```
POSTGRES_PASSWORD=<admin-password>
PGADMIN_DEFAULT_EMAIL=<your-email>
PGADMIN_DEFAULT_PASSWORD=<pgadmin-password>
DATABASE_URL=postgresql+psycopg2://retrofun:<user-password>@localhost:5432/retrofun
```

### 2. Start Docker Containers
```sh
docker compose up -d
```
Wait 1-2 minutes for services to initialize.

### 3. Login to pgAdmin as Admin
1. Open browser to http://localhost:8080
2. Login with `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` from [.env](.env)

### 4. Add PostgreSQL Server to pgAdmin
1. Click "Add New Server"
2. **General tab**: Name = `db`
3. **Connection tab**:
   - Host name/address: `db`
   - Port: `5432`
   - Maintenance database: `postgres`
   - Username: `postgres`
   - Password: `POSTGRES_PASSWORD` from [.env](.env)
   - Save password: ✓

### 5. Create retrofun User
1. Right-click `db` → Create → Login/Group Role
2. **General tab**: Name = `retrofun`
3. **Definition tab**: Password = `<user-password>` (from `DATABASE_URL` in [.env](.env))
4. **Privileges tab**:
   - Can login: ✓
   - Inherit rights from parent roles: ✓
   - All others: ✗
5. Click Save

### 6. Create retrofun Database
1. Right-click `db` → Create → Database
2. Database name: `retrofun`
3. Owner: `postgres`
4. Click Save

### 7. Grant User Permissions
1. Expand: db → Databases → retrofun → Schemas → public
2. Right-click `public` → Properties
3. **Security tab** → Click "+" in Privileges table
4. Grantee: `retrofun`
5. Privileges: ✓ ALL
6. Click Save

## Testing Login Persistence

### Stop Containers
```sh
docker compose down
```

### Restart Containers
```sh
docker compose up -d
```

### Verify Admin Access
1. Open http://localhost:8080
2. Login with pgAdmin credentials from [.env](.env)
3. Server `db` should reconnect automatically

### Verify User Access (Python)
```sh
python db.py
```
The [`engine`](db.py) in [db.py](db.py) should connect successfully using `DATABASE_URL` from [.env](.env).

## Troubleshooting

### Reset Everything (Nuclear Option)
If you exhaust login attempts or need to start fresh:
```sh
docker compose down -v
docker compose up -d
```
**Warning**: This deletes all data in `db-data` and `admin-data` volumes.

## Password Management
- Store in [.env](.env) (gitignored in [.gitignore](.gitignore))
- Or use `password.txt` (also gitignored)
- Never commit passwords to git