from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'live_demo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    counter = models.IntegerField(initial=0)


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        print('received a bid from', player.id_in_group, ':', data)
        player.counter += 1
        return {0: player.counter}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
