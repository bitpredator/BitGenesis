from __future__ import annotations


class KernelError(Exception):
    """
    Base exception for all Kernel-related errors.
    """


class ServiceError(KernelError):
    """
    Base exception for service management errors.
    """


class ServiceNotFoundError(ServiceError, LookupError):
    """
    Raised when a required service cannot be found.
    """


class ServiceAlreadyRegisteredError(ServiceError):
    """
    Raised when attempting to register a service that already exists.
    """


class ServiceDependencyError(ServiceError):
    """
    Raised when a service dependency cannot be resolved.
    """


class ServiceLifecycleError(ServiceError):
    """
    Raised when a service cannot transition between lifecycle states.
    """