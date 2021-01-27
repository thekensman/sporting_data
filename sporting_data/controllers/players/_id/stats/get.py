from sporting_data.controllers import Base

class Get(Base):

    def __init__(self, id, *args, **kwargs):
        self.player_id = id

    def run(self):
        raise NotImplementedError("To be completed")
