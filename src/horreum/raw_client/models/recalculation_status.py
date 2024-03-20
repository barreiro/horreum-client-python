from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RecalculationStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Total number of generated datasets
    datasets: Optional[int] = None
    # Total number of completed recalculations
    finished: Optional[int] = None
    # Recalculation timestamp
    timestamp: Optional[int] = None
    # Total number of Runs being recalculated
    total_runs: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecalculationStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecalculationStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecalculationStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "datasets": lambda n : setattr(self, 'datasets', n.get_int_value()),
            "finished": lambda n : setattr(self, 'finished', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
            "totalRuns": lambda n : setattr(self, 'total_runs', n.get_int_value()),
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
        writer.write_int_value("datasets", self.datasets)
        writer.write_int_value("finished", self.finished)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_int_value("totalRuns", self.total_runs)
        writer.write_additional_data_value(self.additional_data)
    

