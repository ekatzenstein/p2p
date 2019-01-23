import pytest


from pandastoproduction.p2p import (publish, Page)


def test_publish():
    publish()

    with pytest.raises(TypeError):
        publish('x')

    with pytest.raises(TypeError):
        publish(['x'])

    with pytest.raises(TypeError):
        publish([Page(), 'x'])

    with pytest.raises(TypeError):
        publish(Page())

    publish([Page()])
