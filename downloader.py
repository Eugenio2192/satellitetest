from eodag.api.core import EODataAccessGateway
from eodag.utils.logging import setup_logging
from eodag.utils import ProgressCallback
import os
import json
import pprint
import tqdm
setup_logging(verbose=1)
WORKSPACE="eodag_workspace"
DESCRIPTORS_PATH = r"products/stuttgart21.json"
PROVIDER = "sobloo"

dag = EODataAccessGateway('eodag.yml')
dag.set_preferred_provider(PROVIDER)

def loadDescriptorJson(path):
    with open(path, "r") as json_file:
        data = json.load(json_file)
    return data


def createDescriptors(data):
    descriptorDict = {}
    for type in data["PRODUCT_TYPES"]:
        descriptorDict[type] = {"productType": data["PRODUCT_TYPES"][type]}
        for prop in data:
            if prop != "PRODUCT_TYPES":
                descriptorDict[type][prop] = data[prop]
    return descriptorDict


def downloadProducts(descDict):
    products, _ = dag.search(**descDict)
    path = dag.download(products[0], progress_callback=ProgressCallback())


def main():
    if not os.path.isdir(WORKSPACE):
        os.mkdir(WORKSPACE)
    data = loadDescriptorJson(DESCRIPTORS_PATH)
    descriptorDict = createDescriptors(data)
    for type in tqdm.tqdm(descriptorDict):
        downloadProducts(descriptorDict[type])


if __name__ == "__main__":
    # pp = pprint.PrettyPrinter(indent=4)
    # data = loadDescriptorJson(DESCRIPTORS_PATH)
    # descriptorDict = createDescriptors(data)
    # pp.pprint(descriptorDict["NO2"])
    main()