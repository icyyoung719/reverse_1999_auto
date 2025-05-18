from engine.target import EngineTarget
from config.config import Config
# from config.config import Config
# from engine import Engine


class Target(EngineTarget):
    def __init__(self, name, path, min_similar=0.8, offset=None):
        if Config.LANGUAGE == "en":
            processed_path = path.replace('./assets', './assets/en').replace('.jpg', '.png')
        else:
            processed_path = path

        super().__init__(name, processed_path, Config.MIN_SIMILARITY, offset)
        
        # self.min_similar = MIN_SIMILARITY


    # def click(self, similar=None):
    #     return super().click(similar)

