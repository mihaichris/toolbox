import typer

from datetime import datetime
from common.work import get_month_working_hours, get_month_working_days

from common.output import show_message

app = typer.Typer(name="Business CLI Tool")


@app.command("working_hours")
def working_hours(is_today: bool = typer.Option(False, '--today', help="Get current day working hours.", is_flag=True),
                  is_month: bool = typer.Option(False, '--this-month', help="Get current month working hours.", is_flag=True)):
    """Get working hours based of a date period."""
    year = datetime.now().year
    if is_today:
        show_message("Current day working hours: {0}".format(8))
    if is_month:
        month = datetime.now().month
        month_working_hours = get_month_working_hours(month, year)
        show_message("Current month working hours: {0}".format(
            month_working_hours))


@app.command("working_days")
def working_days(is_month: bool = typer.Option(False, '--this-month', help="Get current month working days.", is_flag=True)):
    """Get working days based of a date period."""
    year = datetime.now().year
    if is_month:
        month = datetime.now().month
        show_message("Current month working days: {0}".format(
            get_month_working_days(month, year)))
