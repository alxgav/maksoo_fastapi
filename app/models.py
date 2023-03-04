from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

import pytz

warsaw = pytz.timezone('Europe/Warsaw')

class SportData(BaseModel):
    id: str
    title: str
    description: str
    url: str
    img_url: str
    start: str
    end: str
    stream: str


    @validator('img_url')
    def validate_img_url(cls, value: Optional[str]) -> Optional[str]:
        return ''.join(value.split('?')[0])
    
    @validator('start', 'end')
    def validate_date(cls, value: Optional[str]) -> Optional[str]:
        stop = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        stop = pytz.utc.localize(stop, is_dst=None).astimezone(warsaw)
        return datetime.strftime(stop, "%Y-%m-%dT%H:%M:%S.%fZ").replace('.000', '.')