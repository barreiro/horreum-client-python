from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SchemaUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Does schema have a JSON validation schema defined?
    has_json_schema: Optional[bool] = None
    # Schema unique ID
    id: Optional[int] = None
    # Ordinal position of schema usage in Run/Dataset
    key: Optional[str] = None
    # Schema name
    name: Optional[str] = None
    # Source of schema usage, 0 is data, 1 is metadata. DataSets always use 0
    source: Optional[int] = None
    # Location of Schema Usage, 0 for Run, 1 for Dataset
    type: Optional[int] = None
    # Schema name
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SchemaUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SchemaUsage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SchemaUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "hasJsonSchema": lambda n : setattr(self, 'has_json_schema', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_bool_value("hasJsonSchema", self.has_json_schema)
        writer.write_int_value("id", self.id)
        writer.write_str_value("key", self.key)
        writer.write_str_value("name", self.name)
        writer.write_int_value("source", self.source)
        writer.write_int_value("type", self.type)
        writer.write_str_value("uri", self.uri)
        writer.write_additional_data_value(self.additional_data)
    

