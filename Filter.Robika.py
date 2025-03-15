from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import random
import string
from time import sleep

console = Console()

def show_title():
    console.print(Panel(Text("A.hacker  Cyber Filter Tool", justify="center", style="bold cyan"), border_style="bold magenta"))
    console.print(Panel(Text("This tool simulates filtering operations for accounts, groups, and channels.", justify="center", style="bold green")))

def generate_filter_code():
    console.print("\n[bold cyan]Generating a random Filter Code...[/bold cyan]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Creating Code...", total=100)
        for _ in range(10):
            sleep(0.2)
            progress.update(task, advance=10)
    code = f"IP-{'.'.join(str(random.randint(0, 255)) for _ in range(4))}-FILTER-{''.join(random.choices(string.ascii_uppercase + string.digits, k=12))}"
    console.print(f"[bold green]Your Filter Code: [bold magenta]{code}[/bold magenta]\n")
    return code

def connect_to_server():
    console.print("\n[bold cyan]Connecting to Rubika server...[/bold cyan]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Establishing connection...", total=100)
        for i in range(10):
            sleep(0.3)
            progress.update(task, advance=10)
    console.print("[bold green]Connection established successfully![/bold green]\n")

def generate_report(item, reports, item_type):
    connect_to_server()
    for i in range(1, reports + 1):
        sleep(1)
        status = random.choice(["success", "failure"])
        if status == "success":
            console.print(f"[bold green]Report {i}[/bold green]: {item_type} {item} processed successfully.")
        else:
            console.print(f"[bold red]Report {i}[/bold red]: {item_type} {item} failed to process.")
    console.print("[bold cyan]All reports completed![/bold cyan]")

def account_filter():
    console.print(Panel("Simulating [bold cyan]Account Filtering[/bold cyan]", style="bold green"))
    account_id = console.input("[bold cyan]Enter the Account ID: [/bold cyan]")
    reports = int(console.input("[bold yellow]How many reports to generate? [/bold yellow]"))
    generate_report(account_id, reports, "Account ID")

def group_filter():
    console.print(Panel("Simulating [bold cyan]Group Filtering[/bold cyan]", style="bold green"))
    group_link = console.input("[bold cyan]Enter the Group Link: [/bold cyan]")
    reports = int(console.input("[bold yellow]How many reports to generate? [/bold yellow]"))
    generate_report(group_link, reports, "Group Link")

def channel_filter():
    console.print(Panel("Simulating [bold cyan]Channel Filtering[/bold cyan]", style="bold green"))
    channel_link = console.input("[bold cyan]Enter the Channel Link: [/bold cyan]")
    reports = int(console.input("[bold yellow]How many reports to generate? [/bold yellow]"))
    generate_report(channel_link, reports, "Channel Link")

def how_it_works():
    console.print(Panel("This tool simulates filtering operations. For each option, you'll provide the required data (e.g., Account ID, Group Link, or Channel Link). The tool will then connect to the Rubika server and generate simulated reports.", style="bold green"))

def main_menu():
    while True:
        console.clear()
        show_title()
        console.print("[bold cyan]Choose an option:[/bold cyan]")
        console.print("[1] Start the Tool")
        console.print("[2] Generate Filter Code")
        console.print("[3] Exit")
        choice = console.input("\n[bold cyan]Your choice: [/bold cyan]")

        if choice == "1":
            cyber_tool_menu()
        elif choice == "2":
            generate_filter_code()
        elif choice == "3":
            console.print("\n[bold red]Exiting the tool... Goodbye![/bold red]\n")
            sleep(1)
            break
        else:
            console.print("[bold red]Invalid choice! Please try again.[/bold red]")

def cyber_tool_menu():
    while True:
        cyber_title()
        menu()
        choice = console.input("[bold cyan]Your choice: [/bold cyan]")
        if choice == "1":
            account_filter()
        elif choice == "2":
            group_filter()
        elif choice == "3":
            channel_filter()
        elif choice == "4":
            how_it_works()
        elif choice == "5":
            console.print("[bold red]Returning to main menu...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice! Please try again.[/bold red]")

def cyber_title():
    console.print(Panel(Text("Cyber Filter Simulation Tool", justify="center", style="bold cyan"), title="[bold magenta]Cyber Filter Tool"))

def menu():
    console.print("\n[bold cyan]Please choose an option:[/bold cyan]")
    console.print("[1] Account")
    console.print("[2] Group")
    console.print("[3] Channel")
    console.print("[4] How it works")
    console.print("[5] Back to Main Menu")

if __name__ == "__main__":
    main_menu()
