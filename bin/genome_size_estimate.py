#!/usr/bin/python
import sys,os,string
import argparse

def ParseArgs():
	USAGE = """\
	Script to calculate genome size from kmer spectrum. 
	
	"""
	parser = argparse.ArgumentParser(description=USAGE)
	parser.add_argument("-pktr",type=str,\
	help="file containing the peak and trough numbers")
	parser.add_argument("-hist",type=str,\
	help="fof with paths to files containig the histogram columns ")
	
	args = parser.parse_args()
	return args 

def calculate_genome_size(pktr,hist):
	fin = open(pktr,'r').readlines()
	hist_fin = open(hist,'r').readlines()
	dict_hist = {}

	for his in hist_fin:
		suf = his.split('/')[::-1][0].split('_')[0].strip()
		dict_hist[suf] = his #suffix: path of hist 

	for lines in fin:
		suffix,peak,trough,kmer_tot = lines.split()
		#print suffix,peak,trough,kmer_tot
		if peak != 'n/a' or trough != 'n/a':
			path_hist = dict_hist[suffix].strip()
			error_kmer = open(path_hist).readlines()[0:int(trough)]
			err_kmer_tot = 0 
			for i in error_kmer: err_kmer_tot += int(i.split()[1].strip())
			genome_size = (int(kmer_tot)-err_kmer_tot)/float(peak)	
			print suffix,":",float(genome_size/1000000)," mb"


if __name__ == '__main__':
	args = ParseArgs()
	calculate_genome_size(args.pktr,args.hist)	
		
