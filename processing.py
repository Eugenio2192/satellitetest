import xarray as xr

if __name__ == "__main__":
    with xr.open_dataset("eodag_workspace/S5P_OFFL_L2__AER_AI_20180630T112732_20180630T130902_03690_01_010002_20180706T105254.nc", group="PRODUCT") as file:
        dataset = file

    print(dataset)