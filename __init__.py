from mycroft import MycroftSkill, intent_file_handler


class MultimediaControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.multimedia.intent')
    def handle_control_multimedia(self, message):
        self.speak_dialog('control.multimedia')


def create_skill():
    return MultimediaControl()

