from __future__ import annotations
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
    from .....models.label import Label
    from .item.with_label_item_request_builder import WithLabelItemRequestBuilder

class LabelsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/schema/{id-id}/labels
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LabelsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/schema/{id%2Did}/labels", path_parameters)
    
    def by_label_id(self,label_id: int) -> WithLabelItemRequestBuilder:
        """
        Gets an item from the raw_client.api.schema.item.labels.item collection
        param label_id: Label ID
        Returns: WithLabelItemRequestBuilder
        """
        if not label_id:
            raise TypeError("label_id cannot be null.")
        from .item.with_label_item_request_builder import WithLabelItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["labelId"] = label_id
        return WithLabelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[List[Label]]:
        """
        Retrieve list of Labels for a Schema by Schema ID
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[List[Label]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.label import Label

        return await self.request_adapter.send_collection_async(request_info, Label, None)
    
    async def post(self,body: Optional[Label] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[int]:
        """
        Save new or update existing Label for a Schema
        param body: A Label is a core component of Horreum, defining which components of the JSON document are part of a KPI and how the metric values are calculated
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve list of Labels for a Schema by Schema ID
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[Label] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Save new or update existing Label for a Schema
        param body: A Label is a core component of Horreum, defining which components of the JSON document are part of a KPI and how the metric values are calculated
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> LabelsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LabelsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return LabelsRequestBuilder(self.request_adapter, raw_url)
    

