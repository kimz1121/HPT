import zarr

train = zarr.open("./data/zarr_mujoco_metaworld_task1_resnet_traj100", mode='r')
print(train.tree())
train = zarr.open("./data/zarr_mujoco_metaworld_task20_resnet_traj200", mode='r')
print(train.tree())