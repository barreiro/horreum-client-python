from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dataset_summary import DatasetSummary

@dataclass
class DatasetList(AdditionalDataHolder, Parsable):
    """
    Result containing a subset of Dataset Summaries and the total count of available. Used in paginated tables
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # List of Dataset Summaries. This is often a subset of total available.
    datasets: Optional[List[DatasetSummary]] = None
    # Total number of Dataset Summaries available
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DatasetList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DatasetList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DatasetList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .dataset_summary import DatasetSummary

        from .dataset_summary import DatasetSummary

        fields: Dict[str, Callable[[Any], None]] = {
            "datasets": lambda n : setattr(self, 'datasets', n.get_collection_of_object_values(DatasetSummary)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("datasets", self.datasets)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

