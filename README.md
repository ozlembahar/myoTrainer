# myoTrainer: Fine-Tuning Cellpose-SAM for Disease-Aware Segmentation of Human Skeletal Muscle Cells

## Training

Cellpose-SAM model was fine-tuned using the *train_seg* function
provided by the Cellpose developers (1). The model was trained using Cellpose
library version 4.0.7 with a default learning rate of 1 × 10⁻⁵ and the
default learning rate scheduler.

```from cellpose import io, models, train
model = models.CellposeModel(gpu=True, pretrained_model="cpsam")
model_path = train.train_seg(model.net,
                            train_data=images, train_labels=labels,
                            test_data=test_images, test_labels=test_labels,
                            weight_decay=0.1, learning_rate=1e-5,
                            n_epochs=100, model_name="new_model")``` 

## Training and Test Data

The internally generated datasets include:

- Training data:`Muscle_training_images` and `Muscle_training_masks` 
- Test data:`Muscle_test_images` and `Muscle_test_masks`

## Validation

The Metrics package implemented in the Cellpose library was used for
performance evaluation. Segmentation performance was assessed by
matching each predicted mask to the most similar ground-truth mask using
the intersection over union (IoU) metric. Performance of the model was evaluated
across IoU thresholds ranging from 0.5 to 1.0 on the Muscle, Cellpose and TissueNet test sets.

## Citation

1- Pachitariu, M., Rariden, M., & Stringer, C. (2025). Cellpose-SAM: superhuman generalization for cellular segmentation. bioRxiv.

