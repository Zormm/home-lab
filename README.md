# Home Lab Docker Stacks

A collection of Docker Compose stacks for common home lab services, designed for easy deployment with Portainer.

## 📁 Structure

Each stack is contained in its own folder under `stacks/` with:
- `docker-compose.yml` - The Docker Compose configuration
- `.env.example` - Example environment variables (copy to `.env` and customize)

## 🚀 Available Stacks

### Core Management

#### Portainer
**Path:** `stacks/portainer/`  
**Description:** Container management platform with web UI  
**Ports:** 9000 (HTTP), 9443 (HTTPS)  
**Usage:** Essential for managing Docker containers through a web interface

#### Watchtower
**Path:** `stacks/watchtower/`  
**Description:** Automatic Docker container updates  
**Configuration:** Set update schedule and notification preferences in `.env`

### Reverse Proxy & SSL

#### Traefik
**Path:** `stacks/traefik/`  
**Description:** Modern reverse proxy with automatic SSL certificates  
**Ports:** 80 (HTTP), 443 (HTTPS), 8080 (Dashboard)  
**Requirements:** Configure ACME email and domain in `.env`

#### Nginx Proxy Manager
**Path:** `stacks/nginx-proxy-manager/`  
**Description:** Reverse proxy with easy-to-use web interface  
**Ports:** 80 (HTTP), 443 (HTTPS), 81 (Admin UI)  
**Default Credentials:** admin@example.com / changeme

### Monitoring & Dashboard

#### Uptime Kuma
**Path:** `stacks/uptime-kuma/`  
**Description:** Self-hosted monitoring and status page  
**Port:** 3001  
**Features:** Monitor HTTP(s), TCP, Ping, DNS records, and more

#### Homepage
**Path:** `stacks/homepage/`  
**Description:** Modern, customizable application dashboard  
**Port:** 3000  
**Features:** Integrates with Docker to show container status

### Network Services

#### Pi-hole
**Path:** `stacks/pi-hole/`  
**Description:** Network-wide ad blocking and DNS server  
**Ports:** 53 (DNS), 8053 (Web UI)  
**Note:** Change default password in `.env` before deploying

## 📋 Usage

### Deploying with Portainer

1. Navigate to **Stacks** in Portainer
2. Click **Add stack**
3. Give your stack a name
4. Upload the `docker-compose.yml` file or paste its contents
5. Upload or manually add environment variables from `.env.example`
6. Click **Deploy the stack**

### Manual Deployment

1. Navigate to the stack directory:
   ```bash
   cd stacks/<stack-name>
   ```

2. Copy and configure the environment file:
   ```bash
   cp .env.example .env
   nano .env  # Edit with your values
   ```

3. Deploy the stack:
   ```bash
   docker-compose up -d
   ```

## ⚙️ Configuration

Before deploying any stack:

1. Review the `docker-compose.yml` file
2. Copy `.env.example` to `.env`
3. Update environment variables with your specific values
4. Pay special attention to:
   - Timezone settings
   - Passwords and credentials
   - Domain names
   - IP addresses
   - Port mappings (adjust if conflicts exist)

## 🔒 Security Notes

- **Always change default passwords** in `.env` files
- Review port mappings and only expose what's necessary
- Consider using a reverse proxy (Traefik or NPM) for SSL termination
- Keep containers updated (Watchtower can help with this)
- Backup your data volumes regularly

## 🛠️ Customization

Feel free to modify the stacks to fit your needs:
- Adjust resource limits
- Change port mappings
- Add additional volumes
- Configure network modes
- Add more services to existing stacks

## 📝 Adding New Stacks

To add a new stack:

1. Create a new directory under `stacks/`
2. Add a `docker-compose.yml` file
3. Create an `.env.example` file with required variables
4. Update this README with stack information

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new stacks
- Improve existing configurations
- Enhance documentation
- Report issues

## 📄 License

This repository is provided as-is for personal and educational use.