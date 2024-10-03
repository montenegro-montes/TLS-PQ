#!/bin/bash

python3 procesado.py Level1.result.txt 
python3 procesado.py Level3.result.txt 
python3 procesado.py Level5.result.txt 

python3 transformCSV.py Level1.result.csv 
python3 transformCSV.py Level3.result.csv 
python3 transformCSV.py Level5.result.csv 

python3 plot.py Level1.result.processed.csv 
python3 plot.py Level3.result.processed.csv 
python3 plot.py Level5.result.processed.csv 
