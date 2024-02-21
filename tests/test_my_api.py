import pytest
import allure


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test valid request")
@pytest.mark.parametrize("extension", [("jpeg"), ("webp"), ("svg"), ("png")])
def test_status_code(my_api, extension):
    response = my_api.get_image_format(extension)
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test invalid request")
@pytest.mark.parametrize("extension", [("jpeg1"), ("wrbp"), ("srvg"), ("pgng")])
def test_status_code_wrong_extension(my_api, extension):
    with pytest.raises(ValueError) as e:
        my_api.get_image_format(extension)
    assert str(e.value) == f"Unsupported image format: {extension}"


@allure.feature("My Api")
@allure.story("Content-type")
@allure.title("Test content-type")
@pytest.mark.parametrize("extension", [("jpeg"), ("webp"), ("svg"), ("png")])
def test_header_content(my_api, extension):
    response = my_api.get_image_format(extension)
    if extension == "svg":
        assert response.headers["Content-Type"] == f"image/{extension}+xml"
    else:
        assert response.headers["Content-Type"] == f"image/{extension}"


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test jpeg")
def test_status_code_jpeg(my_api):
    response = my_api.get_jpeg()
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test svg")
def test_status_code_svg(my_api):
    response = my_api.get_svg()
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test png")
def test_status_code_png(my_api):
    response = my_api.get_png()
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Status Code")
@allure.title("Test webp")
def test_status_code_webp(my_api):
    response = my_api.get_webp()
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Content-type")
@allure.title("Test Content-type jpeg")
def test_content_type_jpeg(my_api):
    response = my_api.get_jpeg()
    assert response.headers["Content-Type"] == "image/jpeg"


@allure.feature("My Api")
@allure.story("Content-type")
@allure.title("Test Content-type png")
def test_content_type_png(my_api):
    response = my_api.get_png()
    assert response.headers["Content-Type"] == "image/png"


@allure.feature("My Api")
@allure.story("Content-type")
@allure.title("Test Content-type webp")
def test_content_type_webp(my_api):
    response = my_api.get_webp()
    assert response.headers["Content-Type"] == "image/webp"


@allure.feature("My Api")
@allure.story("Content-type")
@allure.title("Test Content-type svg")
def test_content_type_svg(my_api):
    response = my_api.get_svg()
    assert response.headers["Content-Type"] == "image/svg+xml"


@allure.feature("My Api")
@allure.story("Request")
@allure.title("Test Get image request")
def test_get_image_status_code(my_api):
    response = my_api.get_image()
    assert response.status_code == 200


@allure.feature("My Api")
@allure.story("Request")
@allure.title("Test Get image Content-type")
def test_get_image_content(my_api):
    response = my_api.get_image()
    assert response.headers["Content-Type"] == "image/webp"
