from mycroft.skills.displayservice import DisplayBackend
from mycroft.messagebus.message import Message
from mycroft.util.log import getLogger
from os.path import abspath
import imutils
import cv2

logger = getLogger(abspath(__file__).split('/')[-2])

class OpenCVService(DisplayBackend):
    def __init__(self, config, emitter, name='opencv'):
        self.config = config
        self.process = None
        self.emitter = emitter
        self.name = name
        self.emitter.on('OpenCVServiceShow', self._show)
        # image size
        self.width = 500
        self.height = 500

    def show(self, pic):
        logger.info('Call OpenCVServiceShow')
        self.emitter.emit(Message('OpenCVServiceShow', {"pic": pic}))

    def _show(self, message):
        logger.info('OpenCVService._Show')
        pic = message.data["pic"]

        # show in opencv2
        image = cv2.imread(pic)
        image = imutils.resize(image, self.width, self.height)
        # Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)
        #  SIGSEGV 139 attempt to access a virtual address which is not in your address space
        cv2.imshow("OpenCV Display", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def stop(self):
        logger.info('OpenCVServiceStop')
        cv2.destroyAllWindows()