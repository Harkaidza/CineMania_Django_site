from django_cron import CronJobBase, Schedule
from django.core.management import call_command
from datetime import datetime
import yadisk

yaToken = 'AgAAAABIgUuLAAbdqn180kzte0CrnZjfYLqSaaw'


class doDump(CronJobBase):
    RUN_EVERY_MINS = 60 * 24
    RUN_AT_TIMES = ['05.00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=RUN_EVERY_MINS)
    code = "main.doDump"

    def do(self):
        file_json = open('dump.json', 'w')
        call_command('dumpdata', format='json', indent=3, stdout=file_json)
        file_json.close()

        file_xml = open('dump.xml', 'w')
        call_command('dumpdata', format='xml', indent=3, stdout=file_xml)
        file_xml.close()

        y = yadisk.YaDisk(token=yaToken)
        date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
        json = "D:/WorksPackagesTable/all_semestr/5_semestr/BD/Lab#6_django/dump.json"
        xml = "D:/WorksPackagesTable/all_semestr/5_semestr/BD/Lab#6_django/dump.xml"
        y.mkdir(f"Lab#6_django/{date}")
        y.upload(json, f"Lab#6_django/{date}/dump.json")
        y.upload(xml, f"Lab#6_django/{date}/dump.xml")




