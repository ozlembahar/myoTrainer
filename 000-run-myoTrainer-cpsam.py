from cellpose import models, io
from pathlib import Path

# Run myoTrainer or cpsam by modifying model_name in line 19 to myoTrainer or cpsam.
project_dir = Path.cwd()

# download myoTrainer: https://huggingface.co/ozlembahar/myoTrainer and place under myoTrainer/models directory 

image_dir = project_dir / "example_img" / "images-to-segment"
output_dir = project_dir / "example_img" / "segmented-images"

output_dir.mkdir(parents=True, exist_ok=True)

model_choices = {
    "cpsam": "cpsam",
    "myoTrainer": str(project_dir / "models" / "myoTrainer"),
}

model_name = "cpsam"   # your model of choise: myoTrainer or cpsam
pretrained_model = model_choices[model_name]

print("Using model:", pretrained_model)

model = models.CellposeModel(
    gpu=True,
    pretrained_model=pretrained_model
)


for image_path in image_dir.glob("*.tif*"):
    image = io.imread(image_path)

    masks, flows, styles = model.eval(
        image,
        diameter=None
    )

    io.save_masks(
        image,
        masks,
        flows,
        str(image_path),
        png=False,
        tif=True,
        savedir=str(output_dir),
        suffix=f"_{model_name}_masks"
    )