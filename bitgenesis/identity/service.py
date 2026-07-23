from __future__ import annotations

from bitgenesis.kernel.service import KernelService
from bitgenesis.identity.profile import IdentityProfile
from bitgenesis.identity.manager import IdentityManager


class IdentityService(KernelService):

    version = "0.2.0"


    def __init__(
        self,
        event_bus=None,
        identity_store=None,
        **kwargs,
    ):

        super().__init__(
            "identity"
        )

        self.event_bus = event_bus

        self.identity_store = identity_store

        self.manager = IdentityManager()

        self.identity = IdentityProfile(
            name="BitGenesis",
            creator="Bitpredator",
            project="BitGenesis",
            version=self.version,
            description=(
                "Artificial Cognitive Architecture "
                "built from scratch."
            ),
        )

        self.running = False



    def start(self):

        self.running = True


        if self.identity_store and hasattr(
            self.identity_store,
            "load"
        ):

            loaded = self.identity_store.load()

            if isinstance(
                loaded,
                dict
            ):

                self.identity = IdentityProfile(
                    **loaded
                )

        if self.event_bus:

            from bitgenesis.events.event import Event
            from bitgenesis.events.enums import (
                EventCategory,
                EventType,
            )

            self.event_bus.publish(
                Event(
                    category=EventCategory.IDENTITY,
                    type=EventType.IDENTITY_INITIALIZED,
                    source="identity_service",
                    payload={
                        "service": self.name,
                        "identity": self.identity.name,
                    },
                )
            )



    def stop(self):

        if self.identity_store and hasattr(
            self.identity_store,
            "save"
        ):

            if hasattr(
                self.identity,
                "__dict__"
            ):

                self.identity_store.save(
                    self.identity.__dict__
                )


        self.running = False



    def tick(self):

        return None



    def set(
        self,
        key,
        value
    ):

        setattr(
            self.identity,
            key,
            value
        )



    def get(
        self,
        key,
        default=None
    ):

        return getattr(
            self.identity,
            key,
            default
        )



    def metadata(self):

        return {
            "name": self.name,
            "version": self.version,
            "enabled": True,
            "type": "identity",
        }