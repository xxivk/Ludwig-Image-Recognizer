
![Character Illustration](image_for_md_files/characters_illustration.png)




ludwig train --dataset simpsons.csv --config config.yaml 
             --output_directory results

ludwig train --config config.yaml

ludwig preprocess --config config.yaml --output_directory dataset


ludwig preprocess --dataset image_data.csv  --preprocessing_config preprocessing_config.yaml
ludwig preprocess --config preprocessing_config.yaml --debug

ludwig preprocess --dataset simpsons_dataset --preprocessing_config simpsons_dataset\preprocessing_config.yaml 

ludwig preprocess --preprocessing_config simpsons_dataset\preprocessing_config.yaml --dataset simpsons_dataset



ludwig predict --model_path results\experiment_run_2\model  --dataset test.csv --output_directory results\prediction