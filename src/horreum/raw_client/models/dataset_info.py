from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DatasetInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Dataset ID for Dataset
    id: Optional[int] = None
    # Ordinal position in ordered list
    ordinal: Optional[int] = None
    # Run ID that Dataset relates to
    run_id: Optional[int] = None
    # Test ID that Dataset relates to
    test_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DatasetInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DatasetInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DatasetInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "ordinal": lambda n : setattr(self, 'ordinal', n.get_int_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_int_value()),
            "testId": lambda n : setattr(self, 'test_id', n.get_int_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_int_value("ordinal", self.ordinal)
        writer.write_int_value("runId", self.run_id)
        writer.write_int_value("testId", self.test_id)
        writer.write_additional_data_value(self.additional_data)
    

