import pytest

from djikstra import get_total_cost

@pytest.fixture
def graph_one():
    graph = {}

    graph['start'] = {}
    graph['start']['a'] = 2
    graph['start']['b'] = 5
    
    graph['a'] = {}
    graph['a']['b'] = 8
    graph['a']['d'] = 7
    
    graph['b'] = {}
    graph['b']['c'] = 4
    graph['b']['d'] = 2

    graph['d'] = {}
    graph['d']['end'] = 1
    
    graph['c'] = {}
    graph['c']['d'] = 6
    graph['c']['end'] = 3

    graph['end'] = {}

    return graph

def test_djikstra(graph_one):
    result = get_total_cost(graph_one)

    assert result == 8