#!/usr/bin/env python
# coding: utf-8
import sys
import os
import pandas as pd
import geopandas as gpd
from utils import *


def main(config):
	print("blablabla")
	incoming_data_path = config['paths']['incoming_data']
	processed_data_path = config['paths']['data']
	print(incoming_data_path)
	road_edges = gpd.read_file(os.path.join(incoming_data_path,"hotosm_ken_roads_lines_gpkg.gpkg"))									
	road_edges = road_edges[road_edges["highway"].isin(["trunk","trunk_link","primary","primary_link","secondary","secondary_link"])]
	road_edges.to_file(os.path.join(incoming_data_path,'sample_roads.gpkg'))
	
	# road_edges = gpd.read_file(os.path.join(incoming_data_path, "roads","sample_roads.gpkg"),layer="roads") 
	# print (road_edges)
	# network = create_network_from_nodes_and_edges(None,road_edges,"roade")
	# edges = network.edges
	# nodes = network.nodes
	# print (edges)
	# print (nodes)
	# edges, nodes = components(edges,nodes,"node_id")
	# edges.to_file(os.path.join(incoming_data_path,"roads","roads_network.gpkg"),layer="edges",driver="GPKG")
	# nodes.to_file(os.path.join(incoming_data_path,"roads","roads_network.gpkg"),layer="nodes",driver="GPKG")
	
if __name__ == '__main__':
	CONFIG = load_config() 
	main(CONFIG)