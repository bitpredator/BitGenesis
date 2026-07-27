from __future__ import annotations


from bitgenesis.runtime.service_descriptor import (
    ServiceDescriptor,
)



class ServiceRegistry:
    """
    Runtime service discovery registry.

    Responsibilities:

    - store service descriptors
    - discover services
    - lookup services by name
    """



    def __init__(self):

        self._services: dict[str, ServiceDescriptor] = {}



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service,
        name: str | None = None,
        metadata: dict | None = None,
    ) -> ServiceDescriptor:
        """
        Register a runtime service.
        """


        service_name = (
            name
            or type(service).__name__
        )


        descriptor = ServiceDescriptor(
            name=service_name,
            service=service,
            metadata=metadata,
        )


        self._services[service_name] = (
            descriptor
        )


        return descriptor



    def unregister(
        self,
        name: str,
    ) -> bool:
        """
        Remove a service.
        """


        if name not in self._services:

            return False


        del self._services[name]

        return True



    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    def discover(
        self,
        name: str,
    ) -> ServiceDescriptor | None:
        """
        Find service by name.
        """

        return self._services.get(
            name
        )



    def find_by_metadata(
        self,
        key: str,
        value,
    ) -> list[ServiceDescriptor]:
        """
        Find services matching metadata.
        """


        results = []


        for descriptor in self._services.values():

            if descriptor.get(key) == value:

                results.append(
                    descriptor
                )


        return results



    # --------------------------------------------------
    # Access
    # --------------------------------------------------

    def all(
        self,
    ) -> list[ServiceDescriptor]:
        """
        Return all registered services.
        """

        return list(
            self._services.values()
        )



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check if service exists.
        """

        return name in self._services



    def clear(
        self,
    ):
        """
        Remove all services.
        """

        self._services.clear()



    def __len__(
        self,
    ) -> int:

        return len(
            self._services
        )