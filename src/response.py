import logging
import allure


class AssertableResponse(object):

    def __init__(self, response):
        logging.info(f"Request {response.request.url} \n {response.request.body}")
        logging.info(f"Response status code:{response.status_code} body:{response.text}")
        self._response = response

    # @allure.step("status code should be '{code}'")
    # def status_code(self, code):
    #     logging.info("Assert: status code should be {}".format(code))
    #     return self._response.status_code == code
    #
    # def field(self, name):
    #     return self._response.json()[name]

    @allure.step("response should have {condition}")
    def should_have(self, condition):
        logging.info(f"About to check {condition}")
        condition.match(self._response)
        return self
