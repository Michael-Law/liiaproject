from django.http import HttpResponse
from .models import status
from django.template import loader


import networkx as nx
import matplotlib.pyplot as plt



# Create your views here.

def index(request):
    all_sensors = status.objects.all()
    template = loader.get_template('index.html')
    context = {
        'all_sensors': all_sensors
    }
    return HttpResponse(template.render(context, request))

def feature(request, sensor_id):
    return HttpResponse("<h2>Features for sensor id:" +str(sensor_id) +"</h2>")


def graph(request):

    G = nx.Graph()
    G.add_node("a")
    G.add_nodes_from(["b","c"])

    G.add_edge(1, 2)
    edge = ("d", "e")
    G.add_edge(*edge)
    edge = ("a", "b")
    G.add_edge(*edge)
    G.add_edges_from([("a","c"), ("c", "d"), ("a", 1), (1, "d"), ("a", 2)])

    nx.draw(G)
    plt.savefig("graph_simple_path.png") # save as png
    
    image_data = open('graph_simple_path.png', mode='r').read()
    return HttpResponse(image_data, content_type="image/png")



