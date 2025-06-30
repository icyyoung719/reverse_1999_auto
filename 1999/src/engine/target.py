from engine.engineconfig import EngineConfig
from engine.api import click_on_image

class EngineTarget:
    name = None
    path = None
    offset = None
    min_similar = EngineConfig.MIN_SIMILARITY

    def __init__(self, name, path, min_similar = EngineConfig.MIN_SIMILARITY, offset = None):
        self.name = name
        self.path = path
        self.min_similar = min_similar
        self.offset = offset

    def click(self, scale, similar = None):
        if similar is None:
            similar = self.min_similar
        print(f"{self.name} clicked")
        return click_on_image(self.path, scale= scale, similar = similar, click_offset = self.offset)