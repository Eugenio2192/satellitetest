import xarray as xr

if __name__ == "__main__":
    with xr.open_dataset("eodag_workspace/file.nc", group="PRODUCT") as file:
        dataset = file

    print(dataset)