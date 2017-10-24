# coding: utf-8

"""
    Aces Encoded Listener API

    API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ValidationError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'message': 'str',
        'field_errors': 'list[FieldError]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'field_errors': 'field_errors'
    }

    def __init__(self, code=None, message=None, field_errors=None):
        """
        ValidationError - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._field_errors = None
        self.discriminator = None

        if code is not None:
          self.code = code
        if message is not None:
          self.message = message
        if field_errors is not None:
          self.field_errors = field_errors

    @property
    def code(self):
        """
        Gets the code of this ValidationError.

        :return: The code of this ValidationError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ValidationError.

        :param code: The code of this ValidationError.
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ValidationError.

        :return: The message of this ValidationError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidationError.

        :param message: The message of this ValidationError.
        :type: str
        """

        self._message = message

    @property
    def field_errors(self):
        """
        Gets the field_errors of this ValidationError.

        :return: The field_errors of this ValidationError.
        :rtype: list[FieldError]
        """
        return self._field_errors

    @field_errors.setter
    def field_errors(self, field_errors):
        """
        Sets the field_errors of this ValidationError.

        :param field_errors: The field_errors of this ValidationError.
        :type: list[FieldError]
        """

        self._field_errors = field_errors

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other