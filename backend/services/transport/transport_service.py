"""
Transport Service
Integrates with taxi (Uber, Bolt) and Norwegian public transport APIs (Entur, Ruter, Skyss).
Books transport timed to meetings and calculates departure times.
"""
from typing import Literal

TransportProvider = Literal["uber", "bolt", "entur", "ruter", "skyss"]


class TransportService:
    def get_public_transport_routes(
        self,
        origin: str,
        destination: str,
        arrival_time: str,
        provider: TransportProvider = "entur",
    ) -> list[dict]:
        """
        Fetch public transport routes from Entur/Ruter/Skyss.
        Returns a list of route options with departure times.
        """
        # TODO: Integrate with Entur Journey Planner API
        raise NotImplementedError

    def book_taxi(
        self,
        origin: str,
        destination: str,
        pickup_time: str,
        provider: TransportProvider = "uber",
    ) -> dict:
        """
        Book a taxi ride via Uber or Bolt API.
        Returns: booking_id, driver_info, estimated_arrival, price
        """
        # TODO: Integrate with Uber and Bolt APIs
        raise NotImplementedError

    def calculate_departure_time(
        self,
        user_location: str,
        meeting_location: str,
        meeting_start: str,
        buffer_minutes: int = 10,
    ) -> str:
        """
        Calculate when the user needs to leave to arrive on time.
        Accounts for travel time + buffer.
        """
        # TODO: Use routing API to calculate travel time
        raise NotImplementedError

    def get_organized_transport(self, group_size: int, route: dict) -> list[dict]:
        """
        Find company shuttles or shared group transport options.
        """
        # TODO: Implement organized group transport booking
        raise NotImplementedError
