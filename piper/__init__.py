from piper.application.application_runner import ApplicationRunner
from piper.bootstrap import bootstrap_di


def main():
    bootstrap_di()

    ApplicationRunner().run()
