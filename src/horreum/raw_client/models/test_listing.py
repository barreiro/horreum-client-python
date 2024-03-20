from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .test_summary import TestSummary

@dataclass
class TestListing(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Number of tests when pagination is ignored
    count: Optional[int] = None
    # Array of Test Summaries
    tests: Optional[List[TestSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TestListing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TestListing
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TestListing()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .test_summary import TestSummary

        from .test_summary import TestSummary

        fields: Dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "tests": lambda n : setattr(self, 'tests', n.get_collection_of_object_values(TestSummary)),
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
        writer.write_int_value("count", self.count)
        writer.write_collection_of_object_values("tests", self.tests)
        writer.write_additional_data_value(self.additional_data)
    

