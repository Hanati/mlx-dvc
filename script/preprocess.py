import pandas as pd
import numpy as np
import click
import os

def norm(df,rn=4,dn=5):
    results=[]
    for i in range(1,dn):
        results.append(df.apply(np.log).rolling(rn).mean().diff(i))
    return results

@click.command()
@click.option('--input_file',type=click.Path())
@click.option('--output_dir',type=click.Path())
def run_main(input_file,output_dir):
    input_path, input_name = os.path.split(input_file)
    print (input_name)
    df=pd.read_csv(input_file,index_col=0)
    results=norm(df,4,5)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(len(results)):
        results[i].to_csv(output_dir+'/'+input_name.split(".")[0]+"_"+str(i+1)+'.csv')

if __name__=='__main__':
    run_main()
