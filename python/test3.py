#!/usr/bin/python

import matplotlib.pyplot as plt

def myplot(data, bins):
    plt.plot(data,bins)
data = (0.388547161964,
        0.417704616597,
        0.426679508789,
        0.430948055075,
        0.433837532561,
        0.435326051266,
        0.436748900028,
        0.437821509095,
        0.438872228181,
        0.439288137819)
bins = [(9-a)/10.0 for a in range(10)]
plt.subplot(221)
myplot(bins, data)
plt.subplot(222)
myplot(data,bins)
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')
pp.savefig()
pp.close()
#!/usr/bin/python

