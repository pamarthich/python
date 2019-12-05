import boto3
import sys
import datetime
import time

profile = sys.argv[1]
env = sys.argv[2] 
release = sys.argv[3]
client = boto3.client('rds')
def list_db_clusters():
    response = client.describe_db_clusters()
    clusters = response['DBClusters']
    for clus in clusters:
          list_db_clusters.cluster = clus['DBClusterIdentifier']
          list_db_clusters.cluster_list=[] 
          list_db_clusters.cluster_list.append(list_db_clusters.cluster)
          print(list_db_clusters.cluster_list)
list_db_clusters()

def create_cluster_snapshot():
     for x in list_db_clusters.cluster_list:
       client.create_db_cluster_snapshot(DBClusterSnapshotIdentifier=x+release,DBClusterIdentifier=x)
       print("creating snapshot for cluster:"+ x)

create_cluster_snapshot()

list_1 = [sand-release, bza-stp, rpl-sand-rls, bza-cgn]
if env = sand or env = prod-aus:
     
