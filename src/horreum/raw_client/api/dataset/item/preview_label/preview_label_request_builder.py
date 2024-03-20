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
    from .....models.label_preview import LabelPreview

class PreviewLabelRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/dataset/{datasetId-id}/previewLabel
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PreviewLabelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/dataset/{datasetId%2Did}/previewLabel", path_parameters)
    
    async def post(self,body: Optional[Label] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[LabelPreview]:
        """
        param body: A Label is a core component of Horreum, defining which components of the JSON document are part of a KPI and how the metric values are calculated
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LabelPreview]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.label_preview import LabelPreview

        return await self.request_adapter.send_async(request_info, LabelPreview, None)
    
    def to_post_request_information(self,body: Optional[Label] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
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
    
    def with_url(self,raw_url: Optional[str] = None) -> PreviewLabelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PreviewLabelRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PreviewLabelRequestBuilder(self.request_adapter, raw_url)
    

