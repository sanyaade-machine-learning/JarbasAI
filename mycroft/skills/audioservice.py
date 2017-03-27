from abc import ABCMeta, abstractmethod
import time

from mycroft.messagebus.message import Message


class AudioService():
    def __init__(self, emitter):
        self.emitter = emitter
        self.emitter.on('MycroftAudioServiceTrackInfoReply', self._track_info)
        self.info = None

    def _track_info(self, message=None):
        self.info = message.data

    def play(self, tracks=[], utterance=''):
        self.emitter.emit(Message('MycroftAudioServicePlay',
                                  data={'tracks': tracks,
                                        'utterance': utterance}))

    def track_info(self):
        self.info = None
        self.emitter.emit(Message('MycroftAudioServiceTrackInfo'))
        while self.info is None:
            time.sleep(0.1)
        return self.info


class AudioBackend():
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self, config, emitter):
        pass

    @abstractmethod
    def supported_uris(self):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def add_list(self, tracks):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def next(self):
        pass

    def previous(self):
        pass

    def lower_volume(self):
        pass

    def restore_volume(self):
        pass

    def track_info(self):
        pass