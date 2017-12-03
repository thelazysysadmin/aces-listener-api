# coding: utf-8

"""
    ACES Listener API

    API Specification for ACES Listeners that read data on a blockchain and forward transaction events to registered subscribers. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FieldError(object):
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
        'field': 'str',
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'field': 'field',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, field=None, code=None, message=None):
        """
        FieldError - a model defined in Swagger
        """

        self._field = None
        self._code = None
        self._message = None
        self.discriminator = None

        if field is not None:
          self.field = field
        if code is not None:
          self.code = code
        if message is not None:
          self.message = message

    @property
    def field(self):
        """
        Gets the field of this FieldError.

        :return: The field of this FieldError.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this FieldError.

        :param field: The field of this FieldError.
        :type: str
        """

        self._field = field

    @property
    def code(self):
        """
        Gets the code of this FieldError.

        :return: The code of this FieldError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this FieldError.

        :param code: The code of this FieldError.
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this FieldError.

        :return: The message of this FieldError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this FieldError.

        :param message: The message of this FieldError.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, FieldError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other