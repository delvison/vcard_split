import os, sys

#pass in original vcard file
def split(vcard):
  # create directory to store vcards
  os.makedirs('split_vcards')
  path = os.getcwd() + '/split_vcards'
  os.chdir(path)

  # declare vcard file count
  count = 0

  # open original vcard file
  f = open(vcard, 'r')
  v_temp = None
  
  # split large vcf into multiple
  for line in f:
    if line.startswith('BEGIN:VCARD'):
      print("...splitting number "+str(count))
      v_temp = open(str(count)+'.vcf','w')
    if v_temp is not None:
      v_temp.write(line)
    if line.startswith('END:VCARD') and v_temp is not None:
      count+=1
      
split(sys.argv[1])
