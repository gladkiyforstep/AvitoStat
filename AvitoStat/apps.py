from django.apps import AppConfig


class AvitostatConfig(AppConfig):
    name = 'AvitoStat'

    def ready(self):
        from .regular_task import EveryHourTask
        from .counter_creator import create_counters
        a = EveryHourTask(create_counters)
        a.run()
        print('start with regular task')
