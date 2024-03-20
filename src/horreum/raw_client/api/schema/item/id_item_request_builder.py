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
    from ....models.schema import Schema
    from .drop_token.drop_token_request_builder import DropTokenRequestBuilder
    from .export.export_request_builder import ExportRequestBuilder
    from .labels.labels_request_builder import LabelsRequestBuilder
    from .reset_token.reset_token_request_builder import ResetTokenRequestBuilder
    from .transformers.transformers_request_builder import TransformersRequestBuilder
    from .update_access.update_access_request_builder import UpdateAccessRequestBuilder

class IdItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schema/{id-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new IdItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schema/{id%2Did}{?token*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete a Schema by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[Schema]:
        """
        Retrieve Schema by ID
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Schema]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.schema import Schema

        return await self.request_adapter.send_async(request_info, Schema, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete a Schema by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/schema/{id%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve Schema by ID
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> IdItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return IdItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def drop_token(self) -> DropTokenRequestBuilder:
        """
        The dropToken property
        """
        from .drop_token.drop_token_request_builder import DropTokenRequestBuilder

        return DropTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export(self) -> ExportRequestBuilder:
        """
        The export property
        """
        from .export.export_request_builder import ExportRequestBuilder

        return ExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def labels(self) -> LabelsRequestBuilder:
        """
        The labels property
        """
        from .labels.labels_request_builder import LabelsRequestBuilder

        return LabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_token(self) -> ResetTokenRequestBuilder:
        """
        The resetToken property
        """
        from .reset_token.reset_token_request_builder import ResetTokenRequestBuilder

        return ResetTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class IdItemRequestBuilderGetQueryParameters():
        """
        Retrieve Schema by ID
        """
        # API token for authorization
        token: Optional[str] = None

    

