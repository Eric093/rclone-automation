from rich.console import Console
from rich.live import Live
from rich.table import Table
import psutil
import sys


def system_stats():
    table = Table(title="System Stats", title_style="bold cyan")
    table.add_column("Metric", style="bold green")
    table.add_column("Value", style="yellow")
    table.add_column("Details", style="dim white")

    cpu = f"{psutil.cpu_percent()}%"
    memory = f"{psutil.virtual_memory().percent}%"
    disk = f"{psutil.disk_usage('/').percent}%"
    cpu_freq = f"{psutil.cpu_freq().current} MHz"
    num_processes = len(psutil.pids())
    uptime = f"{psutil.boot_time()}"

    network_stats = psutil.net_io_counters()
    net_sent = f"{network_stats.bytes_sent / (1024 * 1024):.2f} MB"
    net_recv = f"{network_stats.bytes_recv / (1024 * 1024):.2f} MB"

    battery = psutil.sensors_battery()
    battery_status = f"{battery.percent}% charging" if battery else "N/A"

    table.add_row("CPU Usage", cpu, cpu_freq)
    table.add_row("Memory Usage", memory, "Used RAM and swap memory")
    table.add_row("Disk Usage", disk, "Disk usage for the root directory")
    table.add_row("Number of Processes", str(num_processes), "Total running processes")
    table.add_row("System Uptime", uptime, "Last boot time")
    table.add_row("Network Sent", net_sent, "Data sent over network")
    table.add_row("Network Received", net_recv, "Data received over network")
    table.add_row("Battery Status", battery_status, "Battery health (if applicable)")

    return table


console = Console()

try:
    with Live(system_stats(), refresh_per_second=1) as live:
        while True:
            live.update(system_stats())
except KeyboardInterrupt:
    console.print("\nExiting program... Goodbye!", style="bold cyan")
    sys.exit(0)