import setuptools
with open('README.md','r') as file:
    Long_description=file.read()

setuptools.setup(
    name='preprocess_kgptalkie',#this should be unique
     version='0.0.2',
     author='vishal chauhan',
     author_email='indvis2000@gmail.com',
     description='this is preprocessing package',
     long_description=Long_description,
     Long_description_content_type='text/markdown',
     packages=setuptools.find_packages(),
     classifiers=[
         'Progamming_Language::Python::3',
         'License::OSI Aproved::MIT License',
         'Operating System::OS Independent'],
     python_requires='>=3.5'
)
     