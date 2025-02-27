conda create -n al_dqc python=3.8
conda activate al_dqc

conda install -c conda-forge xeus-python jupyterlab


# Install requirements
conda install -c pytorch pytorch torchvision
pip install -r requirements.txt