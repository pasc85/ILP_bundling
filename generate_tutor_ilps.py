# the scripts generates the ILP records as .pdf documents by default
# this requires the python package 'pdfkit'
# if you don't have that package, .html files will be generated instead
# if .html files are generated but you would prefer .pdf, install the package
# following the two steps on
# https://pypi.org/project/pdfkit/
# if you have the package and .pdf files are generated, but you prefer .html,
# set the variable 'output_format' below (after the imports) equal to 'html'


# import packages, create folder for output
import os
import sys
import shutil
from distutils.dir_util import copy_tree

output_format = 'pdf'

if output_format == 'pdf':
    try:
        import pdfkit
    except ImportError:
        output_format = 'html'
        print('A Python package required for generating .pdf documents')
        print('is not installed. Generating .html files instead.\n')
if os.path.isdir('./ILPs_by_tutors'):
    shutil.rmtree('./ILPs_by_tutors')
os.mkdir('./ILPs_by_tutors')
if not output_format == 'pdf':
    fromDirectory = './all_ILPs_files'
    toDirectory = './ILPs_by_tutors/all_ILPs_files'
    copy_tree(fromDirectory, toDirectory)


# subroutine that creates dictionary of tutors
ts = {}
groups = open('grouped_list.txt', 'r')
sl = []  # student list
for line in groups:
    if ':' in line:
        temp = line.strip()
        temp = temp.rstrip(':')
        if temp.startswith('Prof '):
            temp = temp.lstrip('Prof ')
        if temp.startswith('Dr '):
            temp = temp.lstrip('Dr ')
        tn = temp.replace(' ', '_')
    if ':' not in line and not line.strip() == '':
        sn = line.split(',')[-1].strip()
        sl.append(sn)
    if line.strip() == '':
        if sl:
            ts.update({tn: sl})
            sl = []


# create individual output files for each tutor
for t in ts.keys():
    # make copy of the html file with non-tutee records missing
    all_ilps = open('all_ILPs.html', 'r')
    tutor_ilps = open('tutor_ILPs.html', 'w')
    orig_stdout = sys.stdout
    sys.stdout = tutor_ilps
    p = True  # boolean that decides whether lines are printed
    for line in all_ilps:
        if line.startswith('<div style="page-break-before'):
            if p is False:  # close file properly in case last stu not written
                print('--->')
                print('\n\n')
                print('</div>')
                print('\n')
                p = True
        if line.startswith('#STUDENT='):
            temp_l = ts[t]
            contains = False  # line contains one of curr tutor's stus
            for k in range(len(temp_l)):
                if temp_l[k] in line:
                    contains = True
            if contains:
                p = True
            else:
                p = False
        if p:
            if 'Report' in line:
                print(line.replace('by', 'for ' + t + ' by'))
            else:
                print(line)
    sys.stdout = orig_stdout
    all_ilps.close()
    tutor_ilps.close()
    # output
    if output_format == 'pdf':
        pdfkit.from_url('./tutor_ILPs.html', './ILPs_by_tutors/' + t
                        + '_ILPs.pdf')
    else:
        shutil.copyfile('./tutor_ILPs.html', './ILPs_by_tutors/' + t
                        + '_ILPs.html')
os.remove('./tutor_ILPs.html')
