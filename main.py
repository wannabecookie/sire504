#!/usr/bin/env python3
from bioseq.seqMan import dnaconvert
from bioseq.pattern import SeqPattern
from bioseq.calculation import SeqCal
import argparse

def argparserLocal():
    parser = argparse.ArgumentParser(prog='myseq', description='Work with sequence')
    subparsers = parser.add_subparsers(title='commands', description='Please choose command below:',dest='command')
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action='store_true', help="Convet DNA to reverse-complementary")
    
    transcript_command = subparsers.add_parser('transcription', help = "Convert DNA->RNA")
    transcript_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transcript_command.add_argument("-r", "--revcomp", action='store_true', help="Convet DNA to reverse-complementary")
    
    translation_command = subparsers.add_parser('translation', help = "Convert DNA->Protein")
    translation_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    translation_command.add_argument("-r", "--revcomp", action='store_true', help="Convet DNA to reverse-complementary")

    enzTargetScan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTargetScan_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    enzTargetScan_command.add_argument("-e", "--enz", type=str, default=None, help="Enzyme name")
    enzTargetScan_command.add_argument("-r", "--revcomp", action='store_true', help="Convet DNA to reverse-complementary")
   
    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
        
    if getattr(args, 'revcomp', False) is True:
        seq = dnaconvert.reverseComplementSeq(seq)
    # if getattr(args, 'revcomp') is False:
    #     seq = seqMan.reverseComplementSeq(seq)
    # Input
    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", SeqCal.gcContent(seq))

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        print("Input",args.seq,"\ncountBases =", SeqCal.countBasesDict(seq))
        
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.enz is None:
            # Check if the required -e/--enz argument for this command is missing
            print("------\nError: The 'enzTargetsScan' command requires the -e or --enz argument.\n------\n")
            exit(parser.parse_args(['enzTargetsScan','-h'])) # Use 'exit()' here
        print(f"Input {args.seq} \n{args.enz} sites = {SeqPattern.enzTargetsScan(seq, args.enz)}")  
        #print("Input",args.seq,"\nenzTargetsScan =", SeqPattern.enzTargetsScan(seq))
        
    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h'])) 
        print("Input",args.seq,"\nTranscription =", dnaconvert.dna2rna(seq))
        
    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h'])) 
        print("Input",args.seq,"\nTranslation =", dnaconvert.dna2protein(seq))
    
        
        
# if __name__ == "__main__":
# #     test()
#     main()
# print(__name__)
# # if __name__ == "__main__":
# #     test()
# main()

