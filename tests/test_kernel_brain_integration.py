from bitgenesis.kernel.kernel import Kernel
from bitgenesis.core.brain import Brain


def test_kernel_builds_brain():

    kernel = Kernel()

    brain = kernel.bootstrap()

    assert isinstance(
        brain,
        Brain
    )


def test_kernel_exposes_brain():

    kernel = Kernel()

    kernel.start()

    assert kernel.get_brain() is not None