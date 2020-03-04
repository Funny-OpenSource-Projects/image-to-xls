# pix-to-xls

A simple tool to make ascii art from an image using excel colored cells.


![mario](images/mario@2x-min.png)
  
## How to use

### Online

Just go to https://pix-to-xls.now.sh/ 

![mario](images/screenshot-min.png)

### As python package

Install Python package:

```bash
pip3 install pix-to_xls
```

You can import this package too.

```python
from pix_to_xls import builder

builder.build("your_image.jpg", "your_output_file.xls", cols=50)
```

### Cli


We provide a cli interface for easiest way to use.

Install Python package:

```bash
pip3 install pix-to-xls
```

Use with `pix-to-xls` command

```bash
pix-to-xls your_image.jpg your_output_file.xls
```

### Examples

![mario](images/monalisa-min.png)



 