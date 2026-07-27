# myoTrainer: Fine-Tuning Cellpose-SAM for Disease-Aware Segmentation of Human Skeletal Muscle Cells

## Installation and running myoTrainer

1. Clone the repository

`git clone https://github.com/ozlembahar/myoTrainer.git`

Change directory to project folder

`cd myoTrainer`

2. Create the Conda environment

Install Miniforge, then create the environment using the provided `environment.yml` file:

`conda env create -f environment.yml -n myoTrainer_env`

Activate the environment

`conda activate myoTrainer_env`

To run myoTrainer or Cellpose-SAM (cpsam)(1), follow the instructions here: *000-run-myoTrainer-cpsam.py*

`python 000-run-myoTrainer-cpsam.py`

## Training and Test Data

The internally generated datasets include:

- Training data:`Muscle_training_images` and `Muscle_training_masks` 
- Test data:`Muscle_test_images` and `Muscle_test_masks`

To generate augmented image patches from a manually annotated image, follow the workflow provided here: *010-img-augment.ipynb*

## Training

Cpsam was fine-tuned using the *train_seg* function
provided by the Cellpose developers (1). The model was trained using Cellpose
library version 4.0.7 with a default learning rate of 1 × 10⁻⁵ and the
default learning rate scheduler.

```from cellpose import io, models, train
model = models.CellposeModel(gpu=True, pretrained_model="cpsam")
model_path = train.train_seg(model.net,
                            train_data=images, train_labels=labels,
                            test_data=test_images, test_labels=test_labels,
                            weight_decay=0.1, learning_rate=1e-5,
                            n_epochs=100, model_name="new_model")
``` 

To fine-tune cpsam using the provided example image-mask pairs, run: *020-train-cpsam.py*:

`python 020-train-cpsam.py`

## Validation

The Metrics package implemented in the Cellpose library was used for
performance evaluation. Segmentation performance was assessed by
matching each predicted mask to the most similar ground-truth mask using
the intersection over union (IoU) metric. Performance of the model was evaluated
across IoU thresholds ranging from 0.5 to 1.0 on the Muscle, Cellpose (https://www.cellpose.org/dataset)(1) and TissueNet (https://datasets.deepcell.org)(2) test sets.

## Citation

1-Pachitariu, M., Rariden, M., & Stringer, C. (2025). Cellpose-SAM: superhuman generalization for cellular segmentation. bioRxiv.
2-Greenwald NF, Miller G, Moen E, Kong A, Kagel A, Dougherty T, et al. Whole-cell segmentation of tissue images with human-level performance using large-scale data annotation and deep learning. Nat Biotechnol. 2022;40:555–65. https://doi.org/10.1038/s41587-021-01094-0.
