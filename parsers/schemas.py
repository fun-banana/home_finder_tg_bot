from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class ListingDTO:
    source_id: str              # Post ID
    source: str                 # 'facebook' | 'yad2'
    url: str                    # Post url
    raw_text: str               # Raw post text
    price: Optional[int]        # Price in NIS
    rooms: Optional[float]      # Amount of rooms
    location: Optional[str]     # Street, city
    images: List[str]           # Url to images
    entrance_at: Optional[str]  # Entrance date
    published_at: datetime      # Time of publishing 