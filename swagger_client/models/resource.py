# coding: utf-8

"""
    ExaVault API

    # Introduction  Welcome to the ExaVault API documentation. Our API lets you control nearly all aspects of your ExaVault account programatically, from uploading and downloading files to creating and managing shares and notifications. Our API supports both GET and POST operations.  Capabilities of the API include:  - Uploading and downloading files. - Managing files and folders; including standard operations like move, copy and delete. - Getting information about activity occuring in your account. - Creating, updating and deleting users. - Creating and managing shares, including download-only shares and recieve folders.  - Setting up and managing notifications.  ## The API Endpoint  The ExaVault API is located at: https://api.exavault.com/v1.2/  # Testing w/ Postman  We've made it easy for you to test our API before you start full-scale development. Download [Postman](https://www.getpostman.com/) or the [Postman Chrome Extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), and then download our Postman collection, below. [Obtain your API key](#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) and you'll be able to interact with your ExaVault account immediately, so you can better understand what the capabilities of the API are.  <div class=\"postman-run-button\" data-postman-action=\"collection/import\" data-postman-var-1=\"e13395afc6278ce1555f\"></div>  ![ExaVault API Postman Colletion Usage](/images/postman.png)  If you'd prefer to skip Postman and start working with code directly, take a look at the sample code below.    # Code Libraries & Sample PHP Code  Once you're ready for full-scale development, we recommend looking at our code libraries available on [GitHub](https://github.com/ExaVault). We offer code libraries for [Python](https://github.com/ExaVault/evapi-python), [PHP](https://github.com/ExaVault/evapi-php) and [JavaScript](https://github.com/ExaVault/evapi-javascript).  While we recommend using our libraries, you're welcome to interact directly with our API via HTTP GET and POST requests -- a great option particularly if you're developing in a language for which we don't yet have sample code.     - [Download Python Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-python) - [Download PHP Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-php) - [Download JavaScript Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-javascript)  *Note: You can generate client libraries for any language using [Swagger Editor](http://editor2.swagger.io/). Just download our documentation file, past it into editor and use 'Generate Client' dropdown.*  ## Obtain Your API Key  You will need to obtain an API key for your application from the [Client Area](https://clients.exavault.com/clientarea.php?action=products) of your account.  To obtain an API key, please follow the instructions below.   + Login to the [Accounts](https://clients.exavault.com/clientarea.php?action=products) section of the Client Area.  + Use the drop down next to your desired account, and select *Manage API Keys*.  + You will be brought to the API Key management screen. Fill out the form and save to generate a new key for your app.  *NOTE: As of Oct 2017, we are in the progress of migrating customers to our next generation platform. If your account is already on our new platform, you should log into your File Manager and create your API key under Account->Developer->Manage API Keys*.  # Status Codes  The ExaVault API returns only two HTTP status codes for its responses: 200 and 500.  When the request could be successfully processed by the endpoint, the response status code will be 200, regardless of whether the requested action could be taken.  For example, the response to a getUser request for a username that does not exist in your account would have the status of 200,  indicating that the response was received and processed, but the error member of the returned response object would contain object with `message` and `code` properties.  **Result Format:**  |Success   | Error     | Results   | | ---      | :---:       |  :---:      | | 0        |  `Object` |   Empty   | | 1        |   Empty       |    `Object` or `Array`        |     When a malformed request is received, a 500 HTTP status code will be returned, indicating that the request could not be processed.  ExaVault's API does not currently support traditional REST response codes such as '201 Created' or '405 Method Not Allowed', although we intend to support such codes a future version of the API.   # File Paths  Many API calls require you to provide one or more file paths. For example, the <a href=\"#operation/moveResources\">moveResources</a> call requires both an array of source paths, **filePaths**, and a destination path, **destinationPath**. Here's a few tips for working with paths:   - File paths should always be specified as a string, using the standard Unix format: e.g. `/path/to/a/file.txt`  - File paths are always absolute _from the home directory of the logged in user_. For example, if the user **bob** had a home directory restriction of `/bob_home`, then an API call made using his login would specify a file as `/myfile.txt`, whereas an API call made using the master user ( no home directory restriction ) would specify the same file as `/bob_home/myfile.txt`.  # API Rate Limits  We rate limit the number of API calls you can make to help prevent abuse and protect system stablity. Each API key will support 500 requests per rolling five minutes. If you make more than 500 requests in a five minute period, you will receive a response with an error object for fifteen minutes.  # Webhooks  A webhook is an HTTP callback: a simple event-notification via HTTP POST. If you define webhooks for Exavault, ExaVault will POST a  message to a URL when certain things happen.     Webhooks can be used to receive a JSON object to your endpoint URL. You choose what events will trigger webhook messages to your endpoint URL.     Webhooks will attempt to send a message up to 8 times with increasing timeouts between each attempt. All webhook requests are tracked in the webhooks log.  ## Getting Started  1. Go to the Account tab inside SWFT.  2. Choose the Developer tab.  3. Configure your endpoint URL and select the events you want to trigger webhook messages.  4. Save settings.    You are all set to receive webhook callbacks on the events you selected.  ## Verification Signature  ExaVault includes a custom HTTP header, X-Exavault-Signature, with webhooks POST requests which will contain the signature for the request.  You can use the signature to verify the request for an additional level of security.  ## Generating the Signature  1. Go to Account tab inside SWFT.  2. Choose the Developer tab.  3. Obtain the verification token. This field will only be shown if you've configured your endpoint URL.  4. In your code that receives or processes the webhooks, you should concatenate the verification token with the JSON object that we sent in our      POST request and hash it with md5.     ```     md5($verificationToken.$webhooksObject);     ```  5. Compare signature that you generated to the signature provided in the X-Exavault-Signature HTTP header  ## Example JSON Response Object  ```json   {     \"accountname\": \"mycompanyname\",     \"username\": \"john\"     \"operation\": \"Upload\",     \"protocol\": \"https\",     \"path\": \"/testfolder/filename.jpg\"     \"attempt\": 1   } ```  ## Webhooks Logs  Keep track of all your webhooks requests in the Activity section of your account. You can find the following info for each request:    1. date and time - timestamp of the request.    2. endpoint url - where the webhook was sent.    3. event - what triggered the webhook.    4. status - HTTP status or curl error code.    5. attempt - how many times we tried to send this request.    6. response size - size of the response from your server.    7. details - you can check the response body if it was sent. 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Resource(object):
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
        'total_files': 'int',
        'resources': 'list[ResourceProperty]',
        'inherited_shares': 'list[Share]',
        'inherited_notifications': 'list[Notification]',
        'inherited_direct_files': 'list[DirectFile]'
    }

    attribute_map = {
        'total_files': 'totalFiles',
        'resources': 'resources',
        'inherited_shares': 'inheritedShares',
        'inherited_notifications': 'inheritedNotifications',
        'inherited_direct_files': 'inheritedDirectFiles'
    }

    def __init__(self, total_files=None, resources=None, inherited_shares=None, inherited_notifications=None, inherited_direct_files=None):
        """
        Resource - a model defined in Swagger
        """

        self._total_files = None
        self._resources = None
        self._inherited_shares = None
        self._inherited_notifications = None
        self._inherited_direct_files = None

        if total_files is not None:
          self.total_files = total_files
        if resources is not None:
          self.resources = resources
        if inherited_shares is not None:
          self.inherited_shares = inherited_shares
        if inherited_notifications is not None:
          self.inherited_notifications = inherited_notifications
        if inherited_direct_files is not None:
          self.inherited_direct_files = inherited_direct_files

    @property
    def total_files(self):
        """
        Gets the total_files of this Resource.
        Total amount of files and folders in resource.

        :return: The total_files of this Resource.
        :rtype: int
        """
        return self._total_files

    @total_files.setter
    def total_files(self, total_files):
        """
        Sets the total_files of this Resource.
        Total amount of files and folders in resource.

        :param total_files: The total_files of this Resource.
        :type: int
        """

        self._total_files = total_files

    @property
    def resources(self):
        """
        Gets the resources of this Resource.
        Array of resources inside given resource path.

        :return: The resources of this Resource.
        :rtype: list[ResourceProperty]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this Resource.
        Array of resources inside given resource path.

        :param resources: The resources of this Resource.
        :type: list[ResourceProperty]
        """

        self._resources = resources

    @property
    def inherited_shares(self):
        """
        Gets the inherited_shares of this Resource.
        Array of all shares inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :return: The inherited_shares of this Resource.
        :rtype: list[Share]
        """
        return self._inherited_shares

    @inherited_shares.setter
    def inherited_shares(self, inherited_shares):
        """
        Sets the inherited_shares of this Resource.
        Array of all shares inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :param inherited_shares: The inherited_shares of this Resource.
        :type: list[Share]
        """

        self._inherited_shares = inherited_shares

    @property
    def inherited_notifications(self):
        """
        Gets the inherited_notifications of this Resource.
        Array of all notifications inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :return: The inherited_notifications of this Resource.
        :rtype: list[Notification]
        """
        return self._inherited_notifications

    @inherited_notifications.setter
    def inherited_notifications(self, inherited_notifications):
        """
        Sets the inherited_notifications of this Resource.
        Array of all notifications inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :param inherited_notifications: The inherited_notifications of this Resource.
        :type: list[Notification]
        """

        self._inherited_notifications = inherited_notifications

    @property
    def inherited_direct_files(self):
        """
        Gets the inherited_direct_files of this Resource.
        Array of all direct file objects inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :return: The inherited_direct_files of this Resource.
        :rtype: list[DirectFile]
        """
        return self._inherited_direct_files

    @inherited_direct_files.setter
    def inherited_direct_files(self, inherited_direct_files):
        """
        Sets the inherited_direct_files of this Resource.
        Array of all direct file objects inside the given resource. Property not emtpy only if `detailed` param was set to `true`.

        :param inherited_direct_files: The inherited_direct_files of this Resource.
        :type: list[DirectFile]
        """

        self._inherited_direct_files = inherited_direct_files

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
