import sys, re

###
### Parse options
###
from optparse import OptionParser
usage="%prog [options] <in-srt> <out-text>"
parser = OptionParser(usage)
# Required,
parser.add_option('--utt-id', dest='utt_id', type='str', default="single_utterance_id",
                   help='single utterance id for verify diff sentence [default: %default]');


(o,args) = parser.parse_args()
if len(args) != 2 :
    parser.print_help()
    sys.exit(1)

in_srt = args[0]
out_text = args[1]


print("Loading [ %s ] ... " %(str(in_srt)))
text = ""
ifp = open(in_srt, 'r')
caption_flag = 0
for line in ifp : 
    line_list = re.split(' |\n', line)
    #line_list = [ x for x in line_list if x != '' ]
    if len(line_list) == 4 : 
        if line_list[1] == "-->" : 
            caption_flag = 1
        else : 
            if caption_flag == 1 : 
                for t in line_list : 
                    text += t + " "
                caption_flag = 0
    else : 
        if caption_flag == 1 : 
            for t in line_list : 
                text += t + " "
            caption_flag = 0
ifp.close()

print("Writing [ %s ] ... " %(str(out_text)))
ofp = open(out_text, 'w')
ofp.write(str(o.utt_id)+" "+str(text)+"\n")
ofp.close()
