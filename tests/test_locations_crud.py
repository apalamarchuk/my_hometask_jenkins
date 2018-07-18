import pytest
from utils.endpoints.locations import *
from resource.test_data import *
from resource.model.Location import *


class TestAPIMethods:
    id = None
    init_data = prep_data["us1"]
    new_data = prep_data["de2"]

    def setup_method(self, method):
        if method.__name__ in ["test_delete_method_positive",
                               "test_put_method_positive",
                               "test_get_by_id_method_positive"]:
            print("setup_method      method:%s" % method.__name__)
            response = Locations.post(self.init_data)
            response_body = response.json()
            self.id = str(response_body.get("id"))

    def teardown_method(self, method):
        if method.__name__ in ["test_post_method_positive",
                               "test_put_method_positive",
                               "test_get_by_id_method_positive"]:
            print("teardown_method   method:%s" % method.__name__)
            Locations.delete(self.id)

    def test_get_method_positive(self):
        response = Locations.get_list()
        response_body = response.json()
        assert 200 == response.status_code
        assert response_body is not None

    def test_get_all_method_positive(self):
        response = Locations.get_all()
        response_body = response.json()
        assert 200 == response.status_code
        assert response_body is not None

    def test_get_by_id_method_positive(self):
        response_body = Locations.get_by_id(self.id)
        assert str(response_body.get("id")) == self.id
        assert Location(self.init_data) == Location(response_body)

    @pytest.mark.parametrize("value", [-1, 0, 9999])
    def test_get_by_id_negative(self, value):
        response_body = Locations.get_by_id(value)
        assert response_body is None

    def test_delete_method_positive(self):
        response = Locations.delete(self.id)
        assert 200 == response.status_code
        response = Locations.get_list()
        response_body = response.json()
        for x in response_body:
            assert x["id"] != self.id

    @pytest.mark.parametrize("value", [-1, 0, 9999])
    def test_delete_method_negative(self, value):
        response = Locations.delete(value)
        #response_body = response.json()
        assert 404 == response.status_code
	print("lol")
        #assert response_body.get("error") is not None

    def test_put_method_positive(self):
        response = Locations.put(self.new_data, self.id)
        assert 200 == response.status_code
        response_body = Locations.get_by_id(self.id)
        assert Location(self.new_data) == Location(response_body)

    @pytest.mark.parametrize("value", [None, "", " ", "random text #142 !@#&@' ' / \n <>", prep_data["missing_fields"]])
    def test_put_method_negative(self, value):
        response = Locations.put(value, self.id)
        response_body = response.json()
        assert 400 == response.status_code
        assert response_body.get("error") is not None

    def test_post_method_positive(self):
        response = Locations.post(self.init_data)
        response_body = response.json()
        assert 200 == response.status_code
        assert Location(self.init_data) == Location(response_body)

    @pytest.mark.parametrize("value", [None, "", " ", "random text #142 !@#&@' ' / \n <>", prep_data["missing_fields"]])
    def test_post_method_negative(self, value):
        response = Locations.post(value)
        response_body = response.json()
        assert 400 == response.status_code
        assert response_body.get("error") is not None
