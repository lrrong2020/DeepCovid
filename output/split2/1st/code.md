```
!python ResNet18_train.py \
--dataset_path /home/jupyter/dataset/covid/covid \
--output_path /home/jupyter/source_code/DeepCovid/output/split2/1st \
--tb_path /home/jupyter/source_code/DeepCovid/tensorboard/split2/1st \
--batch_size 20 \
--epoch 100 \
--num_workers 4 \
--learning_rate 0.0001


Training complete in 20m 44s
Best val Acc= 0.860 at Epoch: 25
total_time tranfer learning= 1248.8056945800781
```