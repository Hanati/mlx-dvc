import pandas as pd
import numpy as np
import click
import os

def df2xy(infile,n=5):
    n=n+1
    df=pd.read_csv(infile,index_col=0)
    xy=[]
    for i in range(len(df)-n):
        xy.append(df.iloc[i:(i+n)].unstack().values)
    return np.array(xy)

@click.command()
@click.option('--input_dir',type=click.Path())
@click.option('--output_dir',type=click.Path())
@click.option('--step',default=5,type=int)
def run_main(input_dir,output_dir,step):
    infiles=os.listdir(input_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for infile in infiles:
        np_xy=df2xy(input_dir+'/'+infile,step)
        outfile=output_dir+'/'+infile.split('.')[0]+'.npy'
        np.save(outfile,np_xy)

if __name__=='__main__':
    run_main()
