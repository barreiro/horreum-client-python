from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.test import Test
    from .add_token.add_token_request_builder import AddTokenRequestBuilder
    from .export.export_request_builder import ExportRequestBuilder
    from .fingerprint.fingerprint_request_builder import FingerprintRequestBuilder
    from .label_values.label_values_request_builder import LabelValuesRequestBuilder
    from .move.move_request_builder import MoveRequestBuilder
    from .notifications.notifications_request_builder import NotificationsRequestBuilder
    from .recalculate.recalculate_request_builder import RecalculateRequestBuilder
    from .revoke_token.revoke_token_request_builder import RevokeTokenRequestBuilder
    from .tokens.tokens_request_builder import TokensRequestBuilder
    from .transformers.transformers_request_builder import TransformersRequestBuilder
    from .update_access.update_access_request_builder import UpdateAccessRequestBuilder

class TestItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/test/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TestItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/test/{id}{?token*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete a Test by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[Test]:
        """
        Retrieve a test by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Test]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.test import Test

        return await self.request_adapter.send_async(request_info, Test, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete a Test by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/test/{id}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a test by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TestItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TestItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TestItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_token(self) -> AddTokenRequestBuilder:
        """
        The addToken property
        """
        from .add_token.add_token_request_builder import AddTokenRequestBuilder

        return AddTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export(self) -> ExportRequestBuilder:
        """
        The export property
        """
        from .export.export_request_builder import ExportRequestBuilder

        return ExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fingerprint(self) -> FingerprintRequestBuilder:
        """
        The fingerprint property
        """
        from .fingerprint.fingerprint_request_builder import FingerprintRequestBuilder

        return FingerprintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def label_values(self) -> LabelValuesRequestBuilder:
        """
        The labelValues property
        """
        from .label_values.label_values_request_builder import LabelValuesRequestBuilder

        return LabelValuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> MoveRequestBuilder:
        """
        The move property
        """
        from .move.move_request_builder import MoveRequestBuilder

        return MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notifications(self) -> NotificationsRequestBuilder:
        """
        The notifications property
        """
        from .notifications.notifications_request_builder import NotificationsRequestBuilder

        return NotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recalculate(self) -> RecalculateRequestBuilder:
        """
        The recalculate property
        """
        from .recalculate.recalculate_request_builder import RecalculateRequestBuilder

        return RecalculateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_token(self) -> RevokeTokenRequestBuilder:
        """
        The revokeToken property
        """
        from .revoke_token.revoke_token_request_builder import RevokeTokenRequestBuilder

        return RevokeTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tokens(self) -> TokensRequestBuilder:
        """
        The tokens property
        """
        from .tokens.tokens_request_builder import TokensRequestBuilder

        return TokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transformers(self) -> TransformersRequestBuilder:
        """
        The transformers property
        """
        from .transformers.transformers_request_builder import TransformersRequestBuilder

        return TransformersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_access(self) -> UpdateAccessRequestBuilder:
        """
        The updateAccess property
        """
        from .update_access.update_access_request_builder import UpdateAccessRequestBuilder

        return UpdateAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TestItemRequestBuilderGetQueryParameters():
        """
        Retrieve a test by id
        """
        token: Optional[str] = None

    

