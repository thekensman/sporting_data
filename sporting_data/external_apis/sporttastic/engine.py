from sporting_data.external_apis import Engine

class Engine(Engine):
    url_suffix = "/sporttastic.json"

    @classmethod
    def fetch_data(cls):
        raise NotImplementedError("To be completed")
