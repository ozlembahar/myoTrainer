import os
from cellpose import models, io, train
import logging
from pathlib import Path


project_dir = Path.cwd()

logging.basicConfig(level=logging.INFO)

# image and mask dirs for fine-tuning cpsam
image_dir = project_dir / "example_img" / "augmented_images"
mask_dir = project_dir / "example_img" / "augmented_masks"
#output model dir
save_dir = project_dir / "models"
save_dir.mkdir(exist_ok=True)

images = []
masks = []

# load matching image-mask pairs
for image_path in sorted(image_dir.glob("*.tif")):
    mask_path = mask_dir / f"{image_path.stem}_masks.tif"

    if not mask_path.exists():
        print(f"Missing mask: {mask_path.name}")
        continue

    images.append(io.imread(image_path))
    masks.append(io.imread(mask_path))

print(f"Loaded {len(images)} image-mask pairs")

if not images:
    raise ValueError("No matching image-mask pairs found")

# fine-tune cpsam
model = models.CellposeModel(gpu=True, pretrained_model="cpsam")

# for more details on training setting: https://cellpose.readthedocs.io/en/latest/api.html
model_path = train.train_seg(
    model.net,
    train_data=images,
    train_labels=masks,
    n_epochs=100,
    rescale=False,
    normalize=False,
    save_every=5,
    save_each=True,
    model_name=f"fine-tuned-cpsam_{len(masks)}_masks",
    min_train_masks=1
)
