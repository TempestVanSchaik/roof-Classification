# Classiying building's roof-type with CNTK and Workbench, using transfer learning

Read the blog post to find out more: https://blogs.technet.microsoft.com/uktechnet/2018/04/18/classifying-the-uks-roofs-from-aerial-imagery-using-deep-learning-with-cntk/

### Setup:

In Workbench, make sure that the working directory for the project, i.e. its location, is the root folder downloaded from git. That is, one level up from the "scripts" folder.

If you get "Error. Your total project size is 37.31 MB which exceeds the limit of 25 MB. Please see http://aka.ms/aml-largefiles on how to work with large files." Make sure you haven't put any large files inside the project folder, this is only for code.

This project is configured to run on a GPU. The easiest way to access a GPU is to create a Deep Learning Virtual Machine which has a GPU. Within the Azure Portal (https://ms.portal.azure.com), click on Virtual Machines>Add and then search for Deep Learning Virtual Machine. Once deployed, start it up and then connect to it using RDP. 


### Dependencies:

From Workbench, launch Powershell by clickig File>Open Powershell, and then run these commands to install the necessary packages:

pip install https://cntk.ai/PythonWheel/GPU/cntk-2.0-cp35-cp35m-win_amd64.whl
 
pip install opencv_python-3.3.1-cp35-cp35m-win_amd64.whl after downloading the OpenCV wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs/ (the exact filename and version can change)

conda install pillow
 
pip install -U numpy

pip install bqplot

jupyter nbextension enable --py --sys-prefix bqplot

### Running the project

Run Scripts 0-5 in order

