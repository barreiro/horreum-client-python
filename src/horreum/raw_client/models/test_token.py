from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TestToken(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Token description
    description: Optional[str] = None
    # Unique Token id
    id: Optional[int] = None
    # The permissions property
    permissions: Optional[int] = None
    # Test ID to apply Token
    test_id: Optional[int] = None
    # Test value
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TestToken:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TestToken
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TestToken()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_int_value()),
            "testId": lambda n : setattr(self, 'test_id', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_int_value("id", self.id)
        writer.write_int_value("permissions", self.permissions)
        writer.write_int_value("testId", self.test_id)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

