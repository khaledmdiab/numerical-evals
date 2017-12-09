import os
import sys
import random
from simulation.data import Data
from simulation.utils import marshal_load_obj

if len(sys.argv) > 1:
    DATA_FILE = sys.argv[1]
    LOG_DIR = sys.argv[2]

    _TEMP = DATA_FILE.split('.')
    CLOUD_PARAMS = _TEMP[-2].split('_')
    NUM_PODS = int(CLOUD_PARAMS[0])
    NUM_LEAFS_PER_POD = int(CLOUD_PARAMS[1])
    NUM_HOSTS_PER_LEAF = int(CLOUD_PARAMS[2])
    NUM_TENANTS = int(CLOUD_PARAMS[4])
    SEED = int(CLOUD_PARAMS[13])

    OPTIMIZER_PARAMS = _TEMP[-1].split('_')
    NUM_BITMAPS = int(OPTIMIZER_PARAMS[1])
    NODE_TYPE = OPTIMIZER_PARAMS[7]
elif True:
    DATA_FILE = 'output/optimizer..'
    LOG_DIR = 'output/logs'

    CLOUD_PARAMS = []
    NUM_PODS = 11
    NUM_LEAFS_PER_POD = 48
    NUM_HOSTS_PER_LEAF = 48
    NUM_TENANTS = 30
    SEED = 0

    OPTIMIZER_PARAMS = []
    NUM_BITMAPS = 3
    NODE_TYPE = 'leafs'
else:
    raise (Exception('invalid parameters'))

random.seed(SEED)

log_dir = LOG_DIR + "/" + "_".join(CLOUD_PARAMS) + "." + "_".join(OPTIMIZER_PARAMS)

# if os.path.isdir(log_dir):
#     print('%s, already exists.' % log_dir)
#     exit(0)

os.system('mkdir -p %s' % log_dir)

data = marshal_load_obj(DATA_FILE)

data = Data(data, num_tenants=NUM_TENANTS, num_pods=NUM_PODS, num_leafs_per_pod=NUM_LEAFS_PER_POD,
            num_hosts_per_leaf=NUM_HOSTS_PER_LEAF, num_bitmaps=NUM_BITMAPS, log_dir=log_dir, node_type=NODE_TYPE)

data.log_stats(log_cloud=False)
