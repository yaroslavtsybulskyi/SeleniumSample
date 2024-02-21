import requests


class My_Api:
    def __init__(self, base_url="https://httpbin.org"):
        self.base_url = base_url

    def get_image_format(self, image_format):
        if image_format in ["jpeg", "png", "svg", "webp"]:
            url = f"{self.base_url}/image/{image_format}"
            payload = {}
            headers = {
                "accept": f"image/{image_format}",
                "Authorization": "Basic YWRtaW46YWRtaW4=",
            }
            response = requests.get(url, headers=headers, data=payload)
            return response
        else:
            raise ValueError(f"Unsupported image format: {image_format}")

    def get_jpeg(self):
        return self.get_image_format("jpeg")

    def get_png(self):
        return self.get_image_format("png")

    def get_svg(self):
        return self.get_image_format("svg")

    def get_webp(self):
        return self.get_image_format("webp")

    def get_image(self):
        url = f"{self.base_url}/image"
        payload = {}
        headers = {"accept": "image/webp"}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response
