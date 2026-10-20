from django.apps import AppConfig
from django.core.signals import setting_changed


def _reset(setting, **kwargs):
    if setting == "ALLYMAILER":
        from . import reset

        reset()


class AllymailerConfig(AppConfig):
    name = "allymailer_wrapper"
    verbose_name = "AllyMailer"

    def ready(self):
        setting_changed.connect(_reset, dispatch_uid="allymailer_wrapper.reset")
