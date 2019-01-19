This set of scripts rearranges the full list of ILPs for a module into bundles
for each tutor.


INSTRUCTIONS
============


(1) Extract the archive file into a folder of your choice.


(2) Go to SRS, click on 'View all ILPs for a module in one document',
select the module, and click 'Run Report'. Once the report is displayed
in your browser, save that page in the folder, calling it 'all_ILPs.html'.


(3) Obtain a .txt file with the tutorial groups for the module from a
colleague with access to the myTTadmin system (emailing
'timetable.harrison@exeter.ac.uk' should work) and copy it into the same folder,
calling it 'tutorials.txt'. If you're not sure whether the format of the
tutorial groups .txt file you have is the right one, see the description at the
end of this document. If you are given a .php.html file, open it in a browser
and copy the relevant blocks of information into 'tutorials.txt'.


(4) If you have a Linux machine or MAC (or Windows with a Bash shell),
run the master file, 'generate_records.sh': Open a terminal, switch to the
folder, and run the command 'bash generate_records.sh'.
If you have a Windows machine,
{TODO: fill in instructions for Windows}
Note that, either way, Perl and Python need to be installed on your machine.
There may be warnings, never mind them.


(5) You now have a folder called 'ILPs_by_tutors' in the folder. It contains
the ILP records bundled for each tutor. Those records are .pdf documents,
ready to be emailed to the tutors. If a python package needed for the generation
of .pdf files is not installed on your machine, .html files will be generated
instead (this is slightly less convenient: you could open them in a browser,
export to .pdf or print to file, and email them to the tutors; see the comment
at the beginning of 'generate_tutor_ilps.py' for more information on that).


(6) You further have a list of students with ILPs ('single_list.txt') in
the folder, and the same list grouped by tutors ('grouped_list.txt').


=====
Format of the tutorial groups .txt file, 'tutorials.txt':

This file should consists of a number of blocks, each of them describing one
tutorial for the module. Each block starts with some information containing one
line that states the tutor name in one of the following three formats:

Staff allocation: Amy, Wong
Staff allocation: Dr John, Zoidberg
Staff allocation: Prof Hubert, Farnsworth

(The format 'Forename, Surname' might not be entirely correct -- if this is
changed in the generation of the tutorial groups file we are working with, the
script 'grouped_list.py' may need to be adjusted.)

This is then followed by a list of students in the format

SURNAME, FORENAME [MIDDLE NAMES], STUDENT_ID
