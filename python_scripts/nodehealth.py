import psutil

def check_system_health():
    # Check CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

    # Check Memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    # Check Disk usage
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

    # Check Network statistics
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent // (1024 ** 2)} MB")
    print(f"Bytes Received: {net_io.bytes_recv // (1024 ** 2)} MB")

# Run the system health check
check_system_health()

