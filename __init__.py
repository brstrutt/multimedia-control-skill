from mycroft import MycroftSkill, intent_file_handler
import mpris2

class MultimediaControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.mediaPlayer = None

    def initialize(self):
        # Grab the first URI in the list. This will just grab whatever media player happens to be first.
        try:
            uri = next(mpris2.get_players_uri())
            self.mediaPlayer = mpris2.Player(dbus_interface_info={'dbus_uri': uri})
        except StopIteration:
            pass

        self.log.info("Multimedia Control started. Controlling URI: " + str(uri))
        
        # Bind to the various audio service messages
        self.add_event('mycroft.audio.service.play',
                   self.handler_mycroft_audio_service_play)
        self.add_event('mycroft.audio.service.stop',
                   self.handler_mycroft_audio_service_stop)
        self.add_event('mycroft.audio.service.pause',
                   self.handler_mycroft_audio_service_pause)
        self.add_event('mycroft.audio.service.resume',
                   self.handler_mycroft_audio_service_resume)
        self.add_event('mycroft.audio.service.next',
                   self.handler_mycroft_audio_service_next)
        self.add_event('mycroft.audio.service.prev',
                   self.handler_mycroft_audio_service_prev)
    
    def handler_mycroft_audio_service_play(self, message):
        self.log.info("mycroft audio service play received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Play()

    def handler_mycroft_audio_service_stop(self, message):
        self.log.info("mycroft audio service stop received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Pause()

    def handler_mycroft_audio_service_pause(self, message):
        self.log.info("mycroft audio service pause received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Pause()

    def handler_mycroft_audio_service_resume(self, message):
        self.log.info("mycroft audio service resume received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Play()

    def handler_mycroft_audio_service_next(self, message):
        self.log.info("mycroft audio service next received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Next()

    def handler_mycroft_audio_service_prev(self, message):
        self.log.inf("mycroft audio service prev received")
        if self.mediaPlayer != None:
            self.mediaPlayer.Previous()



def create_skill():
    return MultimediaControl()

