from odoo import _, api, fields, models
from datetime import datetime
import pytz

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    def _auto_attendance_checkout(self):
        current_time_lisbon = datetime.now(pytz.timezone('Europe/Lisbon'))
        current_time_brazil = datetime.now(pytz.timezone('America/Sao_Paulo'))

        # admin_datetime gets the admin user tz (same format as above):
        admin_datetime = datetime.now(pytz.timezone(self.env['res.users'].browse(1).tz))

        checked_out_records = self.search([('check_out', '=', False), ('check_in', '!=', False)])
        for record in checked_out_records:
            check_in_datetime = fields.Datetime.from_string(record.check_in)

            # Convert current datetime to user's timezone
            converted_datetime = self._convert_to_admin_tz(record.employee_id, admin_datetime)

            # Calculate logout time in user's timezone
            logout_time_user_tz = self._get_logout_time(admin_datetime, record.employee_id)

            # Update check_out field with logout time
            record.check_out = logout_time_user_tz.strftime('%Y-%m-%d %H:%M:%S')

            print(f"\n============== USER DATA ==============\n")
            print(f"\tUSER NAME: {record.employee_id.name}")
            print(f"\tUSER TIME (ADMIN TZ): {converted_datetime}")

            print(f"\n\tCHECK IN: {check_in_datetime}")
            print(f"\tCHECK OUT: {record.check_out}")

            print(f"\n\tLISBON TZ: {current_time_lisbon}")
            print(f"\tBRAZIL TZ: {current_time_brazil}")
            print(f"\tADMIN TZ: {admin_datetime}")
            print(f"\tSERVER DATETIME: {fields.Datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\tSERVER TZ: {fields.Datetime.now().tzname()}\n")

    def _convert_to_admin_tz(self, employee, admin_tz):
        user_tz = pytz.timezone(employee.tz)
        converted_datetime = admin_tz.astimezone(user_tz)

        return converted_datetime

    def _get_logout_time(self, check_in_datetime, employee):
        user_tz = pytz.timezone(employee.tz)
        logout_time = check_in_datetime.replace(hour=18, minute=0, second=0)
        convert_checkout_time = logout_time.astimezone(user_tz)

        return convert_checkout_time
