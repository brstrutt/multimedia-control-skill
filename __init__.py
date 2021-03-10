from mycroft import MycroftSkill, intent_file_handler
import mpris2

class MultimediaControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        this.mediaPlayer = None

        # Grab the first URI in the list. This will just grab whatever media player happens to be first.
        try:
            uri = next(mpris2.get_players_uri())
            this.mediaPlayer = mpris2.Player(dbus_interface_info={'dbus_uri': uri})
        except StopIteration:
            pass
    
    def handler_mycroft_audio_service_play(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Play()

    def handler_mycroft_audio_service_stop(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Pause()

    def handler_mycroft_audio_service_pause(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Pause()

    def handler_mycroft_audio_service_resume(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Play()

    def handler_mycroft_audio_service_next(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Next()

    def handler_mycroft_audio_service_prev(self, message):
        if this.mediaPlayer != None:
            this.mediaPlayer.Previous()



def create_skill():
    return MultimediaControl()

