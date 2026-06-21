"""
Base Health Data Provider

Defines common structure for all health sources.
"""


from abc import ABC, abstractmethod



class HealthProvider(ABC):


    @abstractmethod
    async def get_health_data(self):

        pass