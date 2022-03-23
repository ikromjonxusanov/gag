from rest_framework import renderers


class OwnRenderer(renderers.BaseRenderer):
    media_type = "text/shranet"
    format = "shranet"

    def to_string(self, data):
        result = ""
        if type(data) is dict:
            for k, v in data.items():
                result += f"{k}:{self.to_string(v)}" + "\n"
            return result
        elif type(data) is str:
            return data
        elif type(data) is list:
            return ",".join(map(str, data))
        return "Nan"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return self.to_string(data)
